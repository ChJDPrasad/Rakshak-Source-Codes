#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from mavros_msgs.msg import OverrideRCIn
global pub

def JoytoPWM(Joy):
	rc_msg = OverrideRCIn()
	rc_msg.channels[0] = 1500 + 500*Joy.axes[3]    # Aileron       #3
	rc_msg.channels[1] = 1500 + 500*Joy.axes[0]    # Elevator      #0
	rc_msg.channels[2] = 1500 + 500*Joy.axes[1]    # Trottle       #1
	rc_msg.channels[3] = 1500 + 500*Joy.axes[4]    # Rudder        #4
	rc_msg.channels[5] = 1500 + 500*Joy.axes[5]    # switch C      #5
	rc_msg.channels[6] = 2000 - 1000*Joy.buttons[2] # switch B      #2
	rc_msg.channels[7] = 2000 - 1000*Joy.buttons[3] # switch A      #3
	
	pub.publish(rc_msg)

if __name__ == '__main__':
	rospy.init_node('listener', anonymous=True)
	pub = rospy.Publisher('PWM',OverrideRCIn,queue_size=10)	
	rospy.Subscriber("joy", Joy, JoytoPWM)
	#print('after subs: %s',Joy)
	rospy.spin()
