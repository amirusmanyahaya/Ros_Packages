#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
import sys
import math


distance = 0.0
theta = 0.0
# using pose to update the distance covered
def callback(pose):
    global distance, theta
    distance = pose.x
    theta = pose.theta

def move(velocity_publisher,speed,stop_x,is_forward):
    global distance
    velocity = Twist()
    if is_forward:
        velocity.linear.x = speed
    else:
        velocity.linear.x = 1.0 - speed
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        velocity_publisher.publish(velocity)
        rate.sleep()
        if distance >= stop_x:
            rospy.loginfo("Gotten to my destination")
            break
def rotate(velocity_publisher,ang_speed,rotation_ang, clockwise):
    global theta
    velocity = Twist()
    # convert to radians    
    ang_speed = math.radians(ang_speed)
    if clockwise:
        velocity.angular.z = 1 - ang_speed
    else:
        velocity.angular.z = ang_speed
    
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        velocity_publisher.publish(velocity)
        rate.sleep()
        if theta >= math.radians(rotation_ang):
            rospy.loginfo("rotated to the destination")
            break

if __name__ == '__main__':
    try:
        rospy.init_node("turtlesim_cleaner")
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
        # speed,stop_x = (float(sys.argv[1]),float(sys.argv[2]))
        rospy.Subscriber('/turtle1/pose', Pose, callback)
        rospy.sleep(2)
        # move(velocity_publisher, speed , stop_x, is_forward=True)
        rotate(velocity_publisher, 5.0, 180, clockwise=False)
    except rospy.ROSInterruptException:
        pass