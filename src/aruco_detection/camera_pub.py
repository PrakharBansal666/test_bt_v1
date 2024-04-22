#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraPublisher:
    def __init__(self):
        rospy.init_node('camera_publisher')
        self.bridge = CvBridge()
        self.image_pub = rospy.Publisher('camera/image_raw', Image, queue_size=10)
        self.camera = cv2.VideoCapture(0)

    def publish_image(self):
        rate = rospy.Rate(10)  # 10Hz
        while not rospy.is_shutdown():
            ret, frame = self.camera.read()
            if ret:
                msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
                self.image_pub.publish(msg)
            rate.sleep()

if __name__ == '__main__':
    try:
        publisher = CameraPublisher()
        publisher.publish_image()
    except rospy.ROSInterruptException:
        pass
