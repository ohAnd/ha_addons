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