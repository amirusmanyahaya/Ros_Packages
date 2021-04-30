#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
import sys
import math


x = 0.0
y = 0.0
yaw = 0.0
# using pose to update the distance covered
def callback(pose):
    global x, y, yaw
    x = pose.x
    y = pose.x
    yaw = pose.theta

def move(velocity_publisher,speed,stop_x,is_forward):
    global x
    velocity = Twist()
    if is_forward:
        velocity.linear.x = speed
    else:
        velocity.linear.x = 1.0 - speed
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        velocity_publisher.publish(velocity)
        rate.sleep()
        if x >= stop_x:
            rospy.loginfo("Gotten to my destination")
            break
def rotate(velocity_publisher,ang_speed,rotation_ang, clockwise):
    velocity = Twist()
    # convert to radians    
    ang_speed = math.radians(ang_speed)
    if clockwise:
        velocity.angular.z = 1 - ang_speed
    else:
        velocity.angular.z = ang_speed
    
    rate = rospy.Rate(10)
    t0 = rospy.Time().now().to_sec()
    while not rospy.is_shutdown():
        velocity_publisher.publish(velocity)
        rate.sleep()
        t1 = rospy.Time().now().to_sec()
        current_angle = (t1 - t0) * ang_speed
        if current_angle > math.radians(rotation_ang):
            rospy.loginfo("rotated to the destination")
            break
    velocity.angular.z = 0.0
    velocity_publisher.publish(velocity)

def move_to_point(publisher, end_x, end_y):
    global x, y, yaw
    velocity = Twist()

    K_linear = 0.5
    K_angular = 4.0

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        distance = math.sqrt((end_x - x)**2 + (end_y - y)**2)
        linear_speed = distance * K_linear
        desired_ang = math.atan2(end_y - y, end_x - x)
        angular_speed = (desired_ang-yaw) * K_angular

        velocity.linear.x = linear_speed
        velocity.angular.z = angular_speed

        publisher.publish(velocity)
        rate.sleep()

        rospy.loginfo(f"distance: {distance}, x: {x}, y: {y}, yaw: {yaw}")

        if(distance < 0.01):
            break

def set_desired_orientation(publisher, speed,direction):
    global yaw
    relative_ang = math.radians(direction) - yaw

    if relative_ang < 0 :
        clockwise = True
    else:
        clockwise = False
    
    relative_ang = math.degrees(abs(relative_ang))

    rotate(publisher, speed, relative_ang, clockwise)

def spiral_movement(publisher, lin_speed, ang_speed,desired_x, desired_y):
    global x,y

    velocity = Twist()

    rate = rospy.Rate(1)
    while x < desired_x and y < desired_y:
        lin_speed = lin_speed + 1
        velocity.linear.x = lin_speed
        velocity.angular.z = ang_speed
        publisher.publish(velocity)
        rate.sleep()


if __name__ == '__main__':
    try:
        rospy.init_node("turtlesim_cleaner")
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
        # speed,stop_x = (float(sys.argv[1]),float(sys.argv[2]))
        rospy.Subscriber('/turtle1/pose', Pose, callback)
        rospy.sleep(2)
        move(velocity_publisher, 3.0 , 7.0, is_forward=True)
        rotate(velocity_publisher, 5.0, 180, clockwise=False)
        move_to_point(velocity_publisher,3.0, 3.0)
        spiral_movement(velocity_publisher, 0.0, 2.0, 9.5, 9.5)
        set_desired_orientation(velocity_publisher, 10.0, 90)
    except rospy.ROSInterruptException:
        pass