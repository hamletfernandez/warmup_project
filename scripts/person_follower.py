#!/usr/bin/env python3
import rospy
import numpy as np

from geometry_msgs.msg import Vector3, Twist, TwistStamped
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header

import tf
from tf.transformations import quaternion_from_euler, euler_from_quaternion

#The structure of this code was copied from spin_in_circles
class PersonFollower(object):
    """ This node publishes ROS messages containing the 3D coordinates of a single point """

    def __init__(self):
        rospy.init_node('person_follower')
        self.follow_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/scan', LaserScan, self.robot_scan_received)


        self.move = rospy.Publisher('/cmd_vel', Twist , queue_size=10)

        self.forwardSpeed = 0.2
        self.turnSpeed = 0.2

        # Movement Commands
        _forwardCommand = Twist()
        _forwardCommand.linear.x = self.forwardSpeed

        self.forwardCommand = _forwardCommand # initialize a Forward commend

        _turnLeftCommand = Twist()
        _turnLeftCommand.angular.z = self.turnSpeed

        self.turnLeftCommand = _turnLeftCommand # initialize a turn command


        _turnRightCommand = Twist()
        _turnRightCommand.angular.z = (-1) * self.turnSpeed

        self.turnRightCommand = _turnRightCommand # initialize a turn command              

        _stopCommand = Twist()

        self.stopCommand = _stopCommand # initialize a stop command


    def robot_scan_received(self, data):
        #print(data.ranges)

        forward_range_min = np.pi  / (4 * data.angle_increment)
        forward_range_max = ((2 * np.pi) / data.angle_increment) - forward_range_min

        print (data.ranges[int(forward_range_min):int(forward_range_max)])

        '''
        if(cx > w / 2 + self.x_error):
            self.move.publish(self.turnLeftCommand)
        elif (cx < w/2 - self.x_error):
            self.move.publish(self.turnRightCommand)
        else:
            self.move.publish(self.forwardCommand)
            '''



    def run(self):
        my_header = Header(stamp=rospy.Time.now(), frame_id="odom")
        my_twist = Twist(linear = Vector3(x=0.0, y=0.0, z=0.0), angular = Vector3(x=0.0, y=0.0, z=0.0))
        my_twist_stamped = TwistStamped(header=my_header, twist=my_twist)
        r = rospy.Rate(2)
        while not rospy.is_shutdown():

            my_twist_stamped.header.stamp = rospy.Time.now()
            self.follow_pub.publish(my_twist)


if __name__ == '__main__':
    node = PersonFollower()
    node.run()