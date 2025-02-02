**Version 0.3.63** published on 02.02.2024
- making mqtt auto discover configurable see in mqtt config section

**Version 0.3.62** published on 02.02.2024
- bump to last batcontrol:
- add dynamic price limit ([#117](https://github.com/muexxl/batcontrol/pull/117))
- Add options to tweak batcontrol behavior ([#116](https://github.com/muexxl/batcontrol/pull/116))

**Version 0.3.6** published on 01.02.2024
- see: https://github.com/muexxl/batcontrol/issues/78
- adding homeassistant mqtt autodiscovery config messages at startup
- all mqtt values setter/ getter will be autoconfigured for direct usage in homeassistant and others (e.g. easier integration in e.g. openhab with addon mqtt)

**Version 0.3.5-fix1** published on 28.01.2024
- fixing pushing multi schedule to fronius
- CHARGE_MAX behaviour remains as before and is dependet by ``max_pv_charge_rate``
- DISCHARGE_MAX added and is newly dpendend by ``max_bat_discharge_rate``

**Version 0.3.5** published on 28.01.2024
- new config parameter for max discharge rate in mode 10
  - ~~changing the target schedule on fronius side from CHARGE_MAX to DISCHARGE_MAX when triggering "Discharge allowed"~~
  - value will be expected in Watts

**Version 0.3.4** published on 28.01.2024
- first check with DISCHARGE_MAX without config

**Version 0.3.3-hotfix1** published on 24.01.2024

!!! WARNING !!!

There has been a breaking change in the configuration file.
YOU NEED TO UPDATE YOUR CONFIGURATION in the evcc section

change below lines in the config to make it work again:

loadpoint_topic: evcc/loadpoints/1/charging

to

loadpoint_topic:

- evcc/loadpoints/1/charging

**Version 0.3.3** published on 23.01.2024

HA Addon specific changes:

- move logfile to /data/batcontrol.log to make it persistant
- added entryscript for container startup
- mount persistant addon config folder in /app/addon_config
- use load_profile.csv from addon config folder if file exists
- use batcontrol_config.yaml from addon config folder if file exists instead of configuration provided via the addon configuration

implement version 0.3.3 of batcontrol:

- EVCC : Enhance loadpoint configuration to support multiple topics by @MaStr in #80
- MQTT & EVCC : Improve reconnect handling on broker restart by @MaStr in #82
- Update to Documentation by @johannesghd in #86
- Set Fronius Solar.API to active on initialisation by @johannesghd in #85
- Set allow grid charging at the end of initialisation by @johannesghd in #83
- Update README.MD by @johannesghd in #88
- Feature: handle FC solar rate limit errors by @hashtagKnorke in #93
- Major refactoring of modules by @MaStr in #71
- Add MQTT Connection retry by @hashtagKnorke in #94
- Refactor pylint workflow to analyze only changed Python files by @hashtagKnorke in #102
- introduce proper OS-level timezone handling in Docker setup by @hashtagKnorke in #103
- gracefully handle multiple changed files by @hashtagKnorke in #104
- Add query parameter to allow modification of horizon used to forecast PV production in fcsolar.py by @johannesghd in #110
- 113 invalid login 01.00.00 am after installing the latest ha version by @MaStr in #114

special thanks goes to the contributers:
@MaStr
@hashtagKnorke
@johannesghd

corresponding issues can be found in the main github repo:
https://github.com/muexxl/batcontrol

**Version 0.3.2** published on 08.12.2024

- add evcc options in configuration

**Version 0.3.1** published on 07.12.2024

- Update to batcontrol 0.3.1
- fix bugs
- add MQTT options in configuration
- advanced logging

**Version 0.2.11** published on 14.11.2024

- Update to 0.2.11.
- fix bugs
- integrate PR

**Version 0.2.10** published on 29.10.2024

- Roll Back to intermediate version 0.2.8+ of underlying source code due to https://github.com/muexxl/batcontrol/issues/32

**Version 0.2.9** published on 29.10.2024

- exclude energy that is reserved for backup power when calculating the avaiable energy

**Version 0.2.8** published on 29.10.2024

- fixed issue with timezones in docker #3 https://github.com/muexxl/batcontrol_addon/issues/3

**Version 0.2.7** published on 21.10.2024

- fixed bug in force_charge() introduced with variable renaming in 0.2.0
- fixed bug in Forecast SolarAPI when providing empty apikeys

**Version 0.2.5** published on 18.10.2024

- fixed bug / Bad request to inverter when setting time of use
- code refactoring: renamed fronius module to inverter

**Version 0.2.3** published on 17.10.2024

- added optional parameter `apikey` in pv installations. This parameter allows you to use your own API Key if you are a forecast solar customer
- fixed bug if parameter api is missing

**Version 0.2.0** published on 17.10.2024

- included MQTT capabilities (deactivated per default)
- updated to batcontrol 0.2.1
- new parameter :`max_pv_charge_rate`. Limits the rate at which your PV System charges your battery
- renamed parameter `max_charge_rate` to `max grid charge rate`. Limits the maximum charging rate of your battery when charging from the grid.
- remove unused parameter `max_grid_power`

**Version 0.1.5** published on 09.02.2024

- introduced limit for log file
- added hints in configuration via translations/en.yaml

**Version 0.1.3** published on 16.11.2023

- added support for Awattar (DE+AT)
- enhanced documentation

**Version 0.1.2** published on 8.11.2023

- enhanced documentation

**Version 0.1.1** published on 7.11.2023

- Updated logo.
- Updated icon.

**Version 0.1.0** published on 7.11.2023

starting point
