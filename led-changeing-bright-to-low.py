import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def brightness_changer(val):
    try:
        p.ChangeDutyCycle(val)
    except:
        print("**error**") #donothing


lightPIN=8

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(lightPIN, GPIO.OUT)

p = GPIO.PWM(lightPIN, 1) # GPIO 8 for PWM with 50Hz
p.start(0) # Initialization


val=0
while True: # Run forever

    cmd = input("Enter the value (0 to 100): ")
    try:
        val=int(cmd)
    except:
        print("**** Error")
        continue
    
    brightness_changer(val)

      




