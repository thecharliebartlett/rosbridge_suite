A python test client which demonstrates the communication with ROSBridge.
This is bash script to test BSON/JSON client connection.  Using the python test from https://github.com/Sanic/ROSBridgeTestclient/blob/master/BSONTestClient.py


## How to use 

Wrote 2 Scripts to test the BSON and JSON

##Relevant notes:
- Tested with Python 2.7
- The client assumes that your rosbridge server is running on localhost:9090
- Edited this orignal ( see https://github.com/Sanic/ROSBridgeTestclient/blob/master/BSONTestClient.py#L16 ).
- For demonstration purposes, the client calls the add_two_ints service. Make sure to have ros-Version-rospy-tutorial installed
