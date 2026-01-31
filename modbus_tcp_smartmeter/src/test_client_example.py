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
import struct


def main():
    """Main function to run the Modbus TCP test client."""
    # Server connection details
    host = "localhost"
    # host = "192.168.1.135"
    # host = "192.168.1.125"
    port = 502
    unit_id = 0  # Use 0 for single context mode (matches pymodbus server default)

    print(f"Connecting to Modbus server at {host}:{port}, unit {unit_id}")

    client = ModbusTcpClient(host=host, port=port)

    try:
        if not client.connect():
            print("Failed to connect to server")
            return

        print("Connected successfully!")

        # Read from the actual address where the server writes (offset 40072)
        print("\nReading Holding Registers at offset 40072 (register 80073)")
        address = 40071
        count = 70  # Read a block to see all values written by the server
        result = client.read_holding_registers(
            address=address, count=count, slave=unit_id
        )
        if result.isError():
            print(f"Error: {result}")
        else:
            print(f"Registers 40072-40141: {result.registers}")

            # Example extraction: decode several floats from the block
            def decode_float(regs, idx, label=None):
                if idx + 1 >= len(regs):
                    return None
                int1 = regs[idx]
                int2 = regs[idx + 1]
                hex1 = f"{int1:04x}"
                hex2 = f"{int2:04x}"
                value_hex = "0x" + hex1 + hex2
                try:
                    as_int = int(value_hex, 16)
                    val = struct.unpack("<f", as_int.to_bytes(4, "little"))[0]
                except Exception:
                    val = None
                if label:
                    print(
                        f"{label} registers [{idx}, {idx+1}]: [{int1}, {int2}] hex: {value_hex} decoded: {val}"
                    )
                return val

            # Print all register pairs and their decoded float values for mapping
            print("\n--- Register Pair Scan (first 60 registers) ---")
            for idx in range(0, 120, 2):
                int1 = result.registers[idx] if idx < len(result.registers) else None
                int2 = (
                    result.registers[idx + 1]
                    if idx + 1 < len(result.registers)
                    else None
                )
                if int1 is None or int2 is None:
                    continue
                hex1 = f"{int1:04x}"
                hex2 = f"{int2:04x}"
                value_hex = "0x" + hex1 + hex2
                try:
                    as_int = int(value_hex, 16)
                    val = struct.unpack("<f", as_int.to_bytes(4, "little"))[0]
                except Exception:
                    val = None
                print(
                    f"Registers [{idx}, {idx+1}]: [{int1}, {int2}] hex: {value_hex} decoded: {val}"
                )
            print("--- End Register Pair Scan ---\n")

            # Use correct indices as per server's register mapping
            try:
                # Indices for the main values in the block from server (starting at 40072)
                current_total_idx = 0  # Total current
                current_l1_idx = 2  # L1 current
                current_l2_idx = 4  # L2 current
                current_l3_idx = 6  # L3 current
                voltage_avg_idx = 8  # Average voltage
                voltage_l1_idx = 10  # L1 voltage
                voltage_l2_idx = 12  # L2 voltage
                voltage_l3_idx = 14  # L3 voltage
                freq_idx = 24  # Frequency
                power_total_idx = 26  # Total power
                energy_exported_idx = 62  # Total Watt Hours Exported [Wh]
                energy_exported_l1_idx = 64  # Total Watt Hours Exported [Wh]
                energy_exported_l2_idx = 66  # Total Watt Hours Exported [Wh]
                energy_exported_l3_idx = 68  # Total Watt Hours Exported [Wh]
                energy_imported_idx = 70  # Total Watt Hours Imported [Wh]

                current_total = decode_float(
                    result.registers, current_total_idx, label="Current Total (A)"
                )
                current_l1 = decode_float(
                    result.registers, current_l1_idx, label="Current L1 (A)"
                )
                current_l2 = decode_float(
                    result.registers, current_l2_idx, label="Current L2 (A)"
                )
                current_l3 = decode_float(
                    result.registers, current_l3_idx, label="Current L3 (A)"
                )
                voltage_avg = decode_float(
                    result.registers, voltage_avg_idx, label="Voltage Avg (V)"
                )
                voltage_l1 = decode_float(
                    result.registers, voltage_l1_idx, label="Voltage L1 (V)"
                )
                voltage_l2 = decode_float(
                    result.registers, voltage_l2_idx, label="Voltage L2 (V)"
                )
                voltage_l3 = decode_float(
                    result.registers, voltage_l3_idx, label="Voltage L3 (V)"
                )
                frequency = decode_float(
                    result.registers, freq_idx, label="Frequency (Hz)"
                )
                power_total = decode_float(
                    result.registers, power_total_idx, label="Power Total (W)"
                )
                energy_exported = decode_float(
                    result.registers, energy_exported_idx, label="Energy Exported (Wh)"
                )
                energy_exported_l1 = decode_float(
                    result.registers,
                    energy_exported_l1_idx,
                    label="Energy Exported L1 (Wh)",
                )
                energy_exported_l2 = decode_float(
                    result.registers,
                    energy_exported_l2_idx,
                    label="Energy Exported L2 (Wh)",
                )
                energy_exported_l3 = decode_float(
                    result.registers,
                    energy_exported_l3_idx,
                    label="Energy Exported L3 (Wh)",
                )
                energy_imported = decode_float(
                    result.registers, energy_imported_idx, label="Energy Imported (Wh)"
                )

                print(f"Decoded values:")
                print(f"--Current Total (A): {current_total}")
                print(f"  Current L1 (A): {current_l1}")
                print(f"  Current L2 (A): {current_l2}")
                print(f"  Current L3 (A): {current_l3}")
                print(f"--Voltage Avg (V): {voltage_avg}")
                print(f"  Voltage L1 (V): {voltage_l1}")
                print(f"  Voltage L2 (V): {voltage_l2}")
                print(f"  Voltage L3 (V): {voltage_l3}")
                print(f"--Frequency (Hz): {frequency}")
                print(f"--Power Total (W): {power_total}")
                print(f"--Energy Exported (Wh): {energy_exported}")
                print(f"  Energy Exported L1 (Wh): {energy_exported_l1}")
                print(f"  Energy Exported L2 (Wh): {energy_exported_l2}")
                print(f"  Energy Exported L3 (Wh): {energy_exported_l3}")
                print(f"--Energy Imported (Wh): {energy_imported}")
            except Exception as e:
                print(f"Error decoding values: {e}")

    except ModbusException as me:
        print(f"Modbus error: {me}")
    except (ConnectionError, ValueError, TypeError, OSError) as e:
        print(f"Unexpected error: {e}")

    finally:
        client.close()
        print("\nDisconnected from server")


if __name__ == "__main__":
    main()
