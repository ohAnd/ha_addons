# A Collection of ohAnd's Add-ons for Home Assistant


[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fohand%2Fha_addons)

## Add-ons

This repository contains different addons.


### [Batcontrol add-on](./batcontrol)

*Fork from https://github.com/muexxl/batcontrol.*

To use this addon you need a Fronius Inverter with a battery AND a dynamic priced electricity contract from Tibber.

Futher details can be found here https://github.com/ohAnd/batcontrol (forked from here https://github.com/muexxl/batcontrol)

The batcontrol addon builds locally during the install at Homeassistant.

<!-- ![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield] -->

### [EOS connect add-on](./eos_connect)

EOS Connect is a tool designed to easily collect the needed data for optimize energy usage by interacting with the EOS system. It displays the results dynamically on a webpage. And is controlling your PV / Battery System. Futher details can be found here https://github.com/ohAnd/EOS_connect.

To use this addon you need an openhab or homeassistant with persisted energy data and a running [EOS - Energy Optimization System](https://github.com/Akkudoktor-EOS/EOS) instance. Optional [EVCC](https://github.com/evcc-io/hassio-addon) is also connectable to cover some specific use cases during e-car charging.

*Note: Recommendation for a HA addon for EOS at https://github.com/Duetting/ha_eos_addon. (or https://github.com/thecem/ha_eos_addon)*

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
<!-- ![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield] -->

### [EOS connect develop add-on](./eos_connect_develop)

Contentwise same as above. Last develop version -> https://github.com/ohAnd/EOS_connect/tree/develop

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
<!-- ![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield] -->

### [modbus_tcp_smartmeter add-on](./modbus_tcp_smartmeter)

Small self running modbus tcp client to serve energy, power, voltage and current data for an central energy system or main hybrid inverter.

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

### [trmnlServer add-on](./trmnl_server)

This addons wrapping the trmnl server application to be a runnable docker in Home Assistant as an add-on.

Futher details can be found here https://github.com/ohAnd/trmnlServer

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]



<!--

Notes to developers after forking or using the github template feature:
- While developing comment out the 'image' key from 'example/config.yaml' to make the supervisor build the addon
  - Remember to put this back when pushing up your changes.
- When you merge to the 'main' branch of your repository a new build will be triggered.
  - Make sure you adjust the 'version' key in 'example/config.yaml' when you do that.
  - Make sure you update 'example/CHANGELOG.md' when you do that.
  - The first time this runs you might need to adjust the image configuration on github container registry to make it public
  - You may also need to adjust the github Actions configuration (Settings > Actions > General > Workflow > Read & Write)
- Adjust the 'image' key in 'example/config.yaml' so it points to your username instead of 'home-assistant'.
  - This is where the build images will be published to.
- Rename the example directory.
  - The 'slug' key in 'example/config.yaml' should match the directory name.
- Adjust all keys/url's that points to 'home-assistant' to now point to your user/fork.
- Share your repository on the forums https://community.home-assistant.io/c/projects/9
- Do awesome stuff!
 -->

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
