ARG BUILD_FROM
FROM $BUILD_FROM

# Install Python, pip, and other required tools
RUN apk add --no-cache python3 py3-pip git

# Copy the application code
COPY ./src /app

# Set the working directory
WORKDIR /app

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
        ruamel.yaml>=0.18.10

# Link the configuration file
RUN ln -sf /data/options.json /app/src/config.yaml

# Add HEALTHCHECK directive
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8081/ || exit 1

# Expose port 8081 for the add-on
EXPOSE 8081

# Set the command to start the container
CMD ["/opt/venv/bin/python", "/app/src/eos_connect.py"]
