#!/usr/bin/env python3
import rospy
from person.msg import Person
from random import randint

def set_attribute(object):
    object.name = "Person" + str(randint(0,10))
    object.age = randint(1,60)
    object.address = "Rydsvagen 248 C" + str(randint(30,38))

# initialize node
rospy.init_node("person_publisher")

pub = rospy.Publisher('person',Person)

# setting the rate to publish message
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    person = Person()
    set_attribute(person)
    pub.publish(person)
    rate.sleep()



