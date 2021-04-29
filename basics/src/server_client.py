#!/usr/bin/env python3

import rospy
from basics.srv import WordCount
import sys

rospy.init_node("server_client")

# wait for service to be advertised
rospy.wait_for_service("word_count")

# allows the creation of proxy and used like a local variable
word_counter = rospy.ServiceProxy('word_count',WordCount)

words = ' '.join(sys.argv[1:])
word_count = word_counter(words)
print(words, " -> " , word_count)