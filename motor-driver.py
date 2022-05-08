import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def motor_forward():
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)   

def motor_reverse():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)   

def motor_stop():
    GPIO.output(22, GPIO.LOW)  
    

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)


while True: # Run forever
    cmd = input("Enter the command")
    if (cmd == "forward"):
        motor_forward()
    elif (cmd == "reverse"):
        motor_reverse()    
    elif (cmd == "stop"):
        motor_stop()
    else:
        print("****Invalid command")
      


