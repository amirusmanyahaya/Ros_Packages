#!/usr/bin/env python3
import rospy
from basics.msg import Complex

rospy.init_node("topic_subscriber")

def callback(message):
    print('Real number: ', message.real)
    print('Imaginary number: ', message.imaginary)

sub = rospy.Subscriber('couter',Complex,callback)
rospy.spin()