import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def multi_color(val):
    try:
        p.ChangeDutyCycle(val)
    except:
        print(".") #donothing


servoPIN=8

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 300) # GPIO 8 for PWM with 50Hz
p.start(0) # Initialization


val=0
while True: # Run forever
#     if val > 100:
#         val=0
# 
#     multi_color(val)
#     
#     sleep(1)
#     val = val + 10

    cmd = input("Enter the value (0 to 100): ")
    try:
        val=int(cmd)
    except:
        print("**** Error")
        continue
    
    multi_color(val)

      


