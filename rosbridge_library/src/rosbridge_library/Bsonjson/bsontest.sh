#!/bin/bash  
# Bson test Script       

echo Testing Bson Client

xterm -e roslaunch rosbridge_server rosbridge_tcp.launch bson_only_mode:=True &
sleep 15
echo Server Up
xterm -e rosrun rospy_tutorials add_two_ints_server &
sleep 2
python BSONTestClient.py
sleep 10
killall -9 roslaunch
killall -9 xterm
