#!/usr/bin/env python3

import rospy
from basics.srv import AddTwoPoints,AddTwoPointsResponse

rospy.init_node("addtwopoints_server")

# when you recieve a request run the code below
def callback(request):
    sum = request.x + request.y
    return AddTwoPointsResponse(sum)

server = rospy.Service('sum',AddTwoPoints,callback)
rospy.spin()