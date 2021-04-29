#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys

robot_x = 0

def callback(pose):
    global robot_x
    rospy.loginfo(f"Robot X: {pose.x}")
    robot_x = pose.x
    
def move(lin_vel, ang_vel, distance):
    global robot_x
    rospy.init_node("move_turtle")
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist)
    sub = rospy.Subscriber('/turtle1/pose', Pose, callback)
    rate = rospy.Rate(10) #10hz

    velocity = Twist()
    while not rospy.is_shutdown():
        velocity.linear.x = lin_vel
        velocity.linear.y = 0
        velocity.linear.z = 0
        velocity.angular.x = 0
        velocity.angular.y = 0
        velocity.angular.z = ang_vel
        rospy.loginfo(f"linear velocity: {velocity.linear.x}, angular velocity: {velocity.angular.z}")
        pub.publish(velocity)
        rate.sleep()
        if robot_x >= distance:
            velocity.linear.x = 0
            velocity.linear.y = 0
            rospy.loginfo("stopping robot")
            break

if __name__ == '__main__':
    try:
        linear_vel, angular_vel,distance = (float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
        move(linear_vel,angular_vel,distance)
    except rospy.ROSInterruptException:
        pass