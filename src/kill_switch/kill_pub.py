#!/usr/bin/env python

import rospy
import sys
import tty
import termios
from std_msgs.msg import String

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def keyboard_input_publisher():
    rospy.init_node('keyboard_input_publisher')
    pub = rospy.Publisher('keyboard_input', String, queue_size=10)

    try:
        while not rospy.is_shutdown():
            key = getch()
            msg = String()
            msg.data = key
            pub.publish(msg)
    except rospy.ROSInterruptException:
        pass

if __name__ == "__main__":
    try:
        keyboard_input_publisher()
    except rospy.ROSInterruptException:
        pass
