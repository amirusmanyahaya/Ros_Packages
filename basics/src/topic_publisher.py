#!/usr/bin/env python3
import rospy
from basics.msg import Complex
from random import random

# initializing a rosnode with a name topic_publisher
rospy.init_node("topic_publisher")
# creating an instance of a publisher with a a message named counter
# and a type of Int 32
pub = rospy.Publisher("couter",Complex)

# specifying the rate to publish the message
rate = rospy.Rate(2)
while not rospy.is_shutdown():
    msg = Complex()
    msg.real = random()
    msg.imaginary = random()
    pub.publish(msg)
    rate.sleep()