FROM ghcr.io/home-assistant/base:3.23

# build-image only emits io.hass.arch and io.hass.version. The rest of the add-on
# metadata came from the legacy builder and has to be declared here instead --
# without io.hass.type the image inherits "base" from the base image.
LABEL \
    io.hass.type="addon" \
    io.hass.name="Modbus TCP Smart Meter" \
    io.hass.description="emulates a modbus tcp client to pretend to be an energy metering device" \
    io.hass.url="https://github.com/ohAnd/ha_addons"

# Installiere Python und pip
RUN apk add --no-cache python3 py3-pip git

# Erstelle und aktiviere eine virtuelle Umgebung
RUN python3 -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir pymodbus==3.0.0 pyserial>=3.5 pyserial-asyncio>=0.6 requests>=2.28.1 PyYAML>=6.0.2

# Setze das Arbeitsverzeichnis und kopiere den Code
COPY ./src /app
WORKDIR /app
RUN ln -sf /data/options.json /app/config.yaml

# Expose port 502 for Modbus TCP
EXPOSE 502

# Setze den Befehl für den Container-Start
CMD ["/opt/venv/bin/python", "/app/modbus_tcp_smartmeter.py"]
