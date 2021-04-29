#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

rospy.init_node("listener_sub")

def callback(msg):
    print("I heard ",msg.data)

sub = rospy.Subscriber("talker",String,callback)
rospy.spin()