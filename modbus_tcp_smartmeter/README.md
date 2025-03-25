
Table of content
- [modbus tcp smartmeter](#modbus-tcp-smartmeter)
  - [features](#features)
  - [configuration](#configuration)
    - [Configuration Parameters](#configuration-parameters)
    - [Home Assistant Add-on Configuration](#home-assistant-add-on-configuration)
    - [Local Usage](#local-usage)
  - [installing locally as system service](#installing-locally-as-system-service)
  - [Further information](#further-information)

# modbus tcp smartmeter

![Modbus TCP Smartmeter Icon](icon.png) 

Simulates a Fronius Smart Meter for providing necessary information to inverters (e.g. Gen24).

## features

- **Fronius Smart Meter Simulation**: Simulates a Fronius Smart Meter to provide necessary data for inverters like Gen24.
- **Modbus TCP Server**: Implements a Modbus TCP server to serve data to connected clients.
- **Dynamic Data Updates**: Periodically updates Modbus registers with real-time data from OpenHAB.
- **OpenHAB Integration**: Fetches data from OpenHAB REST API for parameters like energy, voltage, current, power, and frequency.
- **Selected Phase Support**: Supports specific single-phase configurations (L1, L2, L3).
- **Customizable Configuration**: Allows configuration of parameters like `loglevel`, `openhab_host`, `connected_phase`, and more via Home Assistant Add-on or local `config.yaml`.
- **Thread-Safe Updates**: Ensures thread safety while updating Modbus registers using a global lock.
- **System Time Zone Handling**: Automatically sets the time zone for accurate logging.
- **Graceful Shutdown**: Handles termination signals (e.g., Ctrl+C) to stop the server and clean up resources.
- **System Service Support**: Can be installed and run as a system service for local usage.


## configuration

### Configuration Parameters

- **connected_phase** : Connected Phase of Single Phase Inverter - Specifies the phase the inverter is connected to. Use `1`, `2`, or `3` to represent phases L1, L2, or L3.
- **energy_counter_out** : OpenHAB Item Name of Inverter Energy Counter - Name of the OpenHAB item representing the inverter energy counter (e.g., `inverter_energy` or `smartmeter_energy`).
- **current_voltage** : OpenHAB Item Name of Inverter Current Grid Voltage - Name of the OpenHAB item representing the current grid voltage (e.g., `inverter_voltage` or `smartmeter_voltage`).
- **current_current** : OpenHAB Item Name of Inverter Current Grid Current - Name of the OpenHAB item representing the current grid current (e.g., `inverter_current` or `smartmeter_current`).
- **current_power** : OpenHAB Item Name of Inverter Current Grid Output Power - Name of the OpenHAB item representing the current grid output power (e.g., `inverter_power` or `smartmeter_power`).
- **openhab_host** : Your OpenHAB Host - Host IP or internal DNS of your OpenHAB instance where the current inverter data is available.
- **modbus_tcp_address** : Log Level - Defines the logging level for the add-on (e.g., debug, info, warning, error).
- **loglevel** : Log Level - Defines the logging level for the add-on (e.g., debug, info, warning, error).
- **time_zone** : Time Zone - Your local time zone to ensure the correct timestamp is used in logging.

### Home Assistant Add-on Configuration

The add-on can be configured directly through the Home Assistant Add-on configuration interface.

### Local Usage

Create a config.yaml in folder /src - and configure your settings

example config file 

```yaml
connected_phase: 2
energy_counter_out: inverter2_PV_E_total
current_voltage: inverter2_Grid_U
current_current: inverter2_Grid_I
current_power: inverter2_Grid_P
openhab_host: 192.168.1.31
modbus_tcp_address: 2
loglevel: debug
time_zone: Europe/Berlin
```

## installing locally as system service

Install required Python dependencies
```bash
pip install -r requirements.txt
```

installing as system service:

```bash
sudo chmod +x /your/path/to/modbus_tcp_smartmeter/src/modbus_tcp_smartmeter.py
```

create service file e.g. /home/pi/ModbusTCP_SmartMeter.service

```ini
[Unit]
Description=Modbus TCP Smart Meter Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /your/path/to/modbus_tcp_smartmeter/src/modbus_tcp_smartmeter.py
WorkingDirectory=/path/to/your/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```
then
```bash
sudo cp /home/pi/ModbusTCP_SmartMeter.service /etc/systemd/system/
sudo systemctl enable ModbusTCP_SmartMeter.service
sudo systemctl start ModbusTCP_SmartMeter.service
```

If you prefer not to run the script as root, you can use setcap to grant the necessary capabilities:

```bash
sudo setcap 'cap_net_bind_service=+ep' /usr/bin/python3
```

This setup will ensure your script runs automatically at startup with the necessary permissions.


## Further information

...