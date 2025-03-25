#!/usr/bin/env python3
"""
sniplet from
https://github.com/tichachm/fronius_smart_meter_modbus_tcp_emulator

Simulates a Fronius Smart Meter for providing necessary
information to inverters (e.g. Gen24).

Based on
https://www.photovoltaikforum.com/thread/185108-fronius-smart-meter-tcp-protokoll
https://www.photovoltaikforum.com/thread/185108-fronius-smart-meter-tcp-protokoll/?postID=2760134#post2760134
"""
###############################################################
# Import Libs
###############################################################
import os
import logging
import signal
import sys
import threading
import struct
import time
import requests
import yaml

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer

# import json
# import getopt
# import sys
# import socket
# import signal
# import os

from pymodbus.server import StartTcpServer

from pymodbus.transaction import (
    ModbusAsciiFramer,
    ModbusBinaryFramer,
    ModbusSocketFramer,
    ModbusTlsFramer,
)

###############################################################
# Configuration
###############################################################

OPENHAB_PORT = "8080"
MODBUS_PORT = 502
CORR_FACTOR = 1 # or 1000

###############################################################
# Add a global variable to store the timer instance
rt = None

###############################################################
class ConfigManager:
    '''
    Manages the configuration settings for the application.

    This class handles loading, updating, and saving configuration settings from a 'config.yaml'
    file. If the configuration file does not exist, it creates one with default values and
    prompts the user to restart the server.
    '''
    def __init__(self):
        self.config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yaml')
        self.default_config = {
            'connected_phase': 1,
            'energy_counter_out': 'inverter_energy',
            'current_voltage': 'inverter_voltage',
            'current_current': 'inverter_current',
            'current_power': 'inverter_power',
            'openhab_host': '192.168.1.99',
            'modbus_tcp_address': 0,
            'time_zone': 'UTC',  # Add default time zone
            'loglevel': 'debug'
        }
        self.config = self.default_config.copy()
        self.load_config()

    def load_config(self):
        """
        Reads the configuration from 'config.yaml' file located in the current directory.
        If the file exists, it loads the configuration values.
        If the file does not exist, it creates a new 'config.yaml' file with default values and
        prompts the user to restart the server after configuring the settings.
        """
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config.update(yaml.safe_load(f))
        else:
            print("ERROR - Config file not found. [config.yaml]")
            print("Creating a new config file with default values...")
            self.save_config()
            print("Please configure the settings in the 'config.yaml' file and restart the server.")
            sys.exit(0)
    
    def save_config(self):
        """
        Saves the configuration settings to the 'config.yaml' file.
        """
        with open(self.config_file, 'w', encoding='utf-8') as f:
            yaml.dump(self.config, f, default_flow_style=False)

config_manager = ConfigManager()
###############################################################

LOGLEVEL = config_manager.config["loglevel"].upper()

# Clear existing handlers from the root logger
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S"
    )
    streamhandler = logging.StreamHandler(sys.stdout)
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)
logger.setLevel(LOGLEVEL)
logger.info('[MAIN] Starting modbus_tcp_smartmeter')

###############################################################
# Timer Class
###############################################################
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

###############################################################

lock = threading.Lock()

def isfloat(num):
    """
    Checks if the given input can be converted to a float.
    """
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_data_from_openhab_item(item):
    """
    Fetches the state of a specified item from the OpenHAB REST API.
    """
    url = "http://" + config_manager.config["openhab_host"] + ":" + OPENHAB_PORT + "/rest/items/" + item
    response = requests.get(url, timeout=10)  # Set a timeout of 10 seconds
    data = response.json()
    if "error" in data:
        logger.error(
            "[OPENHAB_IF] Error: Could not fetch data from OpenHAB for item: %s - error: %s",
            item, data["error"]["message"]
        )
        return 0
    # logger.debug("[OPENHAB_IF] Data from OpenHAB for item: %s - %s", item, data["state"])
    if "state" in data and isfloat(data["state"]):
        return data["state"]
    return 0


###############################################################
# Update Modbus Registers
###############################################################
def calculate_register(value_float):
    """
    Converts a floating-point value into two 16-bit integer registers.

    This function takes a floating-point number and converts it into two 
    16-bit integer values that represent the lower and upper parts of the 
    32-bit IEEE 754 floating-point representation. This is useful for 
    communication with Modbus devices that require data in register format.
    """
    if value_float == 0:
        int1 = 0
        int2 = 0
    else:
        value_hex = hex(struct.unpack('<I', struct.pack('<f', value_float))[0])
        value_hex_part1 = str(value_hex)[2:6] #extract first register part (hex)
        value_hex_part2 = str(value_hex)[6:10] #extract seconds register part (hex)
        #convert hex to integer because pymodbus converts back to hex itself
        int1 = int(value_hex_part1, 16)
        #convert hex to integer because pymodbus converts back to hex itself
        int2 = int(value_hex_part2, 16)
    return (int1,int2)

def updating_writer(a_context):
    """
    Updates Modbus context with data retrieved from OpenHAB items and calculated values.
    This function retrieves data from OpenHAB items, applies a correction factor, converts
    the values into Modbus register format, and updates the Modbus context with the calculated
    values. It handles various parameters such as power, voltage, current, and energy metrics.

    Notes:
        - The function uses a global lock to ensure thread safety while updating the context.
        - The Modbus context is updated with a predefined structure of values, including
          placeholders for unimplemented metrics.
        - The function sleeps for 1 second before releasing the lock to allow for consistent
          updates.
    """

    inverter_energy_total_out = float(
        get_data_from_openhab_item(config_manager.config["energy_counter_out"])
    ) * 1000

    # inverter_energy_total_out = 0
    # avoid wrong data serving
    if inverter_energy_total_out == 0:
        logger.error(
            "[MODBUS] Error: inverter_energy_total_out is 0 "
            "- emergency shutdown to prevent wrong counter values"
            )
        os._exit(1)  # Forcefully exit the whole application

    inverter_energy_total_in = 0

    input_power = float(get_data_from_openhab_item(config_manager.config["current_power"])) * -1
    input_voltage = float(get_data_from_openhab_item(config_manager.config["current_voltage"]))
    input_current = float(get_data_from_openhab_item(config_manager.config["current_current"]))

    if config_manager.config["connected_phase"] == 1:
        l1 = input_power
        v1 = input_voltage
        i1 = input_current
        l2, v2, i2 = 0, v1, 0
        l3, v3, i3 = 0, v1, 0
    elif config_manager.config["connected_phase"] == 2:
        l2 = input_power
        v2 = input_voltage
        i2 = input_current
        l1, v1, i1 = 0, v2, 0
        l3, v3, i3 = 0, v2, 0
    elif config_manager.config["connected_phase"] == 3:
        l3 = input_power
        v3 = input_voltage
        i3 = input_current
        l1, v1, i1 = 0, v3, 0
        l2, v2, i2 = 0, v3, 0
    else:
        logger.error(
            "[MODBUS] Error: connected_phase is not set correctly - emergency shutdown"
            )
        os._exit(1)  # Forcefully exit the whole application

    logger.debug(
        ("[MODBUS] Updating Modbus Registers with data from OpenHAB for phase %s -"
         " energy: %d, P: %s, U: %s, I: %s"),
        config_manager.config["connected_phase"],
        int(inverter_energy_total_out),
        input_power,
        input_voltage,
        input_current
    )

    # Check if the current time is at the start of a full minute
    current_time = time.localtime()
    if current_time.tm_sec == 0:
        logger.info(
            ("[MODBUS] heartbeat - rectent update for Modbus Registers with data"
             " from OpenHAB for phase %s -"
             " energy: %d, P: %s, U: %s, I: %s"),
            config_manager.config["connected_phase"],
            int(inverter_energy_total_out),
            input_power,
            input_voltage,
            input_current
        )

    lock.acquire()
    #Considering correction factor

    float_inverter_energy_total_in = float(inverter_energy_total_in)
    inverter_energy_total_in_corr = float_inverter_energy_total_in * int(CORR_FACTOR)
    #print (inverter_energy_total_in_corr)

    float_inverter_energy_total_out = float(inverter_energy_total_out)
    inverter_energy_total_out_corr = float_inverter_energy_total_out * int(CORR_FACTOR)
    #print (inverter_energy_total_out_corr)

    #Converting values of payload to Modbus register
    power_total_int1, power_total_int2 = calculate_register(float(input_power))
    current_total_int1, current_total_int2  = calculate_register(float(input_current))
    ti_int1, ti_int2 = calculate_register(inverter_energy_total_in_corr)

    exp_int1, exp_int2 = calculate_register(inverter_energy_total_out_corr)

    exp1_int1, exp1_int2 = (0,0)
    exp2_int1, exp2_int2 = (0,0)
    exp3_int1, exp3_int2 = (0,0)

    if config_manager.config["connected_phase"] == 1:
        exp1_int1, exp1_int2 = calculate_register(inverter_energy_total_out_corr)
        exp2_int1, exp2_int2 = (0,0)
        exp3_int1, exp3_int2 = (0,0)
    if config_manager.config["connected_phase"] == 2:
        exp1_int1, exp1_int2 = (0,0)
        exp2_int1, exp2_int2 = calculate_register(inverter_energy_total_out_corr)
        exp3_int1, exp3_int2 = (0,0)
    if config_manager.config["connected_phase"] == 3:
        exp1_int1, exp1_int2 = (0,0)
        exp2_int1, exp2_int2 = (0,0)
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


    #updating the context
    context = a_context[0]
    register = 3
    # slave_id = 0x01
    address = 0x9C87
    values = [current_total_int1, 0,    #Ampere - AC Total Current Value [A]
              i1_int1, 0,               #Ampere - AC Current Value L1 [A]
              i2_int1, 0,               #Ampere - AC Current Value L2 [A]
              i3_int1, 0,               #Ampere - AC Current Value L3 [A]
              v1_int1, 0,               #Voltage - Average Phase to Neutral [V]
              v1_int1, 0,               #Voltage - Phase L1 to Neutral [V]
              v2_int1, 0,               #Voltage - Phase L2 to Neutral [V]
              v3_int1, 0,               #Voltage - Phase L3 to Neutral [V]
              0, 0,                     #Voltage - Average Phase to Phase [V]
              0, 0,                     #Voltage - Phase L1 to L2 [V]
              0, 0,                     #Voltage - Phase L2 to L3 [V]
              0, 0,                     #Voltage - Phase L1 to L3 [V]
              0, 0,                     #AC Frequency [Hz]
              power_total_int1, 0,      #AC Power value (Total) [W] ==> Second hex word not needed
              l1_int1, 0,               #AC Power Value L1 [W]
              l2_int1, 0,               #AC Power Value L2 [W]
              l3_int1, 0,               #AC Power Value L3 [W]
              0, 0,                     #AC Apparent Power [VA]
              0, 0,                     #AC Apparent Power L1 [VA]
              0, 0,                     #AC Apparent Power L2 [VA]
              0, 0,                     #AC Apparent Power L3 [VA]
              0, 0,                     #AC Reactive Power [VAr]
              0, 0,                     #AC Reactive Power L1 [VAr]
              0, 0,                     #AC Reactive Power L2 [VAr]
              0, 0,                     #AC Reactive Power L3 [VAr]
              0, 0,                     #AC power factor total [cosphi]
              0, 0,                     #AC power factor L1 [cosphi]
              0, 0,                     #AC power factor L2 [cosphi]
              0, 0,                     #AC power factor L3 [cosphi]
              exp_int1, exp_int2,       #Total Watt Hours Exportet [Wh]
              exp1_int1, exp1_int2,     #Watt Hours Exported L1 [Wh]
              exp2_int1, exp2_int2,     #Watt Hours Exported L2 [Wh]
              exp3_int1, exp3_int2,     #Watt Hours Exported L3 [Wh]
              ti_int1, ti_int2,         #Total Watt Hours Imported [Wh]
              0, 0,                     #Watt Hours Imported L1 [Wh]
              0, 0,                     #Watt Hours Imported L2 [Wh]
              0, 0,                     #Watt Hours Imported L3 [Wh]
              0, 0,                     #Total VA hours Exported [VA]
              0, 0,                     #VA hours Exported L1 [VA]
              0, 0,                     #VA hours Exported L2 [VA]
              0, 0,                     #VA hours Exported L3 [VA]
              0, 0,                     #Total VAr hours imported [VAr]
              0, 0,                     #VA hours imported L1 [VAr]
              0, 0,                     #VA hours imported L2 [VAr]
              0, 0                      #VA hours imported L3 [VAr]
    ]
    #print(values)
    context.setValues(register, address, values)
    time.sleep(1)
    lock.release()


###############################################################
# Config and start Modbus TCP Server
###############################################################
def run_updating_server():
    """
    Starts a Modbus TCP server with predefined data blocks and registers.
    This function initializes a Modbus server context with specific data blocks
    and registers, sets up a repeated timer to update the registers periodically,
    and starts the server to listen for incoming Modbus TCP requests.
    The server uses a single slave context with the same data block for discrete
    inputs, coils, holding registers, and input registers.
    Data blocks include:
    - Manufacturer and device model information.
    - Serial number and Modbus TCP address.
    - Other predefined register values.
    The server listens on the port specified by the `MODBUS_PORT` variable.
    A repeated timer is used to call the `updating_writer` function every 2 seconds
    to update the register values dynamically.
    Note:
    - The function uses a threading lock to ensure thread safety during initialization.
    - The `RepeatedTimer` and `updating_writer` functions must be defined elsewhere in the code.
    Raises:
        Any exceptions related to Modbus server initialization or runtime errors.
    """
    global rt
    lock.acquire()
    modbus_tcp_address = int(240 + config_manager.config["modbus_tcp_address"])
    serial_number_increment = int(50 + config_manager.config["modbus_tcp_address"])
    logger.info("[MAIN] Modbus TCP Address: %s and serial number fragment: %s",
                modbus_tcp_address, serial_number_increment
            )
    if modbus_tcp_address > 254:
        logger.error("[MAIN] Error: Modbus TCP Address is out of range. Too much Smart Meters")
        os._exit(1)  # Forcefully exit the whole application
    datablock = ModbusSparseDataBlock({

        40001:  [21365, 28243],
        40003:  [1],
        40004:  [65],
        40005:  [70,114,111,110,105,117,115,0,0,0,0,0,0,0,0,0,         #Manufacturer "Fronius
                83,109,97,114,116,32,77,101,116,101,114,32,54,51,65,0, #Device Model "Smart Meter
                0,0,0,0,0,0,0,0,                                       #Options N/A
                0,0,0,0,0,0,0,0,                                       #Software Version  N/A
                #Serial Number: 00000 (should be different if there are more Smart Meters)
                48,48,48,48,48,48,48,serial_number_increment,0,0,0,0,0,0,0,0,
                modbus_tcp_address],                                   #Modbus TCP Address:
        40070: [213],
        40071: [124],
        40072: [0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0],

        40196: [65535, 0],
    })

    slave_store = ModbusSlaveContext(
            di=datablock,
            co=datablock,
            hr=datablock,
            ir=datablock,
        )

    a_context = ModbusServerContext(slaves=slave_store, single=True)

    lock.release()

    ###############################################################
    # Run Update Register every 2 Seconds
    ###############################################################
    repetition_time = 2  # 2 seconds delay
    rt = RepeatedTimer(repetition_time, updating_writer, a_context)

    logger.info("[MAIN] start server, listening on %s", MODBUS_PORT)
    address = ("", MODBUS_PORT)
    try:
        StartTcpServer(
                context=a_context,
                address=address,
                framer=ModbusSocketFramer
                # TBD handler=None,  # handler for each session
                # allow_reuse_address=True,  # allow the reuse of an address
                # ignore_missing_slaves=True,  # ignore request to a missing slave
                # broadcast_enable=False,  # treat unit_id 0 as broadcast address,
                # TBD timeout=1,  # waiting time for request to complete
                # TBD strict=True,  # use strict timing, t1.5 for Modbus RTU
                # defer_start=False,  # Only define server do not activate
            )
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        signal_handler(None, None)

def signal_handler(sig, frame):
    """
    Handles the termination signal (e.g., Ctrl+C) to clean up resources.
    """
    global rt
    logger.info("[MAIN] Stopping server...")
    if rt:
        rt.stop()  # Stop the RepeatedTimer
    sys.exit(0)

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Main function
if __name__ == "__main__":
    try:
        tz = os.environ['TZ']
        logger.info("[MAIN] host system time zone is %s", tz)
    except KeyError:
        logger.info(
            "[MAIN] host system time zone was not set. Setting to %s",
            config_manager.config['time_zone']
        )
        os.environ['TZ'] = config_manager.config['time_zone']

    run_updating_server()
