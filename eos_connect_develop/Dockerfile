ARG BUILD_FROM
FROM $BUILD_FROM

# Install required build tools
RUN apk add --no-cache g++ gcc libffi-dev musl-dev make python3 py3-pip python3-dev git

# Copy the application code
COPY ./src /app

# Debug: List the contents of /app and /app/src to verify the copy
RUN ls -l /app
RUN ls -l /app/src

# Set the working directory
WORKDIR /app/src

# Create and activate a virtual environment, then install dependencies
RUN python3 -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir \
        Flask>=2.2.5 \
        requests>=2.26.0 \
        pandas>=2.2.3 \
        numpy>=2.2.2 \
        gevent>=24.2.1 \
        pyyaml>=6.0 \
        pytz>=2025.1 \
        ruamel.yaml>=0.18.10 \
        paho-mqtt>=2.1.0 \
        pvlib>=0.13.0

# Link the configuration file
RUN ln -sf /data/options.json /app/src/config.yaml

# Add HEALTHCHECK directive
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8081/ || exit 1

# Expose port 8081 for the add-on
EXPOSE 8081

# Set the command to start the container
CMD ["/opt/venv/bin/python", "/app/src/eos_connect.py"]
