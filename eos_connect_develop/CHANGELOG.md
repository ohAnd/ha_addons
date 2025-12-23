**Version 0.2.29.215** published on 2025-12-23
- feat: remove experimental banner for optimization source 'evopt' in controls manager
- feat: adjust canvas size and stroke color for charging data patterns in battery chart
- feat: implement auto-detection of battery power convention and enhance historical data fetching - touches calculating price for stored energy in battery and using dynamically for optimization touches [#185](https://github.com/ohAnd/EOS_connect/issues/185)

**Version 0.2.29.214** published on 2025-12-22
- Feature: implement dynamic battery price calculation and update configuration settings - adds comprehensive battery price analysis and overview features
- Feature: enhance battery overview UI for better mobile responsiveness and readability
- Feature: enhance battery price calculation by adjusting gap tolerances and improving event handling
- Feature: implement inventory valuation for dynamic battery price calculation and enhance UI for better clarity
- Fix: correct import statement for BatteryPriceHandler in battery_interface.py
- Feat: add sanitization step for Docker tag reference name in workflow
- Feat: enhance battery overview to reflect dynamic price calculation status and improve UI responsiveness
Closes [#186](https://github.com/ohAnd/EOS_connect/pull/186)

**Version 0.2.29.213** published on 2025-12-20
- Feature: add dynamic battery energy price from Home-Assistant/OpenHAB - adds support for price_euro_per_wh_sensor to dynamically fetch battery price
Closes [#172](https://github.com/ohAnd/EOS_connect/pull/172)
- Refactor: update battery price configuration and unify data fetching methods
- Add defensive handling for price of stored energy in EVOptBackend

**Version 0.2.29.209** published on 2025-12-20
- Refactor charge demand calculations in BaseControl to use optimization_max_charge_power_w for consistent value conversion - fixes evopt lädt zu wenig/langsam
Fixes [#167](https://github.com/ohAnd/EOS_connect/issues/167)
- Enhance clipboard functionality in BugReportManager for improved iOS compatibility and user experience - fixes Copy to clipboard funktioniert nicht
Fixes [#180](https://github.com/ohAnd/EOS_connect/issues/180)
- Enhance error handling in EVOptBackend for response validation and initial SOC clamping
- Improve error handling in OptimizationScheduler and PvInterface for robustness against None values and API errors - closes [#178](https://github.com/ohAnd/EOS_connect/issues/178) [FIX] catch more exceptions in main loop

**Version 0.2.29.208** published on 2025-12-15
- Enhance discharge state handling by introducing effective discharge logic and updating related MQTT topics to reflect final states after overrides - fixes Missing State in HA for Allow Discharge EVCC
Fixes [#175](https://github.com/ohAnd/EOS_connect/issues/175)
- Implement dynamic max charge power based on charging curve configuration in get_pv_akku_data function - fixes part 2 of evopt lädt zu wenig/langsam
Fixes [#167](https://github.com/ohAnd/EOS_connect/issues/167)

**Version 0.2.29.207** published on 2025-12-14
- Fix AC charge power calculation during override in get_current_ac_charge_demand method - fixes Override Charge funktioniert nicht mehr unter EOS Connect develop
Fixes [#173](https://github.com/ohAnd/EOS_connect/issues/173)

**Version 0.2.29.202** published on 2025-12-07
- Add charge rate limiting for AC and DC in change_control_state function - fixes Max grid charge rate wrong calculation
Fixes [#171](https://github.com/ohAnd/EOS_connect/issues/171)

**Version 0.2.29.198** published on 2025-12-02
- Limit AC charge power to the maximum battery charge capacity in get_current_ac_charge_demand()
- Add battery charge max settings to AC charge demand tests for accurate power simulation - touches [#167](https://github.com/ohAnd/EOS_connect/issues/167)

**Version 0.2.29.196** published on 2025-11-30
- Refactor AC charge demand handling to use get_needed_ac_charge_power() for MQTT updates and add comprehensive tests for AC charge demand conversion - fixes evopt lädt zu wenig/langsam
Fixes [#167](https://github.com/ohAnd/EOS_connect/issues/167)

**Version 0.2.28.194** published on 2025-11-22
- Refactor FroniusWRV2 inverter data fetching to improve error handling and add unit tests for monitoring functionality

**Version 0.2.28.193** published on 2025-11-16
- Refactor EOS version handling and add unit tests for EOSBackend class - fixes 422 Client Error: Unprocessable Entity for url: http://eos:8503/optimize?start_hour=9 Fixes [#158](https://github.com/ohAnd/EOS_connect/issues/158)
- Refactor temperature forecast handling in PvInterface to use default values and clean up commented code - fixes [#154](https://github.com/ohAnd/EOS_connect/issues/154) - PV Forecats from evcc but I get [PV-IF] Akkudoktor API error for temperature: HTTPSConnectionPool

**Version 0.2.28.192** published on 2025-11-16
- Update port configuration logic to default to 8081 in HA addon mode
- Fix: Enable Docker port mapping by removing host_network mode
  - Removes host_network: true to allow port mapping configuration
  - Removes eos_connect_web_port from addon UI options (use ports: section instead)
  - Retains schema for backward compatibility with local installations
  - Fixes issue [#144](https://github.com/ohAnd/EOS_connect/issues/144): 404 in home assistant UI

**Version 0.2.28.191** published on 2025-11-15
- Add fallback for avg_runtime and error handling in calculate_next_run_time method
- Update discharge_allowed mapping to convert values to binary representation
- HA addon specific - fixed external port config for addon - fixes https://github.com/ohAnd/EOS_connect/issues/144

**Version 0.2.28.190** published on 2025-11-12
- Refactor chart data processing to ensure consistent use of server timestamp for current slot calculations
- Adjust update interval logic for Solcast based on configuration length - fixes Solcast, rate limit exceeded Fixes [#151](https://github.com/ohAnd/EOS_connect/issues/151)
- Enhance load profile calculation to handle cases with zero values, ensuring accurate averaging and data integrity - fix load profile at 50% if two weeks before have no historical data Fixes [#156](https://github.com/ohAnd/EOS_connect/issues/156)

**Version 0.2.28.189** published on 2025-11-12
- Refactor battery price calculation to remove unnecessary division and update schedule manager to use hourly sums for AC charge transformation

**Version 0.2.28.188** published on 2025-11-11
- HA addon specific - added port config for addon - fixes https://github.com/ohAnd/EOS_connect/issues/144
- Enhance EVOpt response handling with detailed array length specifications and improved processing logic for control and result arrays. Update methods to ensure correct sizing and padding based on time frame, and extract battery parameters more robustly.
- Fix AC charge value calculation for quarterly slots in ChartManager to ensure correct power distribution.
- Update PV Forecast Configuration section in CONFIG_README.md to clarify sources and parameters
- Increase retry parameters in PV forecast request to enhance error handling and data retrieval reliability.
- Fix lambda function in test_api_error_triggers_fallback to correctly handle additional arguments in retry request

**Version 0.2.28.186** published on 2025-11-09
- Update EOS version checks to include 0.2.0+dev for configuration handling
- Refactor control data handling in optimize method to use current step index instead of hour, improving accuracy for AC and DC charge demands and discharge allowance logging.

**Version 0.2.28.185** published on 2025-11-09
- Enhance time frame configuration with validation and fallback. Add type checking for time_frame and improve logging for invalid configurations.

**Version 0.2.28.184** published on 2025-11-09
- Refactor EVOptBackend to correct variable names for request and response handling, ensuring consistency in transformation methods and improving debug file outputs.
- Enhance ScheduleManager to transform ac_charge and discharge_allowed to hourly values, improving data accuracy for schedule display.
- Refactor ChartManager to improve label time calculation for hourly intervals and enhance discharge data handling based on time frame settings.
- Enhance showMainMenu and showInfoMenu to include backend and granularity parameters, improving information display for users.
- Enhance battery and schedule managers to support conversion of 15-min interval data to hourly averages, improving data accuracy and UI updates. Update setBatteryChargingData to accept data_controls for better handling of charging data.

**Version 0.2.28.183** published on 2025-11-08
- Enhance LoadInterface to extend energy calculation for incomplete intervals and update related tests for accurate load profile generation
- Enhance EVOptBackend to support dynamic time frame base for load and price series calculations, accommodating both hourly and 15-minute intervals.
- Enhance chart and statistics management to support dynamic time frame base for data processing, including 15-minute and hourly intervals, and update related calculations and display logic.
- Enhance configuration and documentation to support new time frame settings for optimization cycles, allowing 15-minute and hourly intervals. Update related logic in the ConfigManager and EOS connection handling. (currently only with EVopt as backend)

**Version 0.2.28.182** published on 2025-11-07
- Fix energy conversion calculation in PvInterface to correctly convert kW to Wh for 30-minute periods - fix Solcast forecast for yield way too high Fixes [#149](https://github.com/ohAnd/EOS_connect/issues/149)
- Enhance PvInterface to support dynamic time frame base for PV forecasts and adjust related tests
- Enhance PriceInterface to support dynamic time frame base for price retrieval and update related tests for hourly and 15-minute aggregations
- Enhance LoadInterface to support dynamic time frame base for load profile calculations and update related tests

**Version 0.2.28.181** published on 2025-11-02
- Refactor PvInterface configuration validation and enhance Solcast data handling in tests
- Update CONFIG_README and pv_interface.py for clarity on configuration parameters and source requirements - fix Solcast forecast for yield way too high Fixes [#149](https://github.com/ohAnd/EOS_connect/issues/149)

**Version 0.2.25.174** published on 2025-11-01
- bugreport - fix: show current version - refactor: clean up whitespace and improve readability in BugReportManager methods
- refactor: rename EVCCOptBackend to EVOptBackend and update related transformation methods
- refactor: adjust forecast calculations for EVopt source based on current time
- refactor: adjust background opacity of experimental banner in index.html

**Version 0.2.25.173** published on 2025-11-01
- fix: comment out debug logging for needed AC charge power calculation
- refactor: enhance MQTT control command handling and add SOC limit management incl. via MQTT
- refactor: update configuration for EOS and EVopt sources, including time frame base adjustments - breaking change in config evcc_opt -> evopt

**Version 0.2.25.172** published on 2025-10-31
- fix: enhance Docker workflows to support multi-platform builds and QEMU setup
- fix: update BaseControl to include time frame base and calculate needed AC charge power

**Version 0.2.25.171** published on 2025-10-30
- fix: update default azimuth, tilt, power, and inverter settings in PvInterface configuration for solcast, evcc
- fix: enhance EOS version handling and configuration validation for version 0.1.0+dev - incl. automatic config update if needed

**Version 0.2.25.170** published on 2025-10-30
- feat: enhance PV configuration handling with default values for azimuth and tilt, and improve horizon parameter checks - fix PV: All options seem to be required, despite not using akkudoktor Fixes [#135](https://github.com/ohAnd/EOS_connect/issues/135)
- fix: update references from EVCC Opt to EVopt across documentation and codebase
- Renaming EVCCOptBackend to EVOptBackend + fix grid charge calculation for fulfilling EOS api and get right target value

**Version 0.2.25.166** published on 2025-10-29
- EXPERIMENTAL: Evcc opt wrapper ([#138](https://github.com/ohAnd/EOS_connect/issues/138))
  - first working draft of second source for optimization - evcc opt
  - feat: update README and configuration for EOS server source and port settings - fixes eos intrerface tests
  - feat: update README and UI to support evcc optimization backend and display experimental mode banner
  - refactor: remove hardcoded base URL for EVCC optimization request
  - feat: Add OptimizationInterface for backend optimization management
    - Introduced OptimizationInterface class to serve as an abstraction layer for interacting with EOS and EVCC Opt optimization backends.
    - Implemented methods for optimization, control data examination, and scheduling management.
    - Added functionality to calculate the next optimal run time and retrieve EOS version from the backend.
    - Created unit tests for OptimizationInterface, covering backend selection, response handling, and error management.
    - Included a dummy backend for testing integration without actual backend dependencies.
    - refactor: remove obsolete test module for EosInterface scheduling algorithm

**Version 0.2.25.164** published on 2025-10-27
- feat: enhance historical data processing to include attributes and unit conversion for HA source - found by @WolfImBusch

**Version 0.2.25.163** published on 2025-10-27
- Add Strømligning.dk price provider ([#126](https://github.com/ohAnd/EOS_connect/issues/126)) - implements [#123](https://github.com/ohAnd/EOS_connect/issues/123) - thanks to @LordMike
  - feat: add Stromligning price provider
  - feat: extend stromligning price window by using their forecast API
  - Update price interface for stromligning as per discussion
  - Tweak the docs
  - Handle some pylint issues
- fix: [#122](https://github.com/ohAnd/EOS_connect/issues/122) set all evcc states to avoid discharge ([#134](https://github.com/ohAnd/EOS_connect/issues/134)) - fixes [#122](https://github.com/ohAnd/EOS_connect/issues/122)
  - fix: [#66](https://github.com/ohAnd/EOS_connect/issues/66) set all evcc states to avoid discharge
  - fix: enhance MQTT value and command templates for better state handling

**Version 0.2.25.158** published on 2025-10-27
- fix: remove currency symbol from in/out text display in schedule
- update EVCC charging modes in connection with EOS demands
- Introduced a new color constant for "Charge From Grid During E-Car Fast Charge" in `constants.js`.
- Updated the schedule display logic in `schedule.js` to include the new charging mode.
- Improved logging format in `pv_interface.py` for better readability.
- feat: add 'Charge from Grid EVCC FAST' option to MQTT command templates - touches Haus-Batterie wird nicht gesperrt, sofern evcc mode = "PV" und Ladeplan aktiv touches [#66](https://github.com/ohAnd/EOS_connect/issues/66)


**Version 0.2.25.153** published on 2025-10-25
- Implement currency symbols from price provider ([#129](https://github.com/ohAnd/EOS_connect/issues/129)) thanks to @LordMike
  - * feat: expose currency for chosen price provider such that ui sees it
  - * bugfix: currency ui symbol
  - * refactor localization for a centrilzed structure

**Version 0.2.25.151** published on 2025-10-25
- fix: enhance data validation by checking for 'unknown' state in energy data
- fix: add DST change detection and adjust EMS data retrieval accordingly - preperation for full EOS DST change capability - fixes Null values lead to crash Fixes [#130](https://github.com/ohAnd/EOS_connect/issues/130)
- fix: implement last control data tracking for optimized charging decisions - fixes Log file flooded with 'WARNING [Main] EOS requested AC charging (0.75) but battery SoC (100.0%) at/above maximum (100%) - overriding to 0' Fixes [#131](https://github.com/ohAnd/EOS_connect/issues/131)

**Version 0.2.25.145** published on 2025-10-20
- fix: update API version to 0.0.2 and enhance logging for EVCC charging state transitions
- fix: improve grid charge power handling and logging in ControlsManager - fix 0.2.24: After setting override, I cannot disable override or change it, from the UI Fixes [#119](https://github.com/ohAnd/EOS_connect/issues/119)
- fix: update expense and income color representation to use 'lightgray' for better visibility
- fix: update expense and income color representation to improve visibility thresholds
- chore: update version prefix in workflow and version file to 0.2.25 - adjust SOC color representation in schedule manager

**Version 0.2.25.144-fix1** published on 2025-10-19
- fix HAaddon - src missing
- feat: implement retry logic for HTTP requests in LoadInterface and add unit tests
- style: improve CSS formatting and enhance font size scaling for better responsiveness
- feat: update schedule display to include SOC and improve expense/income representation
- fix: improve logging for charge power limitation in FroniusWRV2 class
- feat: add planActive state and update charging mode logic in EVCC interface - fix Haus-Batterie wird nicht gesperrt, sofern evcc mode = "PV" und Ladeplan aktiv Fixes [#66](https://github.com/ohAnd/EOS_connect/issues/66)
- chore: update version prefix in workflow and version file to 0.2.25 - adjust SOC color representation in schedule manager
- fix: update API version to 0.0.2 and enhance logging for EVCC charging state transitions

**Version 0.2.01.138** published on 2025-10-14
- feat: refactor API request handling in PvInterface for improved error management and retry logic
- feat: add testing workflows for Docker builds and implement unit tests for PvInterface error handling and retry logic
- feat: improve scheduling algorithm in EosInterface and add comprehensive unit tests
- fix: correct conditional checks for SOC data source selection and ensure proper capacity calculation - fix ERROR [BATTERY-IF] source currently not supported. Using default start SOC = 5%. Fixes [#111](https://github.com/ohAnd/EOS_connect/issues/111)

**Version 0.2.01.136** published on 2025-10-11
- feat: enhance error logging in LoadInterface and improve SOC error handling in BatteryInterface
- feat: aggregate 15-min intervals to hourly Wh in __get_pv_forecast_evcc_api for improved accuracy - closes [#108](https://github.com/ohAnd/EOS_connect/issues/108) - thanks to @forouher

**Version 0.2.01.135** published on 2025-10-10
- feat: update logging.js for improved functionality and performance
- feat: add SOC failure handling and reset logic in BatteryInterface for improved reliability

**Version 0.2.01.134** published on 2025-10-09
- feat: enhance optimization scheduling logic to support first run alignment and improve quarter-hour synchronization
- feat: implement background price update service in PriceInterface for improved data retrieval - touches [#45](https://github.com/ohAnd/EOS_connect/issues/45)

**Version 0.2.01.133** published on 2025-10-08
- feat: add override modes to test scenarios and update HTML for selection
- feat: enhance override menu with better order for duration selection and grid charge power controls - touches [#105](https://github.com/ohAnd/EOS_connect/issues/105)
- feat: add fixed price adder and relative price multiplier to price calculations for akkudoktor/ default price source - fix Excluded taxes and grid fees lead to wrong optimization - Fixes [#88](https://github.com/ohAnd/EOS_connect/issues/88) and Modul 3 Prices - TOU - static/ dynamic prices - grid fees
touches [#51](https://github.com/ohAnd/EOS_connect/issues/51)
- feat: add fixed price adder and relative price multiplier to configuration readme for default price source
- feat: update bug report manager to use EOS_connect repository for bug reports
- feat: refactor optimization scheduler and control logic for improved state management and runtime calculations -  Real-Time Price Response with EOS Connect: Supporting 15-Minute Intervals (and timed executions) touches [#104](https://github.com/ohAnd/EOS_connect/issues/104)

**Version 0.2.01.132** published on 2025-10-05
- refactor: update test mode handling and improve variable naming in data fetching methods
- fix: correct max charge power retrieval in schedule manager
- style: comment out console logs in menu notifications

**Version 0.2.01.131** published on 2025-10-05
- refactor: improve code formatting and enhance timestamp handling in MemoryLogHandler
- feat: clickable links and log [Main] with color in web logger
- feat: web logger adding search filter
- feat: create generated bug report for github issue
- fix: correct condition for determining current mode at hour in showSchedule

**Version 0.2.01.130** published on 2025-10-05
- fix: web api pathes for logger to align also with HA addon

**Version 0.2.01.129** published on 2025-10-04
- fix: improve error messages and refactor variable names for clarity in PvInterface
- fix: rename timezone parameter to tz_name for consistency and clarity
- feat: implement in-memory logging handler with API endpoints for log retrieval and management
- full refactoring of UI backend + integration of ui log viewer
- fix: update logging prefixes for consistency and clarity across API and control modules
- feat: introduce web ui system log view with several filters and alert dashboard incl. notification via menu and menu entries
- fix: update showSchedule function to include data_controls parameter for enhanced schedule management
- fix: conditions in evcc state overrides
- fix: adjust font sizes for mobile responsiveness in main and full-screen overlays
- feat: implement full-screen override controls menu and enhance UI interactions + new info popup
- feat: add EOS Connect icons for control modes and update ControlsManager and ScheduleManager to utilize them
- fix: update logging.js for improved functionality and compatibility

**Version 0.1.24.124** published on 2025-10-03
- refactor: remove pvlib dependency and implement custom solar position and angle of incidence calculations
- fix: enhance temperature forecast retrieval with error handling and default fallback
- feat: add Solcast integration for high-precision solar forecasting and update configuration documentation - fix feature request: solcast data from home assistant Fixes [#100](https://github.com/ohAnd/EOS_connect/issues/100)
- fix: increase precision of hourly price calculations to 9 decimal places - fix smartenergy_at prices deviate Fixes [#98](https://github.com/ohAnd/EOS_connect/issues/98)

**Version 0.1.24.123** published on 2025-09-28
- fix: implement retry mechanism for price retrieval failures
- fix: enhance PV forecast retrieval with timezone-aware processing and error handling - fixing evcc change at 0.208.1 - touches [#89](https://github.com/ohAnd/EOS_connect/issues/89)
- fix: update datetime handling for historical energy data to use timezone-aware processing due to deprecated functions
- refactor: remove unused load profile creation methods and improve fallback logic for historical data - fix In EOS connect Grafik wird Load nicht angezeigt.
Fixes [#97](https://github.com/ohAnd/EOS_connect/issues/97)

**Version 0.1.24.122** published on 2025-09-27
- fix: improve error handling for missing solar forecast data in EVCC API
- fix: enhance logging for invalid sensor data processing in LoadInterface
- fix: improve error handling and logging for EVCC API forecast retrieval
- fix: enhance error handling and logging in PV forecast_solar retrieval
- fix: enhance error handling and logging for PV forecast akkudoktor and openmeteo lib retrieval
- fix: improve error handling and logging for EOS version retrieval and connection issues - close Connection problem Fixes [#72](https://github.com/ohAnd/EOS_connect/issues/72)
- docs: update installation instructions for EOS Connect and Home Assistant add-ons - touches [#72](https://github.com/ohAnd/EOS_connect/issues/72) Connection problem
- fix: disable debug logging for loadpoints and EVCC state fetching

**Version 0.1.23.120** published on 2025-09-21
- feat: update chart and battery data handling to use server timestamp for accurate hour labels
- feat: add safety check to prevent AC charging when battery SoC exceeds maximum limit (EOS bug workaround)
- feat: adapt displaying of grid/ ac charge data for wrong given eos values and add test endpoints for optimization request and response JSON files
- fix: correct comment for battery price unit in configuration
- fix: disable test mode by setting TEST_MODE to false
- feat: implement timezone handling for schedule display and update time labels to reflect server time

**Version 0.1.23.117** published on 2025-09-13
- feat: enhance MQTT connection handling with failure tracking and improved logging - touches [#91](https://github.com/ohAnd/EOS_connect/issues/91)

**Version 0.1.23.116** published on 2025-09-11
- feat: add EVCC support for PV forecasts and improve configuration documentation - fix [#89](https://github.com/ohAnd/EOS_connect/issues/89)

**Version 0.1.23.115** published on 2025-09-10
- feat: enhance SOC value handling in BatteryInterface for improved format detection - fix [#87](https://github.com/ohAnd/EOS_connect/issues/87) openHAB items with UoM throw an error

**Version 0.1.0.114** published on 2025-09-07
- feat: update Fronius GEN24 interfaces for enhanced authentication and backward compatibility - touches [#86](https://github.com/ohAnd/EOS_connect/issues/86)
- feat: enhance firmware detection and authentication handling in Fronius GEN24 V2 interface

**Version 0.1.0.113-fix1** published on 2025-09-06
- fix: update inverter type options to include fronius_gen24_v2 in config.yaml

**Version 0.1.0.113** published on 2025-09-06
- feat: add Fronius GEN24 V2 interface with enhanced authentication support
  - Implemented FroniusWRV2 class for improved authentication handling
  - Updated README and CONFIG_README to reflect new inverter type
  - Modified eos_connect.py to support both fronius_gen24 and fronius_gen24_v2
  - Enhanced error handling and logging for authentication issues
  - fixes [#86](https://github.com/ohAnd/EOS_connect/issues/86)

**Version 0.1.0.111** published on 2025-08-20
- fix:
    - feat: add PortInterface for managing port availability and conflicts in EOS Connect web server - fixes [#83](https://github.com/ohAnd/EOS_connect/issues/83) EOS Connect starting and immediatly shuts down again in Home Assistant
    - fix: enforce Python version requirement to 3.11 or higher

**Version 0.1.0.109** published on 2025-08-03
- doc:
    - docs: enhance load sensor requirements and configuration details for improved clarity - touches [#78](https://github.com/ohAnd/EOS_connect/issues/78) Load Sensor Fehlende Daten

**Version 0.1.0.108** published on 2025-07-30
- feat:
    - add EVCC version handling and improve API response parsing - in advance to https://github.com/evcc-io/evcc/pull/22299
- doc:
    - update electricity price configuration with important notes on tax/fee basis - fix [#76](https://github.com/ohAnd/EOS_connect/issues/76)

**Version 0.1.0.106** published on 2025-07-22
- feat:
    - enhance EvccInterface with default state handling and improved error resilience

**Version 0.1.0.105** published on 2025-07-18
- fix:
    - fix: correct key for ambient temperature in inverter data retrieval
- doc:
    - enhance dynamic charging curve functionality for battery management

**Version 0.1.0.103** published on 2025-07-06
- feature:
    - [feat] enable/disable charging curve - based on discussion with @WolfImBusch

**Version 0.1.0.102-fix2** published on 2025-07-04
- fix:
    - change max configurable value in HA addon for inverter max_grid_charge_rate and max_pv_charge_rate - [#74](https://github.com/ohAnd/EOS_connect/issues/74)
- org:
    - add building of armhf/ armv7 / i386 - until finally deprecated - https://www.home-assistant.io/blog/2025/06/11/release-20256/#deprecating-installation-methods-and-32-bit-architectures


**Version 0.1.0.102** published on 2025-06-28
- orj:
    - Update README.md with enhanced features and quick start guide; add flow diagram and updated screenshot
**Version 0.1.0.99** published on 2025-06-26
- feat: 
    - Merge pull request [#62](https://github.com/ohAnd/EOS_connect/issues/62) from paule96/make_errors_with_more_conent. Make errors with more content and make it possible in debug mode to replay request.

**Version 0.1.0.97** published on 2025-06-26
- org:
    - adjust initialization wait time for interfaces based on pv_forecast entries
- fix:
    - fix: shift in akkudoktor forecast by 1 hour over the day
    - fix: extend data for openmeteo lib for the whole current day
    - fix: extend error recognition for openmeteo lib integration fix [#68](https://github.com/ohAnd/EOS_connect/issues/68) OpenMeteo forecast failing with many forecast entries

**Version 0.1.0.94** published on 2025-06-25
- org:
    - docs: update configuration hints for load parameters to clarify optional settings - fix  [#60](https://github.com/ohAnd/EOS_connect/issues/60) CONFIG_README.md: Note and/or corrections
    - docs: add hints for access token usage in load and battery configurations - closes [#61](https://github.com/ohAnd/EOS_connect/issues/61) - Request failed while fetching battery SOC: 403 Client Error: Forbidden for url: and others
    - removed building of armhf/ armv7 / i386 - deprecated - https://www.home-assistant.io/blog/2025/06/11/release-20256/#deprecating-installation-methods-and-32-bit-architectures

**Version 0.1.0.92** published on 2025-06-23
- Features:
    - feat: enhance PV forecast options and configuration, adding Open-Meteo sources and timezone support - fix [#63](https://github.com/ohAnd/EOS_connect/issues/63) Akkudoktor forecast Server not available, got error 422
    - feat: add OpenMeteo Lib forecast integration and refactor forecast retrieval logic for second openmeteo option 'openmeteo'=lib and 'openmeteo_local' with local model calculation
- Fixes: 
    - fix: correct 'horizont' to 'horizon' in configuration and update related logging
    - fix: correct 'horizont' to 'horizon' in configuration (breakabale change!) and updated config description for new solar forecast sources

**Version 0.1.0.87-fix2** published on 2025-06-22
- Fixes:
    - HA addon: missing dependency for pvlib building for image generation

**Version 0.1.0.87-fix1** published on 2025-06-22
- Fixes:
    - HA addon: missing dependency for pvlib for image generation

**Version 0.1.0.87** published on 2025-06-22
- Features:
    - feat: enhance PV interface to support multiple forecast sources and improve error handling - step 1 for 'Akkudoktor forecast Server not available, got error 422' #63
- Fixes:
    - fix: correct 'horizont' to 'horizon' in configuration (breakabale change!) and updated config description for new solar forecast sources

**Version 0.1.0.85** published on 2025-06-18
- org:
    - refactoring of pv interface - prep for additional sources of solar forecast

**Version 0.1.0.84** published on 2025-06-17
  - Features:
    - feat: add default PV and temperature forecast to use at request errors and improve error handling in price interface - small workaorund for akkudoktor api outage

**Version 0.1.0.83** published on 2025-06-10
- Features:
    - feat: enhance EVCC interface and web display for multiple vehicle support - fix  [#57](https://github.com/ohAnd/EOS_connect/issues/57) second load point from evcc
- Fixes:
    - fix: remove unnecessary punctuation in CONFIG_README for clarity - fix [#60](https://github.com/ohAnd/EOS_connect/issues/60) CONFIG_README.md: Note and/or corrections

**Version 0.1.0.81** published on 2025-06-09
- Fixes:
    - fix: update CONFIG_README with enhanced configuration sections and clearer usage hints
    - fix: enhance EVCC configuration handling with improved URL validation and logging

**Version 0.1.0.80** published on 2025-06-08
- Fixes: 
    - fix: update CONFIG_README with hint on configuration errors and comment out debug logs in PriceInterface - fix Allow in the parsing of the yaml that optional properties can left empty or not mentioned [#52](https://github.com/ohAnd/EOS_connect/issues/52)
    - fix: enhance MQTT connection handling with error logging and status updates - reference Allow in the parsing of the yaml that optional properties can left empty or not mentioned [#52](https://github.com/ohAnd/EOS_connect/issues/52)
    - fix: add configuration validation in EvccInterface class to ensure valid URL and server reachability
    - fix: improve code readability and add configuration validation in PriceInterface class - references Allow in the parsing of the yaml that optional properties can left empty or not mentioned [#52](https://github.com/ohAnd/EOS_connect/issues/52)
    - fix: enhance configuration validation in LoadInterface class - reference Allow in the parsing of the yaml that optional properties can left empty or not mentioned [#52](https://github.com/ohAnd/EOS_connect/issues/52)

**Version 0.1.0.78-fix1** published on 2025-06-07
- Fixes: workaround for HA addon config bug for optional parameters - default is now set to "" (empty string) to avoid to fill up with 'null'

**Version 0.1.0.78** published on 2025-06-01
- fix: use get method for additional load configuration to provide default values - part of [#52](https://github.com/ohAnd/EOS_connect/issues/52)
- fix: update configuration key for feed-in tariff price to improve clarity - fix [#53](https://github.com/ohAnd/EOS_connect/issues/53)
- fix: update fixed_24h_array format in configuration to remove brackets and improve clarity

**Version 0.1.0.76** published on 2025-05-26
- Fix: HA addon config for fixed_24h_array - input as string (fixed_24h_array: 10.25, 15.2, ... without brackets) - direct array not supported

**Version 0.1.0.75** published on 2025-05-25
- Features:
  - feat: add fixed 24-hour price configuration and update price interface handling - step 1 of [#51 Modul 3 Prices - TOU - static/ dynamic prices - grid fees](https://github.com/ohAnd/EOS_connect/issues/51)
  
**Version 0.1.0.74** published on 2025-05-25
- Features:
  - feat: enhance load management with additional load configurations and UI updates - touches #34 (Add other Loads (Heat pumps, Dishwasher, Washing machine))
  - feat: small points approaching #52 (regarding Allow in the parsing of the yaml that optional properties can left empty or not mentioned)

**Version 0.1.0.72** published on 2025-05-21
- Features:
  - feat: add support for smartenergy.at as a price source and implement price retrieval logic - closes #47
- Other Changes
  - refactor: update callback assignments for interfaces to improve clarity and avoid concurrent calls at startup

**Version 0.1.0.71** published on 2025-05-19
- Fix: refactor: update callback assignments for interfaces to improve clarity and avoid concurrent calls at startup

**Version 0.1.0.70** published on 2025-05-18
- Features:
  - implements the evcc external battery control to integrate the control of all evcc known inverter/ battery systems

**Version 0.1.0.67** published on 2025-05-16
- Fixes
  - Refactor change_control_state function and remove commented-out code in EosInterface

**Version 0.1.0.66** published on 2025-05-14
- Features:
  - feature: - closes #38 openHAB: Extension of the load data range to a configurable value between 2 days and 2 weeks - refactoring of load interface to have same result for openhab and homeassistant source
  - Enhance logging for zero energy readings in LoadInterface

- Fixes
  - Remove commented-out logic for skipping zero energy readings in LoadInterface - homeassistant
  - Remove commented-out logic for skipping zero energy readings in LoadInterface - openhab

**Version 0.1.0.60-fix1** published on 2025-05-13
- Fixes
  - fix: config schema for price_euro_per_wh_accu

**Version 0.1.0.60** published on 2025-05-13
- Features
  - Enhance Fronius Inverter Interface and MQTT Integration new method fetch_inverter_data to retrieve real-time inverter data, including various temperature readings and fan control percentages.
  - Updated the MQTT interface to include new sensors for inverter temperature, AC module temperature, DC module temperature, battery module temperature, and fan control metrics.
  - Improved logging messages for better debugging and tracking of inverter operations.
- Fixes
  - fix: config schema for price_euro_per_wh_accu

**Version 0.1.0.59** published on 2025-05-13
- Fixes
  - fix: adjust energy comparison logic to allow equal values for car and load energy - fixes #39 Error Load smaller then car load, if both values are 0.0 Wh

**Version 0.1.0.58-fix1** published on 2025-05-13
- Fixes
  - fix: config also for HA addon

**Version 0.1.0.58** published on 2025-05-13
- Features
  - feat: add price configuration for battery in €/Wh and update related logic

**Version 0.1.0.56** published on 2025-05-06
- Features
  - feat: update max charge power handling to event based by soc changes

**Version 0.1.0.55** published on 2025-05-04
- Features
  - no specific
- Fixes
  - fix: removed max car load detection - car load has to be in watts
- Other Changes
  - no specific

**Version 0.1.0.54** published on 2025-05-04
- Features
  - feat: implement MQTT control command handling and update base control modes
- Fixes
  - no specific
- Other Changes
  - no specific

**Version 0.1.0.53** published on 2025-05-04
- Features
  - no specific
- Fixes
  - fix: update fetch URL for mode override control to use relative path - fixes HA ingress integration
- Other Changes
  - no specific

**Version 0.1.0.52** published on 2025-05-03
- Features
  - feat: refine C-rate calculation for dynamic maximum charge power with improved thresholds and rounding
  - feat: add dynamic maximum charge power to MQTT integration and reduce dyn max charge to 10 watts steps
- Fixes
  - fix: update dynamic maximum charge power display to show two decimal places
- Other Changes
  - no specific
  
**Version 0.1.0.51** published on 2025-05-02
- Features
  - feat: dyn max charge power also for DC; enhance BaseControl for DC charge demand tracking; modify UI label for charge power
  - feat: enhance dynamic charge power calculation with minimum threshold and decay function incl. c-rate
- Fixes
  - no specific
- Other Changes
  - docs: Update README and CONFIG_README for clarity and feature enhancements

**Version 0.1.13** published on 2025-04-30
- Features
  - feat: Implement mode override functionality and enhance UI for control management (-> current controls - click icon on the right)
- Fixes
  - fix: correction of unplausible car load vs. main load
- Other Changes
  - no specific

**Version 0.1.12** published on 2025-04-27
- Features
    - feature: Enhance EVCC charging mode handling and update UI for smart cost scenarios
- Fixes
    - fix: Update version prefix in docker_develop.yml to include minor version
    - fix: Update max charge power display from watts to kilowatts in index.html
    - fix: Correct calculation of remaining charging duration in index.html
- Other Changes
  - no specific

**Version 0.1.11-fix6** published on 2025-04-25
- adding builds for armhf / armv7 - after verifiying run for aarch64

**Version 0.1.11-fix5** published on 2025-04-25
- fixing image build - submodule fetching

**Version 0.1.11-fix4** published on 2025-04-25
- Other Changes
    -  HA addon: pre build images - fixing copy path/ submodule

**Version 0.1.11-fix2** published on 2025-04-25
- Other Changes
    -  HA addon: pre build images - fixing executable path
  
**Version 0.1.11-fix1** published on 2025-04-25
- Other Changes
    -  HA addon: switching to pre build images

**Version 0.1.11** published on 2025-04-25
- Features
    - no specific
- Fixes
    - fix: Add paho-mqtt dependency to requirements
- Other Changes
    - no specific

**Version 0.1.10** published on 2025-04-25
- Features
    - feature: Add MQTT configuration support and interface for Home Assistant integration - close #11 Extract Current Controls values to Homeassistant entities
    - feat: (inverter) refactor version handling and add Docker workflow for image build and push
    - feature: Enhance EVCC interface and UI: - Added detailed vehicle data fetching to the EVCC interface. - Updated HTML to display vehicle charging details and status. - Improved CSS for smoother transitions on value changes.
- Fixes
    - fix: (inverter) update API path handling in login and logout methods
    - fix: (inverter) add version handling for Fronius GEN24 API endpoints
- Other Changes
    - nothing ;-)

**Version 0.1.9** published on 2025-04-22
- Features
    - feature: add several detail data for direct visibility + update layout and font sizes for better readability in dashboard
- Fixes
    - feature: refactor battery interface initialization and add calculating of remaining usable energy
- Other Changes
  - org: update versioning scheme in workflows and version.py for consistency


**Version 0.1.8** published on 2025-04-21
 - Features
     - feat: Update chart data to include income fixes #15 Showing revenue on generated website  and change label for expenses
 - Fixes
     - fix: refine overlay menu styles + incl. links to repo, changelog, issues and improve mobile responsiveness
     - fix: update terminology and color coding for charge modes in index.html
     - fix: enhance error handling in EOS Connect interface - fixes startup behavior with default config
 - Other Changes
     - docs: Update README and CONFIG_README for clarity and configuration details - fix #20

**Version 0.1.6** published on 2025-04-20
- Features
  - Add new mode for discharge allowed during e-car charging in min+pv mode and enhance battery charging data display
- Fixes
  - initialization / startup phase to avoid inverter changes at restart
  - Comment out inverter_mode_num assignment for testing purposes
  - state messages in log and clearer error messages
- Other Changes
  - refactor: Simplify overall state checks and enhance EVCC state handling if charging in PV mode

**Version 0.1.4** published on 2025-04-18
- Features
  - Add versioning to Docker workflows and implement cleanup for old develop versions
  - Add step to pull latest changes before setting version string in Docker workflow
  - Update cleanup process for old Docker images using GitHub CLI
  - Enhance Docker workflows and add version display in web interface
- Fixes
  - Update commit message format for version file changes in Docker workflow
  - Force push changes to version file during Docker image build
  - Enhance cleanup process for old Docker versions by adding VERSION_PREFIX environment variable
  - Update upload artifact action to v4 and rename artifact for clarity

- Other Changes
  - Consolidate Docker workflows by removing nightly and snapshot workflows, and enhancing the main workflow for versioning and cleanup

**Version 0.0.26** published on 17.04.2025
- Fixes:
    - [Resolved inconsistencies between request and response states on the dashboard.](https://github.com/ohAnd/EOS_connect/issues/14)
- Features:
    - improving dashboard especially for mobile view and usual screen sizes
    - Enhance EVCC integration by adding charging mode handling and updating UI to reflect current charging state and mode
- Documentation:
    - ...

**Version 0.0.24** published on 15.04.2025
- Fixes:
    - Resolved inconsistencies between request and response states on the dashboard.
    - Fixed a bug where the EVCC state change did not revert to the former EOS target state correctly.
- Features:
    - Improved the response messages for the optimization scheduler and added timing details for the current and next run.
    - Enhanced the optimization scheduler's state management for better functionality.
- Documentation:
    - Updated the README to include additional details about configuring the feed-in price.

**Version 0.0.22-fix1** published on 13.04.2025
- fixing ha addon config for new entries
  
**Version 0.0.22** published on 13.04.2025
- feat: Add support for Tibber price integration
- fix: Resolve issue with incorrect PV forecast data parsing
- feat: Add health check endpoint for monitoring
- refactor: Simplify configuration schema validation logic
- fix: Address issue with EVCC integration causing unnecessary API calls
- chore: Update dependencies to latest versions
- feat: Enhance web interface with additional diagnostic information
- fix: Correct handling of time zones in load interface
- refactor: Optimize logging for better debugging and performance
- feat: Add support for multiple PV forecast sources in configuration

**Version 0.0.19** published on 11.04.2025
- fixes retrieving historical data if day not fully provided in data

**Version 0.0.18** published on 10.04.2025
- new EOS version released - adapting EOS connect to run with both
- see https://github.com/ohAnd/EOS_connect?tab=readme-ov-file#current-status

**Version 0.0.15** published on 07.04.2025
- feat: Enhance README with detailed functionality and usage instructions
- requesting with last startup_solution
- update logging messages in LoadInterface for clarity

**Version 0.0.14** published on 07.04.2025
- changing versioning of HA addon accprding to snapshot release
- feat: changing HA load interface to use data according to the current workday instead of last 2 days - closes [#4 Unterscheidung Arbeits- / Wochentage beim Erstellen des Lastprofils](https://github.com/ohAnd/EOS_connect/issues/4)
- adapting error feedback on webpage
- enhancing readme regarding historic data

**Version 0.0.7** published on 07.04.2025
- feat: Update control state logging and enhance data structure for current demands + extend webview

**Version 0.0.6** published on 07.04.2025
- fixing wrongly shifted load request and refactoring

**Version 0.0.5** published on 06.04.2025
- extend with EVCC connection to avoid discharge when car is charging

**Version 0.0.4-fix5** published on 06.04.2025
- change icon

**Version 0.0.4-fix4** published on 06.04.2025
- minor change regarding HA addon config

**Version 0.0.4-fix2** published on 06.04.2025
- fixes unnecessary logins and writing of battery settings to fronius inverter

**Version 0.0.4** published on 06.04.2025
- extend config and feature to control fronius inverter

**Version 0.0.3** published on 05.04.2025
- cleanup config and translations

**Version 0.0.2-fix2** published on 05.04.2025
- fixes default config

**Version 0.0.2** published on 04.04.2025
- bump to latest eos_connect
- breakable change in config - see pv_forecast

**Version 0.0.1-fix1** published on 04.04.2025
- adapt config.yaml for unneeded entry

**Version 0.0.1** published on 30.03.2025
- inital start
