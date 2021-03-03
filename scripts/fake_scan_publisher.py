#!/usr/bin/env python

import rospy
import random
import math
from sensor_msgs.msg import LaserScan

def fake_scan():
    pub = rospy.Publisher('fake_scan', LaserScan, queue_size = 20)
    rospy.init_node('fake_scan_publisher', anonymous = False)
    rate = rospy.Rate(20)

    last_time = rospy.Time.now()
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        #make a LaserScan
        scan = LaserScan()

        scan.header.stamp = current_time
        scan.header.frame_id = 'base_link'
        scan.angle_min = -2.0/3.0 * math.pi
        scan.angle_max = 2.0/3.0 * math.pi
        scan.angle_increment = 1.0/300.0 * math.pi
        scan.scan_time = (current_time - last_time).to_sec()
        scan.range_min = 1
        scan.range_max = 10

        scan.ranges = []
        for i in range(401):
            scan.ranges.append(random.uniform(1, 10))  # fake data

        #publish the data     
        pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_scan()
    except rospy.ROSInterruptException:
        pass

