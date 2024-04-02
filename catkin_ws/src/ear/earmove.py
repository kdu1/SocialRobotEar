# Set up libraries and overall settings

from gpiozero import Servo
from time import sleep

servo = Servo(15) #ear

val = .5
servo.value = val
while val < .6: #move to .6
    servo.value = val
    val = val + 0.01
    sleep(.5)



# import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
# from time import sleep   # Imports sleep (aka wait or pause) into the program
# GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout

# # Set up pin 11 for PWM
# GPIO.setup(15,GPIO.OUT)  # Sets up pin 15 to an output (instead of an input)
# p = GPIO.PWM(15, 50)     # Sets up pin 15 as a PWM pin
# p.start(0)               # Starts running PWM on the pin and sets it to 0

# # Move the servo back and forth
# p.ChangeDutyCycle(1)     # Changes the pulse width to 1 (so moves the servo) MAKE SURE IT FALLS WITHIN THE SERVO LIMITS
# sleep(1)                 # Wait 1 second
# #p.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)
# #sleep(1)

# # Clean up everything
# p.stop()                 # At the end of the program, stop the PWM
# GPIO.cleanup()           # Resets the GPIO pins back to defaults