**Version 0.1.21-fix1** 2025-07-04
- fix:
    - change max configurable value in HA addon for inverter max_grid_charge_rate and max_pv_charge_rate - [#74](https://github.com/ohAnd/EOS_connect/issues/74)
- org:
    - add building of armhf/ armv7 / i386 - until finally deprecated - https://www.home-assistant.io/blog/2025/06/11/release-20256/#deprecating-installation-methods-and-32-bit-architectures

**Version 0.1.21** published on 2025-06-28
- Features
    - enhance error logging for OPTIMIZE requests by including payload and response details
    - add the payload too to the error, so a user could replay the request
    - add the text content of a failed response to the output
- Fixes
    - refactor: - adjust initialization wait time for interfaces based on pv_forecast entries - fix: shift in akkudoktor forecast by 1 hour over the day - fix: extend data for openmeteo lib for the whole current day - fix: extend error recognition for openmeteo lib integration fix #68 OpenMeteo forecast failing with many forecast entries
- Other Changes
    - fixes screenshot filename for readme
    - Update README.md with enhanced features and quick start guide; add flow diagram and updated screenshot

**Version 0.1.20-fix1** published on 2025-06-26
- Fixes
    - fix: wrong naming of image for release version

**Version 0.1.20** published on 2025-06-25
- Features
    - feat: update Python version in Pylint workflow to 3.11
    - feat: add open-meteo-solar-forecast dependency to requirements
    - feat: enhance PV forecast options and configuration, adding Open-Meteo sources and timezone support - fix #63 Akkudoktor forecast Server not available, got error 422
    - feat: add OpenMeteo Lib forecast integration and refactor forecast retrieval logic for second openmeteo option 'openmeteo'=lib and 'openmeteo_local' with local model calculation
    - feat: enhance PV interface to support multiple forecast sources and improve error handling - step 1 for 'Akkudoktor forecast Server not available, got error 422' #63
    - feat: add default PV and temperature forecast to use at request errors and improve error handling in price interface - small workaorund for akkudoktor api outage
    - feat: enhance EVCC interface and web display for multiple vehicle support - fix  #57 second load point from evcc
- Fixes
    - fix: correct 'horizont' to 'horizon' in configuration and update related logging
    - fix: correct 'horizont' to 'horizon' in configuration (breakabale change!) and updated config description for new solar forecast sources
    - fix: remove unnecessary punctuation in CONFIG_README for clarity - fix #60 CONFIG_README.md: Note and/or corrections
- Other Changes
    - docs: update configuration hints for load parameters to clarify optional settings - fix  #60 CONFIG_README.md: Note and/or corrections
    - docs: add hints for access token usage in load and battery configurations - closes #61 - Request failed while fetching battery SOC: 403 Client Error: Forbidden for url: and others
    - org: refactoring of pv interface - prep for additional sources of solar forecast

**Version 0.1.19** published on 2025-06-09
- Features
    - no specific
- Fixes
    - fix: update CONFIG_README with enhanced configuration sections and clearer usage hints
    - fix: enhance EVCC configuration handling with improved URL validation and logging
    - fix: update CONFIG_README with hint on configuration errors and comment out debug logs in PriceInterface - fix Allow in the parsing of the yaml that optional properties can left empty or not mentioned #52
    - fix: enhance MQTT connection handling with error logging and status updates - reference Allow in the parsing of the yaml that optional properties can left empty or not mentioned #52
    - fix: add configuration validation in EvccInterface class to ensure valid URL and server reachability
    - fix: improve code readability and add configuration validation in PriceInterface class - references Allow in the parsing of the yaml that optional properties can left empty or not mentioned #52
    - fix: enhance configuration validation in LoadInterface class - reference Allow in the parsing of the yaml that optional properties can left empty or not mentioned #52
- Other Changes

**Version 0.1.18-fix1** published on 2025-06-07
- Fixes: workwround for HA addon config bug for optional parameters - default is now set to "" (empty string) to avoid to fill up with 'null'

**Version 0.1.18** published on 2025-06-06
- Features
    - feat: enhance PriceInterface to support string input for fixed 24-hour price array and extend default prices to 48 hours - needed for HA addon config
    - feat: add fixed 24-hour price configuration and update price interface handling - step 1 of #51 Modul 3 Prices - TOU - static/ dynamic prices - grid fees
    - feat: enhance load management with additional load configurations and UI updates - touches #34 (Add other Loads (Heat pumps, Dishwasher, Washing machine)) - and also small points approaching #52 (regarding Allow in the parsing of the yaml that optional properties can left empty or not mentioned)
- Fixes
    - fix: use get method for additional load configuration to provide default values - part of #52
    - fix: update configuration key for feed-in tariff price to improve clarity - fix #53
    - fix: update fixed_24h_array format in configuration to remove brackets and improve clarity
    - fix: round temperature values in inverter data
- Other Changes
    - docs: update README to enhance clarity and detail on EOS Connect features and functionality

**Version 0.1.17** published on 2025-05-22
- Features
    - feature: add support for smartenergy.at as a price source and implement price retrieval logic - closes [#47](https://github.com/ohAnd/EOS_connect/issues/47)
    - feature: implements the evcc external battery control to integrate the control of all evcc known inverter/ battery systems ([Support newly developed evcc battery API #12](https://github.com/ohAnd/EOS_connect/issues/12))
- Fixes
    - no specific
- Other Changes
    - refactor: update callback assignments for interfaces to improve clarity and avoid concurrent calls at startup
    - doc cleanup to close #12 Support newly developed evcc battery API

**Version 0.1.16** published on 2025-05-17
- Features
    - feature: - closes [#38 openHAB: Extension of the load data range to a configurable value between 2 days and 2 weeks](https://github.com/ohAnd/EOS_connect/issues/38) - refactoring of load interface to have same result for openhab and homeassistant source
    - feat: add price configuration for battery in €/Wh and update related logic
    - Enhance Fronius Inverter Interface and MQTT Integration
      - new method to retrieve real-time inverter data, including various temperature readings and fan control percentages.
      - Updated the MQTT interface to include new sensors for inverter temperature, AC module temperature, DC module temperature, battery module temperature, and fan control metrics.
- Fixes
    - fix: adjust energy comparison logic to allow equal values for car and load energy - fixes [#39 Error Load smaller then car load, if both values are 0.0 Wh](https://github.com/ohAnd/EOS_connect/issues/39)
- Other Changes
    - Refactor change_control_state function and remove commented-out code in EosInterface
    - Enhance logging for zero energy readings in LoadInterface
    - Remove commented-out logic for skipping zero energy readings in LoadInterface - homeassistant
    - Improved logging messages for better debugging and tracking of inverter operations

**Version 0.1.14** published on 2025-05-09
- Features
  - feat: update max charge power handling to event based by soc changes
  - feat: implement MQTT control command handling and update base control modes
  - feat: refine C-rate calculation for dynamic maximum charge power with improved thresholds and rounding
  - feat: add dynamic maximum charge power to MQTT integration and reduce dyn max charge to 10 watts steps
  - feat: enhance dynamic charge power calculation with minimum threshold and decay function incl. c-rate
  - feat: dyn max charge popwer also for DC; enhance BaseControl for DC charge demand tracking; modify UI label for charge power
- Fixes
  - fix: removed max car load detection - car load has to be in watts
  - fix: update fetch URL for mode override control to use relative path - fixes HA ingress integration
  - fix: update dynamic maximum charge power display to show two decimal places
- Other Changes
  - docs: Update README and CONFIG_README for clarity and feature enhancements

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
    - feature: add several detail data for direct visibility + update layout and font sizes for better readability in dashbaord
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
    - improving dashbaord especially for mobile view and usual screen sizes
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
