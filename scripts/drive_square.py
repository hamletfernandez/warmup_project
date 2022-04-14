#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Vector3, Twist, TwistStamped
from std_msgs.msg import Header

#The structure of this code was copied from spin_in_circles
class DriveInSquare(object):
    """ This node publishes ROS messages containing the 3D coordinates of a single point """

    def __init__(self):
        rospy.init_node('drive_in_square')
        self.spin_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # this function will alter the turtlebot's rotation
    # and will be called every 10 seconds using rospy.Timer()
    # First it will stop the linear momentum for 5 seconds then 
    # continue 
    def turn(self, twist):
        tmp = twist.linear.x
        twist.linear.x = 0.0
        twist.angular.z = 0.25
        print(twist.linear.x, twist.angular.z)
        rospy.sleep(rospy.Duration(3, 0))
        twist.linear.x = tmp
        print(twist.linear.x, twist.linear.z)

    def run(self):
        my_header = Header(stamp=rospy.Time.now(), frame_id="odom")

        my_twist = Twist(linear = Vector3(x=0.1, y=0.0, z=0.0), angular = Vector3(x=0.0, y=0.0, z=0.0))
        my_twist_stamped = TwistStamped(header=my_header, twist=my_twist)
        r = rospy.Rate(2)
        while not rospy.is_shutdown():
            my_twist.linear.x = 0.4
            my_twist.angular.z = 0.0 
            my_twist_stamped.header.stamp = rospy.Time.now()
            self.spin_pub.publish(my_twist)
            rospy.sleep(rospy.Duration(3,0))
            my_twist.linear.x = 0.0
            my_twist.angular.z = 0.5
            self.spin_pub.publish(my_twist)
            rospy.sleep(rospy.Duration(3,0))
            #self.turn(my_twist)

if __name__ == '__main__':
    node = DriveInSquare()
    node.run()