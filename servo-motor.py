import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def servo_rotate(degree):
    val=(degree/180)*10 + 2
    p.ChangeDutyCycle(val)
  

servoPIN=8

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 8 for PWM with 50Hz
p.start(0) # Initialization



while True: # Run forever
    cmd = input("Enter the degree")
    try:
        degree=int(cmd)
    except:
        print("**** Error")
        continue
    
    if degree >=0 and degree <=180 :
        servo_rotate(degree)
    else:
        print("****Invalid command")
      


