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
  - feat: dyn max charge popwer also for DC; enhance BaseControl for DC charge demand tracking; modify UI label for charge power
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
