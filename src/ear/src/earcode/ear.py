"""
Pi Servo module.
"""

import rospy
import time 
#import RPi.GPIO as GPIO 
from std_msgs.msg import String
from std_msgs.msg import Float32

class earwrapper:
    '''
    OUT_PIN_SERVO_1 = 32 #one of the ears
    OUT_PIN_SERVO_2 = 31  #one of the ears

    PULSE_FREQ = 20

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(OUT_PIN_SERVO_1, GPIO.OUT) 
    GPIO.setup(OUT_PIN_SERVO_2, GPIO.OUT) 
    '''

    '''
    def main(self):
        print("Starting")
        #left_ear = GPIO.PWM(OUT_PIN_SERVO_1, PULSE_FREQ) 
        #right_ear = GPIO.PWM(OUT_PIN_SERVO_2, PULSE_FREQ) 
        #print("Spinning")
        #left_ear.start(0) 
        #right_ear.start(0) 
        control = [3,3.5,4,4.5,5,5.5,6] 
        control2 = [3.5,3.25,3,2.75,2.5,2.25,2]
        # Test the full range of movement. Note only integers are allowed.
    
        #although it's not specificed what it'll do in documentation
        # a past problem with this code was that it wasn't clear how to change directions but maybe it'll work differently this time
        self.left_ear.ChangeDutyCycle(3)
        self.right_ear.ChangeDutyCycle(3.5)
        time.sleep(1)
        for x in range(7):
            self.left_ear.ChangeDutyCycle(control[x])
            self.right_ear.ChangeDutyCycle(control2[x])
            time.sleep(0.03)
        self.left_ear.stop() 
        self.right_ear.stop() 
        GPIO.cleanup()

    '''

    

    '''
    def move(self, emotion):
        print("Starting")

        self.left_ear.start(0) 

        print("Spinning")
        
        # Test the full range of movement. Note only integers are allowed.
        # 12=180 degrees, 6 is around 90 degrees
        #although it's not specificed what it'll do in documentation
        # a past problem with this code was that it wasn't clear how to change directions but maybe it'll work differently this time
        for x in range(2, 6):
            self.left_ear.ChangeDutyCycle(x)
            time.sleep(0.5)
        
        # Start over and move in bigger, slower movements.
        #left_ear.ChangeDutyCycle(2)
        #time.sleep(1)
        #left_ear.ChangeDutyCycle(6)
        #time.sleep(1)
        self.left_ear.stop() 
        GPIO.cleanup()
    '''

    #left ear:
        #min 3
        #3 is straight upward
        #6 is pointing outwards towards the left

    #right ear:
        #max 3.5
        #3.5 is straight upwards
        #2 is pointing outwards towards the right
    
    #considering x axis 0, y axis 90
    def convert_angle(self, msg):
        angle = msg.data
        print("data: ", angle)
        
        #3/90 = 1 degree
        left_degree = 3/90.0
        move_left = 6 - left_degree*angle

        if(move_left > 6):
            move_left = 6
        elif(move_left < 3):
            move_left = 3

        print("left ear: ", move_left)
        #self.left_ear.ChangeDutyCycle(move_left)

        #right ear
        right_degree = 1.5/90.0
        move_right = 2 + right_degree*angle

        if(move_right < 2):
            move_right = 2
        elif(move_right > 3.5):
            move_right = 3.5

        print("right ear: ", move_right)
        #self.right_ear.ChangeDutyCycle(move_right)

    def poses(self, msg):
        emotion = msg.data

        inmsg = Float32
        #TODO: these equivalencies are not working
        if(emotion == "neutral"):
            inmsg.data = 45.0
        elif(emotion == "happy"):
            inmsg.data = 80.0
        elif(emotion == "smirk"):
            inmsg.data = 60.0
        elif(emotion == "confused"):
            inmsg.data = 0.0 #TODO: can probably do -10 degrees, just need to test what that will look like
        elif(emotion == "surprised"):
            inmsg.data = 90.0
        else:
            print("incorrect emotion recieved\n")

        

        #convert degrees to ChangeDutyCycle amount and move ears
        self.convert_angle(inmsg) #TODO: takes in raw float?
        


    '''
    def stop(self):
        self.left_ear.stop()
        self.right_ear.stop()
        GPIO.cleanup()
    '''

    def __init__(self):
        #rospy.Subscriber("Shown_personality", String, callback_personality)

        rospy.Subscriber("Ear_angle", Float32, self.convert_angle) #can make a message containing 2 floats, or just have ears always mirror each other
        rospy.Subscriber("Shown_personality", String, self.poses)

        #rospy.Timer(30, self.callback_twitch, oneshot=False) #ear twitch
        '''
        OUT_PIN_SERVO_1 = 32 #left ear (view from back of head)
        OUT_PIN_SERVO_2 = 31 #right ear 
        PULSE_FREQ = 50

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(OUT_PIN_SERVO_1, GPIO.OUT)  #TODO:only one servo so far, might test with one servo to make sure they don't collide
        GPIO.setup(OUT_PIN_SERVO_2, GPIO.OUT)

        self.left_ear = GPIO.PWM(OUT_PIN_SERVO_1, PULSE_FREQ) 
        self.right_ear = GPIO.PWM(OUT_PIN_SERVO_2, PULSE_FREQ) 
        '''

if __name__ == "__main__":
    rospy.init_node("ear_node")
    ear_wrapper = earwrapper()
    #rospy.on_shutdown(ear_wrapper.stop())
    
    #rospy.on_shutdown(ear_wrapper.stop()) #don't know if needed but stop method might be useful
    rospy.loginfo("Ear driver is now started, ready to get commands.")
    rospy.spin()
    #main()
"""
import time 

import RPi.GPIO as GPIO 

 
OUT_PIN = 12 #one of the ears
PULSE_FREQ = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(OUT_PIN, GPIO.OUT) 


def main():
    print("Starting")
    left_ear = GPIO.PWM(OUT_PIN, PULSE_FREQ) 

    left_ear.start(0) 

    print("Spinning")
    
    # Test the full range of movement. Note only integers are allowed.
    # 12=180 degrees, 6 is around 90 degrees but they don't specify what happens in between these two numbers
    #although it's not specificed what it'll do in documentation
    # a past problem with this code was that it wasn't clear how to change directions but maybe it'll work differently this time
    for x in range(2, 5):
        left_ear.ChangeDutyCycle(x)
        time.sleep(1)
    left_ear.ChangeDutyCycle(2)
    time.sleep(1)
    
    # Start over and move in bigger, slower movements.
    #left_ear.ChangeDutyCycle(2)
    #time.sleep(1)
    #left_ear.ChangeDutyCycle(6)
    #time.sleep(1)
    
   
    
    left_ear.stop() 
    GPIO.cleanup()

def move(emotion):
    print("Starting")
    left_ear = GPIO.PWM(OUT_PIN, PULSE_FREQ) 

    left_ear.start(0) 

    print("Spinning")
    
    # Test the full range of movement. Note only integers are allowed.
    # 12=180 degrees, 6 is around 90 degrees
    #although it's not specificed what it'll do in documentation
    # a past problem with this code was that it wasn't clear how to change directions but maybe it'll work differently this time

    #left ear:
    #min 3
    #3 is straight upward
    #6 is pointing outwards towards the left

    #right ear:
    #max 3.5?
    #3 is straight upwards
    #2 is pointing outwards towards the right
    for x in range(2, 6):
        left_ear.ChangeDutyCycle(x)
        time.sleep(0.5)
    
    # Start over and move in bigger, slower movements.
    #left_ear.ChangeDutyCycle(2)
    #time.sleep(1)
    #left_ear.ChangeDutyCycle(6)
    #time.sleep(1)
    
   
    
    left_ear.stop() 
    GPIO.cleanup()

if __name__ == "__main__":
    main()
"""