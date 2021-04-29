#!/usr/bin/env python3
import rospy
from basics.srv import WordCount, WordCountResponse

rospy.init_node("server_service")

def count_words(request):
    return WordCountResponse(len(request.words.split()))

# advertise the service
service = rospy.Service("word_count", WordCount, count_words)
rospy.spin()