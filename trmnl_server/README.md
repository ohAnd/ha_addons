## Overview
'TRMNL Local Web Server' is a local web server designed to serve local content (BMP image) to a TRMNL client e-ink display. It simulates the TRMNL cloud server (https://usetrmnl.app/). The server is built using Flask and supports serving BMP images, logging requests, and updating configuration settings.

To enable the usage of TRMNL with this self hosted server there are 2 options:
1. Firmware post https://github.com/usetrmnl/firmware/issues/61 supports self-hosted servers out of the box.
    - there is a possibilty mentioned for using http and https - due to legacy compatibility https have to used with trmnl_server
3. For older firmware a small change is required in [Firmware of TRMNL](https://github.com/usetrmnl/firmware/blob/e3db8c37990c2333ec90b1be10749f9d37620a18/include/config.h#L49)
    - original: ```#define API_BASE_URL "https://trmnl.app" ```
    - change to: ```#define API_BASE_URL "https://<your_ip>:<configured_port>" ``` (e.g. https://192.178.1.10:83)

## Further information

For further details, ongoing discussions, bugs and features you may check the main repository of trmnlServer.
https://github.com/ohAnd/trmnlServer

## local testenvironment

1. building docker container: `docker build --build-arg BUILD_FROM=homeassistant/amd64-base:latest -t test_trmnl_server .`
2. running the container: `docker run -d --name trmnl_server_container -p 83:83 test_trmnl_server`