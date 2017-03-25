#!/usr/bin/env python
# license removed for brevity


import RPi.GPIO as GPIO
import rospy
import time
from std_msgs.msg import Int64

# Set the servo pin no
servo_pin = 7
# Set the motor pin no
#motor_pin = 11

#Setting up GPIO Board

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)
#GPIO.setup(motor_pin, GPIO.OUT)

# PWM Output function
def pwm(position, pin):
    value_high = position * 1e-6
    value_low = 0.02 - value_high
	count = 0    
	while (count < 10):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(value_high)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(value_low)
		count = count +1

def controller(data):
	pwm(data.data, servo_pin)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Int64, controller)
    rospy.spin()


if __name__ == "__main__":
    value = 1500
    pwm(value, servo_pin)
	listener()    
	#motor(value, motor_pin)

