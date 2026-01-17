#!/usr/bin/env python3
"""
Example Modbus TCP test client for the Smart Meter simulator.

This script demonstrates how to connect to the Modbus TCP server and
read registers based on the debug logs generated when modbus_requests
debug mode is enabled.

Run this script while the server is running with debug mode enabled
to see the request patterns, then replicate them in your test client.
"""


import time
from pymodbus.client import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.exceptions import ModbusException


def main():
    """Main function to run the Modbus TCP test client."""
    # Server connection details
    host = "localhost"
    port = 502
    unit_id = 244  # Modbus TCP Address + 240 (from config)

    print(f"Connecting to Modbus server at {host}:{port}, unit {unit_id}")

    # Create client
    client = ModbusTcpClient(host=host, port=port)

    try:
        # Connect to server
        if not client.connect():
            print("Failed to connect to server")
            return

        print("Connected successfully!")

        # Example requests based on typical Smart Meter usage
        # These patterns were observed from debug logs

        # 1. Read Holding Registers - Device identification
        print("\n1. Reading device identification (Holding Registers 40001-40005)")
        result = client.read_holding_registers(address=40001, count=5, slave=unit_id)
        if result.isError():
            print(f"Error: {result}")
        else:
            print(f"Manufacturer/Model: {result.registers}")

        # 2. Read Input Registers - Live data (this is where energy/current/voltage are)
        print("\n2. Reading live meter data (Input Registers 40070-40072)")
        result = client.read_input_registers(address=40070, count=3, slave=unit_id)
        if result.isError():
            print(f"Error: {result}")
        else:
            # Decode the energy value (32-bit float, big-endian)
            decoder = BinaryPayloadDecoder.fromRegisters(
                result.registers, byteorder=Endian.Big, wordorder=Endian.Big
            )
            energy_wh = decoder.decode_32bit_float()
            print(".1f")

        # 3. Read more live data
        print("\n3. Reading additional live data")
        result = client.read_input_registers(address=40190, count=10, slave=unit_id)
        if not result.isError():
            print(f"Additional data: {result.registers}")

        # 4. Periodic reads (simulate what a real inverter would do)
        print("\n4. Starting periodic reads (every 2 seconds for 10 seconds)")
        for i in range(5):
            result = client.read_input_registers(address=40070, count=3, slave=unit_id)
            if not result.isError():
                decoder = BinaryPayloadDecoder.fromRegisters(
                    result.registers, byteorder=Endian.Big, wordorder=Endian.Big
                )
                energy_wh = decoder.decode_32bit_float()
                print(".1f")
            time.sleep(2)

    except ModbusException as me:
        print(f"Modbus error: {me}")
    except (ConnectionError, ValueError, TypeError, OSError) as e:
        print(f"Unexpected error: {e}")

    finally:
        client.close()
        print("\nDisconnected from server")


if __name__ == "__main__":
    main()
