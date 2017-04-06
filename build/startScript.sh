#!/bin/bash
flic/flicd -f /flic/persistence/flic.sqlite3  & 
python3 flic/flic_mqtt_service.py $MQTT_HOST $MQTT_PORT $MQTT_USERNAME $MQTT_PASSWORD $FLIC_TOPIC
