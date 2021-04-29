#!/usr/bin/env python3

import rospy
from person.msg import Person

def callback(msg):
    print(f"Name: {msg.name}, Age: {msg.age}, Address: {msg.address}")

rospy.init_node("person_subscriber")
sub = rospy.Subscriber('person', Person,callback)

# keeps running until rosnode is shut down
rospy.spin()