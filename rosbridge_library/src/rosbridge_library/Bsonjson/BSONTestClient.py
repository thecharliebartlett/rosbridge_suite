# TCP communication adapted from https://wiki.python.org/moin/TcpCommunication#Client

import bson
import json
import time
import socket
import pprint


print("BSON-ROSBridge Testclient")

BSON = "BSON"


TEST_MODE = BSON

TCP_IP = '127.0.0.1'
TCP_PORT = 9090
BUFFER_SIZE = 4096

def encode_message(msg):
        return bson.BSON.encode(msg)

def decode_message(msg):
        bson_message = bson.BSON(data)
        return bson_message.decode()


# Prepare the messages to be sent
# This includes:
#  - Advertising a topic
#  - Publishing to it
#  - Sending a service request

advertise_msg = {
  "op": "advertise",
  "topic": "/bson_test",
  "type": "std_msgs/String"
}
my_message = {
    "data" : "Hello from BSON-ROSBridge Testclient: "
}
my_message["data"]+="BSON Mode."

pub_msg = {
  "op": "publish",
  "topic": "/bson_test",
  "msg": my_message
}

call_service_params = {
    "a" : 20,
    "b" : 22
}

call_service_msg = {
  "op": "call_service",
  "service": "/add_two_ints",
  "args": call_service_params
}

# TCP communication
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

print("Sending BSON data")
s.send(encode_message(advertise_msg))
s.send(encode_message(pub_msg))
s.send(encode_message(call_service_msg))

data = s.recv(BUFFER_SIZE)
print("Received BSON response :")
pprint.pprint( decode_message(data))

s.close()
