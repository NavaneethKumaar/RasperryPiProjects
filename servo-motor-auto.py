import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def servo_rotate(degree):
    val=(degree/180)*10 + 2
    print(val)
    p.ChangeDutyCycle(val)
  

servoPIN=8

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 8 for PWM with 50Hz
p.start(0) # Initialization


degree=0

while True: # Run forever
    if degree > 180:
        degree=0

    servo_rotate(degree)
    
    sleep(1)
    degree = degree + 18

      


