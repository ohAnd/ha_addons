"""
Configuration management for Modbus TCP Smart Meter.

This module handles loading, updating, and saving configuration settings
from a config.yaml file with nested structure.
"""

import os
import yaml


class ConfigManager:
    """
    Manages the configuration settings for the application.

    This class handles loading, updating, and saving configuration settings from a 'config.yaml'
    file. If the configuration file does not exist, it creates one with default values and
    prompts the user to restart the server.
    """

    def __init__(self):
        self.config_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "config.yaml"
        )
        self.default_config = {
            "data": {
                "source": "openhab",
                "host": "192.168.1.99",
                "access_token": "",
            },
            "modbus": {
                "modbus_tcp_address": 0,
                "connected_phase": 1,
            },
            "smartmeter_energy": {
                "energy_counter_out": "inverter_energy",
                "min_energy_threshold": 0.1,
            },
            "smartmeter_livedata": {
                "current_voltage": "inverter_voltage",
                "current_current": "inverter_current",
                "current_power": "inverter_power",
                "current_frequency": "",
            },
            "general": {
                "loglevel": "debug",
                "time_zone": "UTC",
            },
        }
        self.config = self._deep_copy_config(self.default_config)
        self.load_config()

    def _deep_copy_config(self, config):
        """Deep copy nested config dictionary."""
        return {
            key: dict(val) if isinstance(val, dict) else val
            for key, val in config.items()
        }

    def load_config(self):
        """
        Reads the configuration from 'config.yaml' file located in the current directory.
        If the file exists, it loads and merges with defaults.
        If the file does not exist, creates one with default values.
        """
        if os.path.exists(self.config_file):
            with open(self.config_file, "r", encoding="utf-8") as f:
                loaded_config = yaml.safe_load(f)
                if loaded_config:
                    self._merge_config(loaded_config)
        else:
            print("ERROR - Config file not found. [config.yaml]")
            print("Creating a new config file with default values...")
            self.save_config()
            print(
                "Please configure the settings in the 'config.yaml' file and restart the server."
            )
            exit(1)

    def _merge_config(self, loaded_config):
        """Merge loaded configuration with defaults (nested)."""
        for key, value in loaded_config.items():
            if key in self.config and isinstance(value, dict):
                self.config[key].update(value)
            else:
                self.config[key] = value

    def save_config(self):
        """Saves the current configuration to the config file."""
        with open(self.config_file, "w", encoding="utf-8") as f:
            yaml.dump(self.config, f, default_flow_style=False)
