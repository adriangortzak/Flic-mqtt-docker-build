FROM ubuntu:14.04

RUN apt-get update -y && \
  apt-get install bluez bluez-utils -y

RUN apt-get install python3-pip -y && \
   pip3  install paho-mqtt

ENV FLIC_TOPIC trigger/flic/
ENV MQTT_HOST test.com
ENV MQTT_PORT 1883
ENV MQTT_USERNAME username 
ENV MQTT_PASSWORD password
COPY add_button.py /flic/add_button.py
COPY flic_mqtt_service.py /flic/flic_mqtt_service.py
COPY fliclib.py /flic/fliclib.py
COPY startScript.sh /startScript.sh
COPY flicd /flic/flicd
RUN mkdir -p /flic/persistence

CMD /startScript.sh
