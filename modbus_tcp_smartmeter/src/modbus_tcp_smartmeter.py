#!/usr/bin/env python3
"""
Smart Meter Modbus TCP Emulator

Simulates a Smart Meter for providing necessary
information to inverters (e.g. Gen24).

Based on:
https://github.com/tichachm/fronius_smart_meter_modbus_tcp_emulator
https://www.photovoltaikforum.com/thread/185108-fronius-smart-meter-tcp-protokoll
"""

import logging
import os
import signal
import sys
import time

# Import local modules
from .modbus_server import rt as server_rt
from .config_manager import ConfigManager
from .energy_data import EnergyData, isfloat
from . import modbus_server
from .modbus_server import (
    build_modbus_context,
    start_modbus_services,
    stop_modbus_services,
    stop_and_wait_for_valid,
)

###############################################################
# Logging Setup
###############################################################
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Reduce noise from external libraries
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("pymodbus").setLevel(logging.WARNING)

###############################################################
# Global instances
###############################################################
config_manager = None
energy_data = None


def signal_handler(sig, frame):
    """
    Handles the termination signal (e.g., Ctrl+C) to clean up resources.
    """
    logger.info("[MAIN] Stopping server...")
    stop_modbus_services()
    if energy_data:
        energy_data.shutdown()
    logger.info("[MAIN] Server stopped.")
    sys.exit(0)


# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)


def main():
    """Main entry point for the application."""
    global config_manager, energy_data

    # Load configuration
    config_manager = ConfigManager()

    # Set logging level from config
    log_level = config_manager.config["general"]["loglevel"].upper()
    logging.getLogger().setLevel(getattr(logging, log_level, logging.DEBUG))

    # Prepare flat config for EnergyData from nested structure
    energy_items_config = {
        **config_manager.config["smartmeter_energy"],
        **config_manager.config["smartmeter_livedata"],
    }

    # Create energy data instance with callback for threshold violations
    def stop_callback_wrapper(reason):
        """Wrapper to check if server is running before stopping."""

        if server_rt is not None:
            stop_and_wait_for_valid(reason)

    energy_data = EnergyData(
        energy_items_config, config_manager, stop_callback=stop_callback_wrapper
    )

    # Wait until we have a valid energy value before exposing Modbus
    min_energy_threshold = config_manager.config["smartmeter_energy"].get(
        "min_energy_threshold", 0.1
    )
    logger.info(
        "[MAIN] Waiting for valid energy data (threshold %.3f kWh)...",
        min_energy_threshold,
    )

    while True:
        current_energy = energy_data.get_energy_value()
        if isfloat(current_energy) and current_energy >= min_energy_threshold:
            logger.info(
                "[MAIN] Energy data available (%.3f kWh >= threshold %.3f kWh)."
                + " Starting Modbus TCP server...",
                current_energy,
                min_energy_threshold,
            )
            break

        logger.warning(
            "[MAIN] Waiting for valid energy data (current: %.3f kWh, threshold: %.3f kWh)...",
            current_energy if isfloat(current_energy) else -1,
            min_energy_threshold,
        )
        time.sleep(2)

    # Set timezone from config
    try:
        tz = os.environ["TZ"]
        logger.info("[MAIN] host system time zone is %s", tz)
    except KeyError:
        logger.info(
            "[MAIN] host system time zone was not set. Setting to config value: %s",
            config_manager.config["general"]["time_zone"],
        )
        os.environ["TZ"] = config_manager.config["general"]["time_zone"]

    # Build context and start services
    context = build_modbus_context(config_manager)
    start_modbus_services(context, energy_data, config_manager)

    # Keep the main thread running and monitor for recovery after stops
    try:
        while True:
            time.sleep(2)
            # Check if server was stopped due to bad energy and needs recovery
            if modbus_server.waiting_for_valid:
                current_energy = energy_data.get_energy_value()
                min_energy_threshold = config_manager.config["smartmeter_energy"].get(
                    "min_energy_threshold", 0.1
                )
                # Only restart if energy is valid AND source is actually sending valid data
                # (checking rt is None prevents restart loop during stop transition)
                if (
                    current_energy >= min_energy_threshold
                    and energy_data.last_source_valid
                    and modbus_server.rt is None
                ):
                    logger.info(
                        "[MAIN] Valid energy data recovered (%.3f kWh >= threshold %.3f kWh)."
                        + " Restarting Modbus server...",
                        current_energy,
                        min_energy_threshold,
                    )
                    modbus_server.waiting_for_valid = False
                    context = build_modbus_context(config_manager)
                    start_modbus_services(context, energy_data, config_manager)
    except KeyboardInterrupt:
        signal_handler(None, None)


if __name__ == "__main__":
    main()
