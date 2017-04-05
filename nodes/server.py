#!/usr/bin/env python

# url: http://wiki.ros.org/dynamic_reconfigure/Tutorials/SettingUpDynamicReconfigureForANode%28python%29
import rospy

from dynamic_reconfigure.server import Server
from arduino_msgs.cfg import LI3DSArduinoConfig

def callback(config, level):
    rospy.loginfo("""Reconfigure Request: {camlight_time_between_pics}""".format(**config))
    return config

if __name__ == "__main__":
    rospy.init_node("arduino_msgs", anonymous=True)

    srv = Server(LI3DSArduinoConfig, callback)
    rospy.spin()
