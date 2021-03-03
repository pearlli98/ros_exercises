#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
from ros_exercises.msg import OpenSpace

rospy.init_node('open_space_publisher', anonymous = False)
# pub1 = rospy.Publisher('open_space/distance', Float32, queue_size = 20)
# pub2 = rospy.Publisher('open_space/angle', Float32, queue_size = 20)
pub = rospy.Publisher('open_space', OpenSpace, queue_size=20)

def callback(data):
    m = max(data.ranges)
    a = data.angle_max + data.ranges.index(m) * data.angle_increment
    os = OpenSpace()
    os.angle = a
    os.distance = m
    pub.publish(os)
    # pub1.publish(Float32(m))
    # pub2.publish(Float32(a))
    rospy.loginfo(data.ranges.index(m))

def open_space():
    sub = rospy.Subscriber('fake_scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    open_space()

