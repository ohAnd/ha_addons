**Version 1.0.3** published on 31.01.2026
- fixing precise of provided values

**Version 1.0.2** published on 28.01.2026
- fixing exported energy calculations in modbus_server

**Version 1.0.1** published on 17.01.2026
- fixing startup behavior

**Version 1.0.0** published on 17.01.2026
- Major refactor: improved data abstraction and error handling for unavailable or invalid energy data
- Exception handling for unreachable OpenHAB host
- Logging now supports timezone and is configurable via config.yaml
- Configuration is managed by a new ConfigManager class; config.yaml structure is now strictly enforced
- If config.yaml is missing, a default is created and server restart is required
- Home Assistant is now supported as a data source (in addition to OpenHAB)
- Energy data updates now run in a background thread for real-time accuracy
- Modbus register updates are more robust and thread-safe
- Signal handling for graceful shutdown (Ctrl+C)
- Improved docstrings and comments for maintainability
- BREAKING CHANGE: config.yaml must be updated to the new structure; old configs may not be compatible
- Existing parameters (modbus address, connected phase, etc.) are now strictly required and validated
- Phase selection for power/current data is now more robust

**Version 0.0.11** published on 06.05.2025
- fix: wrong last data for energy_data
- 
**Version 0.0.10** published on 06.05.2025
- fix: move energy_data initialization to main function with timeout check for energy value retrieval

**Version 0.0.9** published on 05.05.2025
- fix: handle invalid energy values - using the last known

**Version 0.0.8** published on 02.05.2025
- rework for a more abstracted data receiving to be more stable if incoming data are not available for a certain time

**Version 0.0.7-fix1** published on 04.04.2025
- adapt config.yaml for unneeded entry
 
**Version 0.0.7** published on 25.03.2025
- add exception handling for openHAB host not reachable
- updating doc
  
**Version 0.0.6** published on 25.03.2025
- new config param for modbus address
  
**Version 0.0.5** published on 25.03.2025
- implement timezone handling for logger output
 
**Version 0.0.4** published on 24.03.2025
- rework with detailed config 
- improved error handling
  
**Version 0.0.3** published on 22.03.2025
- changed power, current data from phase 1 to phase 2

**Version 0.0.2** published on 09.02.2025
- first runnable release

**Version 0.0.1** published on 04.02.2025
- inital start