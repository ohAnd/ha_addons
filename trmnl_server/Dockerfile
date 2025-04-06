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
COPY entrypoint.sh /app

WORKDIR /app
RUN ln -sf /data/options.json /app/config.yaml

# Expose port 83 for the website
EXPOSE 83

CMD [ "/bin/sh", "/app/entrypoint.sh" ]