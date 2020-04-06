#! /usr/bin/env python

import rospy 
import rospkg 
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState
import time

class Person_trajectory:

    def __init__(self):
        self.state_msg = ModelState()
        self.state_msg.model_name = 'person'
        self.state_msg.pose.position.x = 1
        self.state_msg.pose.position.y = 2
        self.state_msg.pose.position.z = 0
        self.state_msg.pose.orientation.x = 0
        self.state_msg.pose.orientation.y = 0
        self.state_msg.pose.orientation.z = 0
        self.state_msg.pose.orientation.w = 0

    def state(self,point):
        self.state_msg.pose.position.x = point[0]
        self.state_msg.pose.position.y = point[1]
        self.state_msg.pose.orientation.z = point[2]

    def main(self):
        rospy.init_node('set_pose')
        points = [(0,0,0),(0,0.5,0),(0,1,0),(0.5,1,0),(1,1,0),(1,0.5,0),(1,0,0),(0.5,0,0),(0,0,0)]
        for point in points:
            self.state(point)
            rospy.wait_for_service('/gazebo/set_model_state')
            try:
                set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
                resp = set_state( self.state_msg )
                rospy.loginfo(point)

            except rospy.ServiceException, e:
                print "Service call failed: %s" % e
            time.sleep(0.5)

if __name__ == '__main__':
    try:
        person = Person_trajectory()
        person.main()
    except rospy.ROSInterruptException:
        pass
