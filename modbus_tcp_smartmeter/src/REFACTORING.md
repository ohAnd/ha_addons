# Modbus TCP Smart Meter - Refactored Structure

## Overview
The code has been refactored into separate modules for better maintainability, testability, and clarity.

## Module Structure

```
src/
├── __init__.py                    # Package initialization
├── modbus_tcp_smartmeter.py       # Main entry point and orchestration (149 lines)
├── config_manager.py              # Configuration management (99 lines)
├── energy_data.py                 # Energy data retrieval (344 lines)
├── modbus_server.py               # Modbus server lifecycle (397 lines)
└── config.yaml                    # Configuration file
```

**Total: ~1000 lines** (reduced from 1288 lines monolithic file)

## Module Responsibilities

### `config_manager.py`
- **Purpose**: Configuration loading, validation, and persistence
- **Key Class**: `ConfigManager`
- **Functions**:
  - Load configuration from `config.yaml`
  - Merge with defaults
  - Save configuration
- **Dependencies**: `os`, `yaml`

### `energy_data.py`
- **Purpose**: Fetch and manage energy-related data
- **Key Class**: `EnergyData`
- **Functions**:
  - Fetch data from OpenHAB or Home Assistant
  - Background update service (2-second interval)
  - Energy threshold validation
  - API abstraction for both data sources
- **Dependencies**: `logging`, `threading`, `time`, `requests`

### `modbus_server.py`
- **Purpose**: Modbus TCP server lifecycle and register updates
- **Key Components**:
  - `build_modbus_context()`: Initialize Modbus registers
  - `start_modbus_services()`: Start server and update timer
  - `stop_modbus_services()`: Graceful shutdown
  - `stop_and_wait_for_valid()`: Handle energy threshold violations
  - `updating_writer()`: Update registers every 2 seconds
  - `RepeatedTimer`: Timer helper class
- **Dependencies**: `logging`, `os`, `struct`, `threading`, `time`, `pymodbus`

### `modbus_tcp_smartmeter.py`
- **Purpose**: Main entry point and application orchestration
- **Key Functions**:
  - Initialize all components
  - Wait for valid energy before starting server
  - Signal handling (Ctrl+C)
  - Main event loop
- **Dependencies**: All other modules

## Data Flow

```
1. Startup:
   main() → ConfigManager() → EnergyData() → Wait for valid energy → build_modbus_context() → start_modbus_services()

2. Runtime (every 2 seconds):
   RepeatedTimer → updating_writer() → EnergyData.get_*_value() → Update Modbus registers

3. Threshold Violation:
   EnergyData.__update_item() → stop_callback → stop_and_wait_for_valid() → Set waiting_for_valid flag
   updating_writer() detects flag → Wait for energy recovery → Restart server

4. Shutdown:
   Ctrl+C → signal_handler() → stop_modbus_services() → energy_data.shutdown() → Exit
```

## Key Design Improvements

### 1. **Separation of Concerns**
- Configuration logic isolated from business logic
- Energy data retrieval separated from Modbus serving
- Server lifecycle management in dedicated module

### 2. **Reduced Coupling**
- Modules communicate through well-defined interfaces
- Dependency injection for `EnergyData` (config_manager, stop_callback)
- Function parameters instead of global state where possible

### 3. **Improved Testability**
- Each module can be tested independently
- Clear boundaries for unit testing
- Mock-friendly design (callbacks, injected dependencies)

### 4. **Better Error Handling**
- Energy threshold violations handled gracefully
- Server can stop/wait/restart without process exit
- Background threads properly managed

### 5. **State Management**
- `waiting_for_valid` flag prevents restart loops
- Global state minimized and clearly documented
- Thread-safe operations with locks

## Configuration

All configuration remains in `config.yaml` with the same nested structure:
```yaml
data:
  source: openhab | homeassistant
  host: IP address
  access_token: (for Home Assistant)

modbus:
  modbus_tcp_address: 0-15
  connected_phase: 1-3

smartmeter_energy:
  energy_counter_out: item/entity name
  min_energy_threshold: kWh

smartmeter_livedata:
  current_voltage: item/entity name
  current_current: item/entity name
  current_power: item/entity name
  current_frequency: item/entity name

general:
  loglevel: debug | info | warning | error
  time_zone: UTC | Europe/Berlin | etc
```

## Running the Application

```bash
cd src/
python modbus_tcp_smartmeter.py
```

## Future Enhancements

Potential improvements now easier due to modular structure:

1. **Testing**: Add unit tests for each module
2. **API Abstraction**: Create abstract base class for data sources
3. **Plugin System**: Support additional data sources (MQTT, InfluxDB, etc.)
4. **Configuration Validation**: Use schema validation (e.g., Pydantic)
5. **Async Support**: Convert to async/await for better performance
6. **Metrics**: Add Prometheus metrics endpoint
7. **Docker**: Easier containerization with clear module boundaries

## Migration Notes

- **Backward Compatible**: Uses same `config.yaml` format
- **No Behavior Changes**: Identical runtime behavior
- **Backup Available**: Original file saved as `modbus_tcp_smartmeter.py.bak`
