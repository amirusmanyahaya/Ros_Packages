#!/usr/bin/env python3
import rospy
import sys
from basics.srv import AddTwoPoints

rospy.init_node("addtwopoints_client")

x = int(sys.argv[1])
y = int(sys.argv[2])

client = rospy.ServiceProxy('sum',AddTwoPoints)
print(f"the sum of {x} and {y} is {client(x,y)}")