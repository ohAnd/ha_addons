ARG BUILD_FROM
FROM $BUILD_FROM

# Installiere Python und pip
RUN apk add --no-cache python3 py3-pip git

# Erstelle und aktiviere eine virtuelle Umgebung
RUN python3 -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir -r ./src/requirements.txt

# Setze das Arbeitsverzeichnis und kopiere den Code
COPY ./src /app
WORKDIR /app
RUN ln -sf /data/options.json /app/src/config.yaml

# Expose port 502 for Modbus TCP
EXPOSE 8081

# Setze den Befehl für den Container-Start
CMD ["/opt/venv/bin/python", "/app/src/eos_connect.py"]
