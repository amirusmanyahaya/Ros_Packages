#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node("talker_pub")

pub = rospy.Publisher("talker",String)

rate = rospy.Rate(2)
while not rospy.is_shutdown():
    pub.publish("I love her")
    rate.sleep()