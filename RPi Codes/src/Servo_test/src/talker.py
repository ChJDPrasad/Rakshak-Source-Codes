#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import Int64




def talker(value):
    pub = rospy.Publisher('chatter', Int64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    hello_int = value
    rospy.loginfo(hello_int)
    pub.publish(hello_int)
    rate.sleep()

if __name__ == '__main__':


    value = input('Enter a value: ')
    while(value != 0):
        try:
            talker(value)
        except rospy.ROSInterruptException:
            pass
        value = input('Enter a value: ')
