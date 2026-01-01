ARG BUILD_FROM
FROM $BUILD_FROM

# Install system dependencies and python packages via apk
# Using apk packages is preferred in HA add-ons for smaller image size and stability
RUN apk add --no-cache \
    python3 \
    py3-flask \
    py3-psutil \
    py3-pillow \
    py3-yaml \
    py3-requests \
    py3-gevent \
    py3-tz \
    py3-cryptography \
    openssl \
    ca-certificates \
    ttf-dejavu \
    font-noto

COPY ./src /app

# Debug: List the contents of /app to verify the copy
RUN ls -l /app

WORKDIR /app

# Link the configuration and data directories to the HA /data partition
RUN mkdir -p /data/db /data/logs /data/ssl && \
    ln -sf /data/options.json /app/config.yaml && \
    ln -sf /data/db /app/db && \
    ln -sf /data/logs /app/logs && \
    ln -sf /data/ssl /app/ssl

# Expose port 83 for the TRMNL API
EXPOSE 83

# Start the server
CMD ["/usr/bin/python3", "trmnl_server.py"]