"""
Modbus TCP Server management module.

Handles Modbus context building, server lifecycle (start/stop),
and register updates with energy data.
"""

import logging
import os
import struct
import threading
import time

from pymodbus.datastore import ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.server import StartTcpServer
from pymodbus.transaction import ModbusSocketFramer

logger = logging.getLogger(__name__)

MODBUS_PORT = 502
CORR_FACTOR = 1

# Global state
lock = threading.Lock()
_modbus_state = {"last_logged_minute": -1}

# Server components
rt = None
server_thread = None
waiting_for_valid = False


class LoggingDataBlock(ModbusSparseDataBlock):
    """Custom data block that logs register access when debug mode is enabled."""

    def __init__(self, *args, config_manager=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_manager = config_manager
        self.read_count = 0
        self.write_count = 0

    def getValues(self, address, count=1):
        """Get register values and log if debug mode enabled."""
        values = super().getValues(address, count)
        if self.config_manager and self.config_manager.config.get("debug", {}).get(
            "modbus_requests", False
        ):
            self.read_count += 1
            logger.info(
                "[MODBUS-DEBUG] Read #%d - Address: %d, Count: %d, Values: %s",
                self.read_count,
                address,
                count,
                list(values) if values else [],
            )
        return values

    def setValues(self, address, values, use_as_default=None):
        """Set register values and log if debug mode enabled."""
        super().setValues(address, values, use_as_default)
        if self.config_manager and self.config_manager.config.get("debug", {}).get(
            "modbus_requests", False
        ):
            self.write_count += 1
            logger.info(
                "[MODBUS-DEBUG] Write #%d - Address: %d, Values: %s",
                self.write_count,
                address,
                list(values) if values else [],
            )


class RepeatedTimer:
    """Helper class to run a function at regular intervals in a separate thread."""

    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        """Start the timer to run the function periodically."""
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        """Stop the periodic execution of the function."""
        self._timer.cancel()
        self.is_running = False


def calculate_register(value_float):
    """
    Converts a floating-point value into two 16-bit integer registers.

    Uses IEEE 754 floating-point representation for Modbus communication.
    """
    if value_float == 0:
        int1 = 0
        int2 = 0
    else:
        value_hex = hex(struct.unpack("<I", struct.pack("<f", value_float))[0])
        value_hex_part1 = str(value_hex)[2:6]
        value_hex_part2 = str(value_hex)[6:10]
        int1 = int(value_hex_part1, 16)
        int2 = int(value_hex_part2, 16)
    return (int1, int2)


def stop_and_wait_for_valid(reason: str) -> None:
    """
    Stop Modbus server and timer, set flag to wait for valid energy data.

    The main loop in modbus_tcp_smartmeter.py will detect this flag and
    restart services when energy becomes valid again.
    """
    global rt, server_thread, waiting_for_valid
    logger.error(
        "[MODBUS] Error: %s - stopping server and waiting for valid data", reason
    )

    try:
        if rt:
            rt.stop()
        rt = None
        server_thread = None
    except RuntimeError as exc:
        logger.error("[MAIN] Shutdown error: %s", exc)

    waiting_for_valid = True
    logger.warning("[MAIN] Server stopped. Waiting for valid energy data...")


def build_modbus_context(config_manager):
    """
    Build and configure the Modbus TCP server context with data blocks and registers.

    Returns a ModbusServerContext with all register values initialized.
    """
    lock.acquire()
    modbus_tcp_address = int(
        240 + config_manager.config["modbus"]["modbus_tcp_address"]
    )
    serial_number_increment = int(
        50 + config_manager.config["modbus"]["modbus_tcp_address"]
    )
    logger.info(
        "[MAIN] Modbus TCP Address: %s and serial number fragment: %s",
        modbus_tcp_address,
        serial_number_increment,
    )
    if modbus_tcp_address > 254:
        logger.error(
            "[MAIN] Error: Modbus TCP Address is out of range. Too much Smart Meters"
        )
        os._exit(1)

    # Use logging data block if debug mode is enabled
    if config_manager.config.get("debug", {}).get("modbus_requests", False):
        datablock = LoggingDataBlock(
            config_manager=config_manager,
            values={
                40001: [21365, 28243],
                40003: [1],
                40004: [65],
                40005: [
                    70,
                    114,
                    111,
                    110,
                    105,
                    117,
                    115,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,  # Manufacturer "Fronius"
                    83,
                    109,
                    97,
                    114,
                    116,
                    32,
                    77,
                    101,
                    116,
                    101,
                    114,
                    32,
                    54,
                    51,
                    65,
                    0,  # Device Model "Smart Meter 63A"
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,  # Options N/A
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,  # Software Version N/A
                    48,
                    48,
                    48,
                    48,
                    48,
                    48,
                    48,
                    serial_number_increment,  # Serial Number
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    modbus_tcp_address,
                ],
                40070: [213],
                40071: [124],
                40072: [0] * 124,  # Initialize with zeros
                40196: [65535, 0],
            },
        )
    else:
        datablock = ModbusSparseDataBlock(
            {
                40001: [21365, 28243],
                40003: [1],
                40004: [65],
                40005: [
                    70,
                    114,
                    111,
                    110,
                    105,
                    117,
                    115,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,  # Manufacturer "Fronius"
                    83,
                    109,
                    97,
                    114,
                    116,
                    32,
                    77,
                    101,
                    116,
                    101,
                    114,
                    32,
                    54,
                    51,
                    65,
                    0,  # Device Model "Smart Meter 63A"
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,  # Options N/A
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,  # Software Version N/A
                    48,
                    48,
                    48,
                    48,
                    48,
                    48,
                    48,
                    serial_number_increment,  # Serial Number
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    modbus_tcp_address,
                ],
                40070: [213],
                40071: [124],
                40072: [0] * 124,  # Initialize with zeros
                40196: [65535, 0],
            }
        )

    slave_store = ModbusSlaveContext(
        di=datablock,
        co=datablock,
        hr=datablock,
        ir=datablock,
    )

    a_context = ModbusServerContext(slaves=slave_store, single=True)

    lock.release()
    return a_context


def start_modbus_services(context, energy_data_instance, config_manager_instance):
    """
    Start the Modbus TCP server and the periodic update timer.

    Runs the server in a daemon thread to allow graceful shutdown.

    Args:
        context: Modbus server context
        energy_data_instance: EnergyData instance for fetching values
        config_manager_instance: ConfigManager instance for configuration
    """
    global rt, server_thread

    logger.info("[MAIN] Starting Modbus TCP server on port %s...", MODBUS_PORT)

    # Log debug mode status
    if config_manager_instance.config.get("debug", {}).get("modbus_requests", False):
        logger.info(
            "[MAIN] Modbus request debugging enabled - will log all incoming requests"
        )
    else:
        logger.debug("[MAIN] Modbus request debugging disabled")

    # Start the repeated timer for periodic register updates
    repetition_time = 2
    rt = RepeatedTimer(
        repetition_time,
        updating_writer,
        context,
        energy_data_instance,
        config_manager_instance,
    )

    # Create and start the Modbus TCP server in a daemon thread
    def run_server(context):
        try:
            address = ("", MODBUS_PORT)
            StartTcpServer(
                context=context,
                address=address,
                framer=ModbusSocketFramer,
            )
        except OSError as exc:
            logger.error("[MODBUS] Server error: %s", exc)

    server_thread = threading.Thread(target=run_server, args=(context,), daemon=True)
    server_thread.start()

    logger.info("[MAIN] Modbus TCP server started, listening on %s", MODBUS_PORT)


def stop_modbus_services():
    """
    Stop the Modbus TCP server and the periodic update timer gracefully.
    """
    global rt, server_thread

    logger.info("[MAIN] Stopping Modbus TCP server...")
    try:
        if rt:
            rt.stop()
            rt = None
        if server_thread:
            server_thread.join(timeout=2)
            server_thread = None
    except (RuntimeError, OSError) as exc:
        logger.error("[MAIN] Error stopping services: %s", exc)

    logger.info("[MAIN] Modbus TCP server stopped")


def updating_writer(a_context, energy_data_instance, config_manager_instance):
    """
    Updates Modbus context with data retrieved from energy data service.

    Called every 2 seconds by RepeatedTimer to update register values.
    Handles server restart when energy recovers from below-threshold state.

    Args:
        a_context: Modbus server context
        energy_data_instance: EnergyData instance for fetching values
        config_manager_instance: ConfigManager instance for configuration
    """
    # This should never execute - updating_writer() won't be called when timer is stopped
    # Recovery is now handled in the main loop
    if waiting_for_valid:
        logger.error(
            "[MODBUS] BUG: updating_writer() called while waiting_for_valid=True"
        )
        return

    inverter_energy_total_out = float(energy_data_instance.get_energy_value()) * 1000

    # Emergency check - this shouldn't happen as EnergyData already validates
    min_threshold_wh = (
        config_manager_instance.config["smartmeter_energy"].get(
            "min_energy_threshold", 0.1
        )
        * 1000
    )
    if inverter_energy_total_out < min_threshold_wh:
        logger.error(
            "[MODBUS] Error: inverter_energy_total_out is %.2f Wh (below threshold of %.2f Wh) "
            "- emergency shutdown to prevent wrong counter values",
            inverter_energy_total_out,
            min_threshold_wh,
        )
        os._exit(1)

    inverter_energy_total_in = 0

    input_power = float(energy_data_instance.get_power_value()) * -1
    input_voltage = float(energy_data_instance.get_voltage_value())
    input_current = float(energy_data_instance.get_current_value())
    input_frequency = float(energy_data_instance.get_frequency_value())

    # Ensure frequency has a valid value
    if input_frequency <= 0:
        input_frequency = 50.0

    connected_phase = config_manager_instance.config["modbus"]["connected_phase"]
    if connected_phase == 1:
        l1, v1, i1 = input_power, input_voltage, input_current
        l2, v2, i2 = 0, v1, 0
        l3, v3, i3 = 0, v1, 0
    elif connected_phase == 2:
        l2, v2, i2 = input_power, input_voltage, input_current
        l1, v1, i1 = 0, v2, 0
        l3, v3, i3 = 0, v2, 0
    elif connected_phase == 3:
        l3, v3, i3 = input_power, input_voltage, input_current
        l1, v1, i1 = 0, v3, 0
        l2, v2, i2 = 0, v3, 0
    else:
        logger.error(
            "[MODBUS] Error: connected_phase is not set correctly - emergency shutdown"
        )
        stop_and_wait_for_valid("Invalid connected_phase")
        return

    # Heartbeat logging
    current_time = time.localtime()
    if current_time.tm_min != _modbus_state["last_logged_minute"]:
        _modbus_state["last_logged_minute"] = current_time.tm_min
        logger.info(
            "[MODBUS] heartbeat - recent update for Modbus Registers with energy data "
            "for phase %s - energy: %d, P: %s, U: %s, I: %s, F: %s",
            connected_phase,
            int(inverter_energy_total_out),
            input_power,
            input_voltage,
            input_current,
            input_frequency,
        )

    lock.acquire()

    # Apply correction factor
    inverter_energy_total_in_corr = float(inverter_energy_total_in) * int(CORR_FACTOR)
    inverter_energy_total_out_corr = float(inverter_energy_total_out) * int(CORR_FACTOR)

    # Convert values to Modbus registers
    power_total_int1, power_total_int2 = calculate_register(float(input_power))
    current_total_int1, current_total_int2 = calculate_register(float(input_current))
    ti_int1, ti_int2 = calculate_register(inverter_energy_total_in_corr)

    exp_int1, exp_int2 = calculate_register(inverter_energy_total_out_corr)

    exp_tot_int1, exp_tot_int2 = (0, 0)
    exp1_int1, exp1_int2 = (0, 0)
    exp2_int1, exp2_int2 = (0, 0)
    exp3_int1, exp3_int2 = (0, 0)

    if connected_phase == 1:
        exp_tot_int1, exp_tot_int2 = calculate_register(inverter_energy_total_out_corr)
        exp1_int1, exp1_int2 = calculate_register(inverter_energy_total_out_corr)
        exp2_int1, exp2_int2 = (0, 0)
        exp3_int1, exp3_int2 = (0, 0)
    elif connected_phase == 2:
        exp_tot_int1, exp_tot_int2 = calculate_register(inverter_energy_total_out_corr)
        exp1_int1, exp1_int2 = (0, 0)
        exp2_int1, exp2_int2 = calculate_register(inverter_energy_total_out_corr)
        exp3_int1, exp3_int2 = (0, 0)
    elif connected_phase == 3:
        exp_tot_int1, exp_tot_int2 = calculate_register(inverter_energy_total_out_corr)
        exp1_int1, exp1_int2 = (0, 0)
        exp2_int1, exp2_int2 = (0, 0)
        exp3_int1, exp3_int2 = calculate_register(inverter_energy_total_out_corr)

    l1_int1, l1_int2 = calculate_register(float(l1))
    l2_int1, l2_int2 = calculate_register(float(l2))
    l3_int1, l3_int2 = calculate_register(float(l3))

    v1_int1, v1_int2 = calculate_register(float(v1))
    v2_int1, v2_int2 = calculate_register(float(v2))
    v3_int1, v3_int2 = calculate_register(float(v3))

    i1_int1, i1_int2 = calculate_register(float(i1))
    i2_int1, i2_int2 = calculate_register(float(i2))
    i3_int1, i3_int2 = calculate_register(float(i3))

    f1_int1, f1_int2 = calculate_register(float(input_frequency))

    # updating the context with new values
    context = a_context[0]
    register = 3
    # slave_id = 0x01
    address = 0x9C87  # 40000 + 3960

    values = [
        current_total_int1,
        0,  # AC Total Current value [A]
        i1_int1,
        i1_int2,  # AC Current value L1 [A]
        i2_int1,
        i2_int2,  # AC Current value L2 [A]
        i3_int1,
        i3_int2,  # AC Current value L3 [A]
        v1_int1,
        v1_int2,  # AC Voltage average phase to neutral [V]
        v1_int1,
        v1_int2,  # AC Voltage phase L1 to neutral [V]
        v2_int1,
        v2_int2,  # AC Voltage phase L2 to neutral [V]
        v3_int1,
        v3_int2,  # AC Voltage phase L3 to neutral [V]
        0,
        0,  # AC Voltage average phase to phase [V]
        0,
        0,  # AC Voltage phase L1 to L2 [V]
        0,
        0,  # AC Voltage phase L2 to L3 [V]
        0,
        0,  # AC Voltage phase L1 to L3 [V]
        f1_int1,
        f1_int2,  # AC Frequency [Hz]
        power_total_int1,
        power_total_int2,  # AC Power value (Total) [W]
        l1_int1,
        l1_int2,  # AC Power value L1 [W]
        l2_int1,
        l2_int2,  # AC Power value L2 [W]
        l3_int1,
        l3_int2,  # AC Power value L3 [W]
        0,
        0,  # AC Power scale factor
        0,
        0,  # AC VA phase A
        0,
        0,  # AC VA phase B
        0,
        0,  # AC VA phase C
        0,
        0,  # AC VA scale factor
        0,
        0,  # AC VAR phase A
        0,
        0,  # AC VAR phase B
        0,
        0,  # AC VAR phase C
        0,
        0,  # AC VAR scale factor
        0,
        0,  # AC PF average
        0,
        0,  # AC PF phase A
        0,
        0,  # AC PF phase B
        0,
        0,  # AC PF phase C
        0,
        0,  # AC PF scale factor
        exp_tot_int1,
        exp_tot_int2,  # Total Watt Hours Exported [Wh]
        exp1_int1,
        exp1_int2,  # Watt Hours Exported L1 [Wh]
        exp2_int1,
        exp2_int2,  # Watt Hours Exported L2 [Wh]
        exp3_int1,
        exp3_int2,  # Watt Hours Exported L3 [Wh]
        ti_int1,
        ti_int2,  # Total Watt Hours Imported [Wh]
        0,
        0,  # Watt Hours Imported L1 [Wh]
        0,
        0,  # Watt Hours Imported L2 [Wh]
        0,
        0,  # Watt Hours Imported L3 [Wh]
        0,
        0,  # Total VA hours Exported [VA]
        0,
        0,  # VA hours Exported L1 [VA]
        0,
        0,  # VA hours Exported L2 [VA]
        0,
        0,  # VA hours Exported L3 [VA]
        0,
        0,  # Total VAr hours imported [VAr]
        0,
        0,  # VA hours imported L1 [VAr]
        0,
        0,  # VA hours imported L2 [VAr]
        0,
        0,  # VA hours imported L3 [VAr]
    ]

    context.setValues(register, address, values)
    time.sleep(1)
    lock.release()
