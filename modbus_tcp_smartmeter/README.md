
Table of content
- [modbus tcp smartmeter](#modbus-tcp-smartmeter)
  - [features](#features)
  - [configuration](#configuration)
  - [installing locally as system service](#installing-locally-as-system-service)
  - [Further information](#further-information)

# modbus tcp smartmeter

Simulates a Fronius Smart Meter for providing necessary information to inverters (e.g. Gen24).

## features
- ...
- ...

## configuration
...

## installing locally as system service

installing as system service:

`sudo cp /home/pi/ModbusTCP_SmartMeter.py /usr/local/bin/`

`sudo chmod +x /usr/local/bin/ModbusTCP_SmartMeter.py`


create service file /home/pi/ModbusTCP_SmartMeter.service

```
[Unit]
Description=Modbus TCP Smart Meter Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/your/modbus_tcp_smartmeter.py
WorkingDirectory=/path/to/your/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```
then

`sudo cp /home/pi/ModbusTCP_SmartMeter.service /etc/systemd/system/`

`sudo systemctl enable ModbusTCP_SmartMeter.service`

`sudo systemctl start ModbusTCP_SmartMeter.service`

If you prefer not to run the script as root, you can use setcap to grant the necessary capabilities:

`sudo setcap 'cap_net_bind_service=+ep' /usr/bin/python3`

This setup will ensure your script runs automatically at startup with the necessary permissions.


## Further information

...