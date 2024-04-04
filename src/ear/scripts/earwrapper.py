#!/usr/bin/env python
'''
import rospy
#from ear import move #yet to be implemented
from std_msgs.msg import String

"""
Pi Servo module.
"""
import time 

import RPi.GPIO as GPIO 

#subscriber to a topic that takes in an angle for both servos and translates into pwm value
#be in package whenever pushing
class earwrapper:

    #TODO: set minimum and maximum constraints

    #ROM 90 degrees
    #left ear:

    #min 3
    #max 6
    #3 is straight upward
    #6 is pointing outwards towards the left

    #right ear:
    #4.5 towards the left
    #max 3.5
    #3.5 is straight upwards
    #2 is pointing outwards towards the right
    def move(self, emotion):
        
        
        self.servo1.start(0) #TODO: have it be both servos

        print("Spinning")

        # Test the full range of movement. Note only integers are allowed.
        # 12=180 degrees, 6 is around 90 degrees
        #although it's not specificed what it'll do in documentation
        # a past problem with this code was that it wasn't clear how to change directions but maybe it'll work differently this time
        #for x in range(2, 6):
        #    self.servo1.ChangeDutyCycle(x)
        #    time.sleep(0.5)
        
        # Start over and move in bigger, slower movements.
        #servo1.ChangeDutyCycle(2)
        #time.sleep(1)
        #servo1.ChangeDutyCycle(6)
        #time.sleep(1)
        
    
        #self.servo1.stop() #have it after every call to move, or at the very end? Will have to re-initialize every time

     #ear twitch every once and a while
    def callback_twitch(self, event): #TODO: ensure the servo is started first
        #suppose center is at 6
        self.servo1.ChangeDutyCycle(6.5)
        time.sleep(0.1)
        self.servo1.ChangeDutyCycle(6)
        time.sleep(.1)
    
    def callback_emotion(self, msg):
        #if the emotion equals a certain thing, call corresponding function that does the movement
        print(msg.data)
        if(msg.data == "smirk"):
            self.move("smirk")
        elif(msg.data == "smile"):
            self.move("smile")

    def stop(self):
        self.servo1.stop()
        self.servo2.stop()
        GPIO.cleanup()

    def __init__(self):
        rospy.Subscriber("Shown_personality", String, self.callback_emotion)

        #rospy.Timer(30, self.callback_twitch, oneshot=False) #ear twitch

        OUT_PIN_1 = 12 #left ear (view from back of head)
        OUT_PIN_2 = 6 #right ear 
        PULSE_FREQ = 50

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(OUT_PIN_1, GPIO.OUT)  #TODO:only one servo so far, might test with one servo to make sure they don't collide
        GPIO.setup(OUT_PIN_2, GPIO.OUT)

        self.servo1 = GPIO.PWM(OUT_PIN_1, PULSE_FREQ) 
        self.servo2 = GPIO.PWM(OUT_PIN_2, PULSE_FREQ) 
    

if __name__ == "__main__":
    rospy.init_node("ear_node")
    ear_wrapper = earwrapper()
    rospy.on_shutdown(ear_wrapper.stop())
    
    #rospy.on_shutdown(ear_wrapper.stop()) #don't know if needed but stop method might be useful
    rospy.loginfo("Ear driver is now started, ready to get commands.")
    rospy.spin()
'''