import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def motor_off():
    GPIO.output(8, GPIO.LOW) # Turn on motor  

def motor_on():
    GPIO.output(8, GPIO.HIGH) # Turn on motor
    

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)


while True: # Run forever
    cmd = input("Enter the command")
    if (cmd == "run"):
        motor_on()
    elif (cmd == "stop"):
        motor_off()
    else:
        print("****Invalid command")
      

