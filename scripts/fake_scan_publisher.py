#!/usr/bin/env python

import rospy
import random
import math
from sensor_msgs.msg import LaserScan

def fake_scan():
    
    rospy.init_node('fake_scan_publisher', anonymous = False)

    pub = rospy.Publisher(rospy.get_param("publish_topic", "fake_scan"), LaserScan, queue_size = 20)
    rate = rospy.Rate(rospy.get_param("publish_rate", 20))
    last_time = rospy.Time.now()
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        #make a LaserScan
        scan = LaserScan()

        scan.header.stamp = current_time
        scan.header.frame_id = 'base_link'
        scan.angle_min = rospy.get_param("angle_min", -2.0/3.0 * math.pi)
        scan.angle_max = rospy.get_param("angle_max", 2.0/3.0 * math.pi)
        scan.angle_increment = rospy.get_param("angle_increment", 1.0/300.0 * math.pi)
        scan.scan_time = (current_time - last_time).to_sec()
        scan.range_min = rospy.get_param("range_min", 1)
        scan.range_max = rospy.get_param("range_max", 10)

        scan.ranges = []
        for i in range(401):
            scan.ranges.append(random.uniform(scan.range_min, scan.range_max))  # fake data

        #publish the data     
        pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_scan()
    except rospy.ROSInterruptException:
        pass

