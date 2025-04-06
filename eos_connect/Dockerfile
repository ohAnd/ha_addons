ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache python3 py3-pip git

COPY ./src /app
COPY ./src/requirements.txt /app/requirements.txt

RUN python3 -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app
RUN ln -sf /data/options.json /app/src/config.yaml

# Expose port 502 for Modbus TCP
EXPOSE 8081

# Setze den Befehl für den Container-Start
CMD ["/opt/venv/bin/python", "/app/src/eos_connect.py"]
