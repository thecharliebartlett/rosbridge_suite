#!/bin/bash  
# Json test Script       

echo Testing Json Client

xterm -e roslaunch rosbridge_server rosbridge_tcp.launch &
sleep 15
echo Server Up
xterm -e rosrun rospy_tutorials add_two_ints_server &
sleep 2
python JSONTestClient.py
killall -9 roslaunch
killall -9 xterm

