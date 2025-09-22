ARG BUILD_FROM
FROM $BUILD_FROM

# Install build tools in separate layer (cached unless Alpine updates)
RUN apk add --no-cache \
    g++ gcc libffi-dev musl-dev make \
    python3 py3-pip python3-dev git \
    hdf5-dev openblas-dev lapack-dev blas-dev gfortran \
    curl

# Create virtual environment first (cached)
RUN python3 -m venv /opt/venv

# Install dependencies before copying source code (better caching)
RUN . /opt/venv/bin/activate && \
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
        pvlib>=0.13.0 \
        open-meteo-solar-forecast>=0.1.22 \
        psutil>=7.0.0

# Copy application code last (most frequently changed)
COPY ./src /app
WORKDIR /app/src

# Configuration and health check
RUN ln -sf /data/options.json /app/src/config.yaml

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8081/ || exit 1

# Expose port 8081 for the add-on
EXPOSE 8081

# Set the command to start the container
CMD ["/opt/venv/bin/python", "/app/src/eos_connect.py"]
