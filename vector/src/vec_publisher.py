#!/usr/bin/env python3
import rospy
from vector.msg import Vector
from random import randint

rospy.init_node("vec_publisher")
pub = rospy.Publisher("vec",Vector)
rate = rospy.Rate(2)
while not rospy.is_shutdown():
    v = Vector()
    x = randint(0,50)
    y = randint(0,50)
    v.x = x
    v.y = y
    pub.publish(v)
    rate.sleep()
    