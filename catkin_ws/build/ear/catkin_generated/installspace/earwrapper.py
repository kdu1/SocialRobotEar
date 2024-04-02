#!/usr/bin/env python3
import rospy
#from ear import move #yet to be implemented
from std_msgs.msg import String

"""
Pi Servo module.
"""
import time 

import RPi.GPIO as GPIO 



class earwrapper:

    def move(emotion):
        
        
        servo1.start(0) 

        print("Spinning")

        # Test the full range of movement. Note only integers are allowed.
        # 12=180 degrees, 6 is around 90 degrees
        #although it's not specificed what it'll do in documentation
        # a past problem with this code was that it wasn't clear how to change directions but maybe it'll work differently this time
        for x in range(2, 6):
            servo1.ChangeDutyCycle(x)
            time.sleep(0.5)
        
        # Start over and move in bigger, slower movements.
        #servo1.ChangeDutyCycle(2)
        #time.sleep(1)
        #servo1.ChangeDutyCycle(6)
        #time.sleep(1)
        
    
        
        servo1.stop() 
        GPIO.cleanup()

     #ear twitch every once and a while
    def callback_twitch(event): #TODO: ensure the servo is started first
        #suppose center is at 6
        servo1.ChangeDutyCycle(6.5)
        time.sleep(0.1)
        servo1.ChangeDutyCycle(6)
        time.sleep(.1)
    
    def callback_emotion(self, msg):
        #if the emotion equals a certain thing, call corresponding function that does the movement
        print(msg.data)
        if(msg.data == "smirk"):
            move("smirk")
        elif(msg.data == "smile"):
            move("smile")

    def __init__(self):
        rospy.Subscriber("Shown_personality", String, self.callback_emotion)

        rospy.Timer(30, callback_twitch, oneshot=False) #ear twitch
        #self.ear = main()
    #def stop(self):
        #self.ear.stop()

    

        
if __name__ == "__main__":
    rospy.init_node("ear_node")
    ear_wrapper = earwrapper()
    OUT_PIN = 12 #one of the ears
    PULSE_FREQ = 50

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(OUT_PIN, GPIO.OUT) 

    servo1 = GPIO.PWM(OUT_PIN, PULSE_FREQ) 

    #rospy.on_shutdown(ear_wrapper.stop()) #don't know if needed but stop method might be useful
    rospy.loginfo("Ear driver is now started, ready to get commands.")
    rospy.spin()