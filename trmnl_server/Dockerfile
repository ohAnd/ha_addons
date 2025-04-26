ARG BUILD_FROM
FROM $BUILD_FROM

# Copy data for add-on
RUN apk add --no-cache \
            python3 \
            py3-flask \
            py3-psutil \
            py3-pillow \
            py3-yaml \
            py3-requests \
            py3-gevent \
            py-tz \
            openssl \
            ca-certificates \
            ttf-dejavu

COPY ./src /app
# Debug: List the contents of /app and /app/src to verify the copy
RUN ls -l /app

WORKDIR /app
# Link the configuration file
RUN mkdir -p /data/db /data/logs /data/ssl && \
    ln -sf /data/options.json /app/config.yaml && \
    ln -sf /data/db /app/db && \
    ln -sf /data/logs /app/logs && \
    ln -sf /data/ssl /app/ssl

# Expose port 83 for the website
EXPOSE 83

# Set the command to start the container
CMD ["/usr/bin/python3", "trmnl_server.py"]