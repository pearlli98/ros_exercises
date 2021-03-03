#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float32

rospy.init_node('simple_subscriber', anonymous = False)
pub = rospy.Publisher('random_float_log', Float32, queue_size = 20)

def callback(data):
    rospy.loginfo("I heard %f", data.data)
    rospy.loginfo("I published %f", math.log(data.data))
    pub.publish(Float32(math.log(data.data)))

def random_num_listener():
    sub = rospy.Subscriber('my_random_float', Float32, callback)
    rospy.spin()

if __name__ == '__main__':
    random_num_listener()

