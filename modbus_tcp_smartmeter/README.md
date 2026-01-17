# Modbus TCP Smart Meter

![Modbus TCP Smartmeter Icon](icon.png)

**Simulates a smart meter via Modbus TCP to provide real-time energy data to inverters and other devices.**

This addon creates a Modbus TCP server that emulates a smart meter, fetching live data from OpenHAB or Home Assistant and serving it to connected clients like solar inverters (e.g., Fronius Gen24). Perfect for integrating energy monitoring systems where direct smart meter connection isn't available.

## Table of Contents
- [Quick Start](#quick-start)
- [Features](#features)
- [Configuration](#configuration)
- [Installation](#installation)
- [Contributing](#contributing)
- [Support](#support)

## Quick Start

### Home Assistant Add-on Installation
1. Add this repository to your Home Assistant Add-on Store: `https://github.com/ohAnd/ha_addons`
2. Install the "Modbus TCP Smart Meter" addon
3. Configure your data source (OpenHAB or Home Assistant) and item names
4. Start the addon
5. Connect your inverter to the addon's IP on port 502

### Local Installation
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `src/config.yaml` and configure your settings
4. Run: `python3 src/modbus_tcp_smartmeter.py`

## Features

### Core Functionality
- **Smart Meter Emulation**: Full Modbus TCP server implementing smart meter registers
- **Real-time Data**: Continuously updates with live energy data from your home automation system
- **Multi-Source Support**: Compatible with both OpenHAB and Home Assistant
- **Phase-Specific Data**: Supports single-phase configurations (L1, L2, L3)

### Data Types Supported
- **Energy Counter**: Cumulative energy production/consumption
- **Live Measurements**:
  - Grid voltage
  - Grid current
  - Grid power
  - Grid frequency (optional)

### Advanced Features
- **Thread-Safe Operations**: Concurrent data updates with proper locking
- **Configurable Thresholds**: Filter invalid low-energy readings
- **Timezone Handling**: Automatic timezone detection with fallback configuration
- **Debug Logging**: Detailed Modbus request logging for development
- **Graceful Shutdown**: Proper cleanup on termination signals
- **System Service Support**: Can run as a systemd service for production use

### Technical Specifications
- **Protocol**: Modbus TCP
- **Port**: 502 (configurable via Docker/host networking)
- **Unit ID**: Configurable 0-15
- **Register Map**: Compatible with Fronius smart meter specifications
- **Update Interval**: 2-second data refresh cycle

## Configuration

### Configuration Overview

The addon supports two primary configuration methods:
- **Home Assistant Add-on**: Configure through the HA UI
- **Local Config File**: Use `src/config.yaml` for standalone operation

### Data Source Configuration

Choose between OpenHAB or Home Assistant as your data source:

#### OpenHAB Setup
```yaml
data:
  source: openhab
  host: 192.168.1.31  # Your OpenHAB instance IP
  access_token: ""    # Not required for OpenHAB
```

#### Home Assistant Setup
```yaml
data:
  source: homeassistant
  host: 192.168.1.31              # Your HA instance IP
  access_token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."  # Long-lived access token
```

### Modbus Configuration

```yaml
modbus:
  modbus_tcp_address: 2    # Unit ID (0-15)
  connected_phase: 2       # Phase: 1=L1, 2=L2, 3=L3
```

### Energy Data Configuration

```yaml
smartmeter_energy:
  energy_counter_out: sensor.pv_energy_total  # Item/entity name for cumulative energy
  min_energy_threshold: 0.1                   # Minimum valid energy value in kWh
```

### Live Data Configuration

```yaml
smartmeter_livedata:
  current_voltage: sensor.grid_voltage     # Grid voltage sensor
  current_current: sensor.grid_current     # Grid current sensor
  current_power: sensor.grid_power         # Grid power sensor
  current_frequency: sensor.grid_frequency # Grid frequency sensor (optional)
```

### General Settings

```yaml
general:
  loglevel: debug          # Logging level: debug, info, warning, error
  time_zone: Europe/Berlin # Timezone for logging timestamps
```

### Debug Settings

```yaml
debug:
  modbus_requests: false   # Enable detailed Modbus request logging
```

### Configuration Parameters Reference

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `data.source` | Yes | openhab | Data source: `openhab` or `homeassistant` |
| `data.host` | Yes | 192.168.1.99 | IP address of your home automation system |
| `data.access_token` | No | "" | HA long-lived access token (HA only) |
| `modbus.modbus_tcp_address` | Yes | 0 | Modbus unit ID (0-15) |
| `modbus.connected_phase` | Yes | 1 | Connected phase (1-3) |
| `smartmeter_energy.energy_counter_out` | Yes | inverter_energy | Energy counter item/entity name |
| `smartmeter_energy.min_energy_threshold` | Yes | 0.1 | Minimum valid energy value in kWh |
| `smartmeter_livedata.current_voltage` | Yes | inverter_voltage | Voltage item/entity name |
| `smartmeter_livedata.current_current` | Yes | inverter_current | Current item/entity name |
| `smartmeter_livedata.current_power` | Yes | inverter_power | Power item/entity name |
| `smartmeter_livedata.current_frequency` | No | "" | Frequency item/entity name |
| `general.loglevel` | Yes | debug | Logging level |
| `general.time_zone` | Yes | UTC | Timezone for logging |
| `debug.modbus_requests` | No | false | Enable Modbus request logging |

## Installation

### Home Assistant Add-on

1. In Home Assistant, go to **Settings > Add-ons > Add-on Store**
2. Click the menu (⋮) and select **Repositories**
3. Add repository: `https://github.com/ohAnd/ha_addons`
4. Find and install "Modbus TCP Smart Meter"
5. Configure the addon options
6. Start the addon

### Local Installation

#### Prerequisites
- Python 3.8+
- Access to OpenHAB or Home Assistant instance

#### Setup Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ohAnd/ha_addons.git
   cd ha_addons/modbus_tcp_smartmeter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure:**
   ```bash
   cp src/config.yaml.example src/config.yaml
   # Edit src/config.yaml with your settings
   ```

4. **Run:**
   ```bash
   python3 src/modbus_tcp_smartmeter.py
   ```

#### System Service Installation

To run as a system service:

1. **Make executable:**
   ```bash
   chmod +x src/modbus_tcp_smartmeter.py
   ```

2. **Create service file** (`/etc/systemd/system/modbus-tcp-smartmeter.service`):
   ```ini
   [Unit]
   Description=Modbus TCP Smart Meter Service
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /path/to/modbus_tcp_smartmeter/src/modbus_tcp_smartmeter.py
   WorkingDirectory=/path/to/modbus_tcp_smartmeter
   StandardOutput=inherit
   StandardError=inherit
   Restart=always
   User=your-user

   [Install]
   WantedBy=multi-user.target
   ```

3. **Enable and start:**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable modbus-tcp-smartmeter
   sudo systemctl start modbus-tcp-smartmeter
   ```

#### Docker Installation

```bash
docker run -d \
  --name modbus-tcp-smartmeter \
  --network host \
  -v /path/to/config:/app/config.yaml \
  ghcr.io/ohand/ha-addon-modbus_tcp_smartmeter
```

## Contributing

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for details.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Testing
- Use `test_client_example.py` to test Modbus connectivity
- Enable `debug.modbus_requests` for detailed logging
- Test with both OpenHAB and Home Assistant sources

## Support

### Issues
- Check existing [GitHub Issues](https://github.com/ohAnd/ha_addons/issues)
- Provide detailed logs and configuration (redact sensitive data)

### Sponsoring
If you find this project helpful, consider [sponsoring development](https://github.com/sponsors/ohAnd) to support continued maintenance and feature development.

---

**Disclaimer**: This software is provided as-is. Use at your own risk. Ensure proper electrical safety measures when working with energy systems.