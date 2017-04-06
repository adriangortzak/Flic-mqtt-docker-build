#!/bin/bash
./build.sh
docker stop flic
docker rm flic

docker run -d --net=host --privileged --name flic \
  --env 'MQTT_HOST=127.0.0.1' \
  --env 'MQTT_PORT=1883' \
  --env 'MQTT_USERNAME=test' \
  --env 'MQTT_PASSWORD=test'  \
  -v /srv/flic/data:/flic/persistence \
	 adddrian/flic
