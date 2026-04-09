#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import PoseStamped

class ACNCore:
    def __init__(self):
        rospy.init_node('acn_core', anonymous=True)
        rospy.loginfo("ACN Core Initialized — Signal Independent Navigation")
        
        self.imu_sub = rospy.Subscriber('/imu/data', Imu, self.imu_callback)
        self.pose_pub = rospy.Publisher('/acn/pose', PoseStamped, queue_size=10)
        self.rate = rospy.Rate(100)
        rospy.loginfo("ACN Ready — Zero external dependencies")

    def imu_callback(self, msg):
        pose = PoseStamped()
        pose.header.stamp = rospy.Time.now()
        pose.header.frame_id = "world"
        self.pose_pub.publish(pose)

    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == '__main__':
    acn = ACNCore()
    acn.run()
