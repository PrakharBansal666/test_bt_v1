#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

def marker_detected_callback(data):
    if data.data:
        rospy.loginfo("ArUco marker detected")
    else:
        rospy.sleep(5)
        rospy.loginfo("ArUco marker not detected \n switching to ROV mode")

def aruco_subscriber():
    rospy.init_node('aruco_subscriber')
    rospy.Subscriber('aruco_marker_detected', Bool, marker_detected_callback)
    rospy.spin()

if __name__ == '__main__':
    aruco_subscriber()

