"""
Pi Servo module.
"""
import time 

import RPi.GPIO as GPIO 

 
OUT_PIN = 12 #one of the ears
PULSE_FREQ = 50

GPIO.setmode(GPIO.BOARD)
GPIO.setup(OUT_PIN, GPIO.OUT) 


def main():
    print("Starting")
    servo1 = GPIO.PWM(OUT_PIN, PULSE_FREQ) 

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

def move(emotion):
    print("Starting")
    servo1 = GPIO.PWM(OUT_PIN, PULSE_FREQ) 

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

if __name__ == "__main__":
    main()