#!/usr/bin/env python

import sys
sys.path.append('/flic/fliclib')
import fliclib
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import threading


mqtt_host = sys.argv[1] 
mqtt_username = sys.argv[3]
mqtt_password= sys.argv[4] 
mqtt_port= int(sys.argv[2])
start_topic= sys.argv[5]
client = fliclib.FlicClient("localhost")

def got_button(bd_addr):
    cc = fliclib.ButtonConnectionChannel(bd_addr)
    cc.on_button_single_or_double_click_or_hold = \
        lambda channel, click_type, was_queued, time_diff: \
            my_publish(start_topic+channel.bd_addr.replace(":",""),str(click_type).replace("ClickType.",""))
    cc.on_connection_status_changed = \
        lambda channel, connection_status, disconnect_reason: \
            print(channel.bd_addr + " " + str(connection_status) + (" " + str(disconnect_reason) if connection_status == fliclib.ConnectionStatus.Disconnected else ""))
    client.add_connection_channel(cc)

def got_info(items):
    print(items)
    for bd_addr in items["bd_addr_of_verified_buttons"]:
        got_button(bd_addr)

def my_publish(topic, message):
    publish.single(topic, payload=message, qos=0, retain=False, hostname=mqtt_host, port=mqtt_port, client_id="flic", keepalive=60, will=None, auth= {'username':mqtt_username, 'password':mqtt_password}, tls=None, protocol=mqtt.MQTTv31)

client.get_info(got_info)
client.on_new_verified_button = got_button
client.handle_events()
