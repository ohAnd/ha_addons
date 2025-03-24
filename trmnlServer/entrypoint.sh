#!/bin/sh
set -e

SHARED_FOLDER="/app/addon_config"
CONFIG_FOLDER="/app"

CONFIG_FILE="$CONFIG_FOLDER/config.yaml"
CONFIG_FILE_SHARED="$SHARED_FOLDER/config.yaml"
CONFIG_FILE_HA="/data/options.json"


# use custom config file, if available
if test -e $CONFIG_FILE_SHARED ; then
  echo "Using Config file found in addon config folder."
  ln -sf $CONFIG_FILE_SHARED $CONFIG_FILE
else if test -e $CONFIG_FILE_HA ; then
  echo "Config file tmrnlServer_config.yaml not found in addon config folder. Proceeding with data from HA Addon configuration"
  ln -sf $CONFIG_FILE_HA $CONFIG_FILE
else
  echo "Config file tmrnlServer_config.yaml not found in addon config folder. Proceeding with default configuration"
fi
fi

# Start trmnl_server.py
exec python trmnl_server.py /app/addon_config
