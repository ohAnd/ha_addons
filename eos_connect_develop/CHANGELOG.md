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
