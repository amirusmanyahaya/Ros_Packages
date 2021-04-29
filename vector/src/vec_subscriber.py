#!/usr/bin/env python3
import rospy
from vector.msg import Vector

rospy.init_node("vec_subscriber")
def callback(msg):
    print("The vector is : ")
    print(f"[{msg.x},{msg.y}]")
sub = rospy.Subscriber("vec",Vector,callback)
rospy.spin()