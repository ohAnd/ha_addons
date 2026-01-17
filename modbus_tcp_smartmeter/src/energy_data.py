"""
Energy data retrieval and management module.

Handles fetching energy, voltage, current, power, and frequency data
from OpenHAB or Home Assistant, with background update service.
"""

import logging
import threading
import time
import requests

logger = logging.getLogger(__name__)

OPENHAB_PORT = "8080"


def isfloat(num):
    """Checks if the given input can be converted to a float."""
    try:
        float(num)
        return True
    except ValueError:
        return False


class EnergyData:
    """
    Manages energy-related data by fetching it from OpenHAB or Home Assistant REST API
    and periodically updating the state in the background.
    """

    def __init__(self, config, config_manager, stop_callback=None):
        """
        Initialize EnergyData with configuration.

        Args:
            config: Flattened config dict with item names
            config_manager: ConfigManager instance for accessing nested config
            stop_callback: Function to call when energy drops below threshold
        """
        self.energy_data = {
            "energy_counter_out": {"value": -1, "configured": False},
            "current_voltage": {"value": -1, "configured": False},
            "current_current": {"value": -1, "configured": False},
            "current_power": {"value": -1, "configured": False},
            "current_frequency": {"value": 50.0, "configured": False},
        }
        self.energy_data_last = {
            key: value.copy() if isinstance(value, dict) else value
            for key, value in self.energy_data.items()
        }
        self.config = config
        self.config_manager = config_manager
        self.stop_callback = stop_callback
        self.last_source_valid = True  # Track if last source read was valid
        self.__check_config()

        self.update_interval = 2
        self._update_thread = None
        self._stop_event = threading.Event()
        self.start_update_service()

    def __check_config(self):
        """Checks if the configuration is valid and sets the configured flag for each item."""
        for item, data in self.energy_data.items():
            if item in self.config and self.config[item]:
                data["configured"] = True
                logger.info(
                    "[ENERGY-DATA] Config check: item '%s' is configured with value: %s",
                    item,
                    self.config[item],
                )
            else:
                logger.info(
                    "[ENERGY-DATA] Config check:Item '%s' not found in config or empty. "
                    + "Using default value.",
                    item,
                )
                data["configured"] = False
                data["value"] = 0
                self.energy_data_last[item]["value"] = 0

    def __get_data_from_external_item(self, item):
        """Fetches the state of a specified item from OpenHAB or Home Assistant API."""
        data_source = self.config_manager.config["data"]["source"].lower()

        if data_source == "homeassistant":
            return self.__get_data_from_homeassistant(item)
        else:
            return self.__get_data_from_openhab(item)

    def __get_data_from_openhab(self, item):
        """Fetches from OpenHAB REST API."""
        url = (
            "http://"
            + self.config_manager.config["data"]["host"]
            + ":"
            + OPENHAB_PORT
            + "/rest/items/"
            + item
        )
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.Timeout:
            logger.error(
                "[OPENHAB_IF] Timeout error: Could not fetch data from OpenHAB for item: %s",
                item,
            )
            return 0
        except requests.exceptions.ConnectionError:
            logger.error(
                "[OPENHAB_IF] Connection error: Could not connect to OpenHAB for item: %s",
                item,
            )
            return 0
        except requests.exceptions.HTTPError as http_err:
            logger.error(
                "[OPENHAB_IF] HTTP error: %s while fetching data for item: %s",
                http_err,
                item,
            )
            return 0
        except requests.exceptions.RequestException as req_err:
            logger.error(
                "[OPENHAB_IF] Request error: %s while fetching data for item: %s",
                req_err,
                item,
            )
            return 0
        except ValueError:
            logger.error(
                "[OPENHAB_IF] JSON decoding error: Could not parse response for item: %s",
                item,
            )
            return 0
        if "error" in data:
            logger.error(
                "[OPENHAB_IF] Error: Could not fetch data from OpenHAB for item: %s - error: %s",
                item,
                data["error"]["message"],
            )
            return 0
        if "state" in data:
            if isfloat(data["state"]):
                return float(data["state"])
            if data["state"].split()[0] != "NULL":
                return float(data["state"].split()[0])
        return 0

    def __get_data_from_homeassistant(self, entity):
        """Fetches the state of a specified entity from Home Assistant REST API."""
        host = self.config_manager.config["data"]["host"]
        token = self.config_manager.config["data"].get("access_token", "")

        url = f"http://{host}:8123/api/states/{entity}"

        try:
            headers = {}
            if token:
                headers["Authorization"] = f"Bearer {token}"

            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.Timeout:
            logger.error(
                "[HA_IF] Timeout error: Could not fetch data from Home Assistant for entity: %s",
                entity,
            )
            return 0
        except requests.exceptions.ConnectionError:
            logger.error(
                "[HA_IF] Connection error: Could not connect to Home Assistant at %s for entity: %s",
                host,
                entity,
            )
            return 0
        except requests.exceptions.HTTPError as http_err:
            logger.error(
                "[HA_IF] HTTP error: %s while fetching data for entity: %s",
                http_err,
                entity,
            )
            return 0
        except requests.exceptions.RequestException as req_err:
            logger.error(
                "[HA_IF] Request error: %s while fetching data for entity: %s",
                req_err,
                entity,
            )
            return 0
        except ValueError:
            logger.error(
                "[HA_IF] JSON decoding error: Could not parse response for entity: %s",
                entity,
            )
            return 0

        if "state" in data:
            state_value = data.get("state", "")
            if isfloat(state_value):
                return float(state_value)
            try:
                return float(str(state_value).split()[0])
            except (ValueError, IndexError):
                logger.error(
                    "[HA_IF] Could not parse state value: %s for entity: %s",
                    state_value,
                    entity,
                )
                return 0
        return 0

    def __update_item(self, itemname: str) -> None:
        """Update energy data item with value from configured source."""
        if not self.energy_data[itemname]["configured"]:
            return

        try:
            item_value = self.__get_data_from_external_item(self.config[itemname])
            if not isfloat(item_value):
                logger.error(
                    "[ENERGY-DATA] Error: Invalid data type for item: %s - "
                    "using last known value: %s",
                    itemname,
                    self.energy_data_last[itemname]["value"],
                )
                self.energy_data[itemname]["value"] = self.energy_data_last[itemname][
                    "value"
                ]
                return

            # Check threshold for energy counter
            min_threshold_wh = self.config_manager.config["smartmeter_energy"].get(
                "min_energy_threshold", 0.1
            )
            # Only apply threshold check if we have a valid previous value
            # (prevents rejecting the first valid read on startup)
            if (
                itemname == "energy_counter_out"
                and item_value < min_threshold_wh
                and self.energy_data[itemname]["value"] > 0
            ):
                logger.warning(
                    "[ENERGY-DATA] Warning: Invalid energy value: %s (below threshold of %s kWh) - "
                    "using last known value: %s",
                    item_value,
                    min_threshold_wh,
                    self.energy_data_last[itemname]["value"],
                )
                self.last_source_valid = False  # Mark source as invalid
                # Trigger stop callback - main loop checks if server is actually running
                if self.stop_callback:
                    self.stop_callback("Energy below threshold during runtime")
                return

            # Check for backwards energy counter (energy should never decrease)
            if (
                itemname == "energy_counter_out"
                and self.energy_data[itemname]["value"] > 0  # Have previous valid value
                and item_value
                < self.energy_data[itemname]["value"]  # New value is lower
            ):
                logger.warning(
                    "[ENERGY-DATA] Warning: Energy counter went backwards: %s < last valid %s - "
                    "using last known value: %s",
                    item_value,
                    self.energy_data[itemname]["value"],
                    self.energy_data_last[itemname]["value"],
                )
                # Don't mark source as invalid or stop server - just use last valid value
                # This is a data glitch, not a fundamental problem like threshold violations
                return

            # Update with valid value
            self.energy_data[itemname]["value"] = round(item_value, 3)
            self.energy_data_last[itemname]["value"] = self.energy_data[itemname][
                "value"
            ]
            # Mark source as valid when we successfully update
            if itemname == "energy_counter_out":
                self.last_source_valid = True

        except (requests.exceptions.RequestException, ValueError, KeyError) as e:
            logger.error("[ENERGY-DATA] Error updating %s: %s", itemname, e)
            self.energy_data[itemname]["value"] = self.energy_data_last[itemname][
                "value"
            ]

    def get_energy_value(self):
        """Returns the current energy value."""
        return self.energy_data["energy_counter_out"]["value"]

    def get_voltage_value(self):
        """Returns the current voltage value."""
        return self.energy_data["current_voltage"]["value"]

    def get_current_value(self):
        """Returns the current value."""
        return self.energy_data["current_current"]["value"]

    def get_power_value(self):
        """Returns the current power value."""
        return self.energy_data["current_power"]["value"]

    def get_frequency_value(self):
        """Returns the current frequency value."""
        value = self.energy_data["current_frequency"]["value"]
        if not self.energy_data["current_frequency"]["configured"] and value <= 0:
            return 50.0  # Default European grid frequency
        return value

    def start_update_service(self):
        """Starts the background thread to periodically update the state."""
        if self._update_thread is None or not self._update_thread.is_alive():
            self._stop_event.clear()
            self._update_thread = threading.Thread(
                target=self._update_state_loop, daemon=True
            )
            self._update_thread.start()
            logger.info("[ENERGY-DATA] Update service started.")

    def shutdown(self):
        """Stops the background thread and shuts down the update service."""
        if self._update_thread and self._update_thread.is_alive():
            self._stop_event.set()
            self._update_thread.join()
            logger.info("[ENERGY-DATA] Update service stopped.")

    def _update_state_loop(self):
        """The loop that runs in the background thread to update the state."""
        last_values = {}

        while not self._stop_event.is_set():
            self.__update_item("energy_counter_out")
            self.__update_item("current_voltage")
            self.__update_item("current_current")
            self.__update_item("current_power")
            self.__update_item("current_frequency")

            # Only log if values have changed
            current_values = {
                item: self.energy_data[item]["value"]
                for item in self.energy_data
                if self.energy_data[item]["configured"]
            }

            if current_values != last_values:
                logger.debug("[ENERGY-DATA] Updated items: %s", current_values)
                last_values = current_values.copy()

            # Break the sleep interval into smaller chunks to allow immediate shutdown
            sleep_interval = self.update_interval
            while sleep_interval > 0:
                if self._stop_event.is_set():
                    return
                time.sleep(min(1, sleep_interval))
                sleep_interval -= 1
