#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    key = data.data
    if key.lower() == 'f':
        print("\n EMERGENCY \n Sending signal to shut down AUV")
        rospy.signal_shutdown("Shutdown requested by user")

def keyboard_input_subscriber():
    rospy.init_node('keyboard_input_subscriber')
    rospy.Subscriber('keyboard_input', String, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        keyboard_input_subscriber()
    except rospy.ROSInterruptException:
        pass
