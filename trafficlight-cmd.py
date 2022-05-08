import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def off_all():
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
    GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) # Set pin 10 to be an output pin and set initial value to low (off)
    GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # Set pin 12 to be an output pin and set initial value to low (off)


def red_on():
    off_all()
    GPIO.output(8, GPIO.HIGH) # Turn on red
    
def yellow_on():
    off_all()
    GPIO.output(10, GPIO.HIGH) # Turn on yellow

def green_on():
    off_all()
    GPIO.output(12, GPIO.HIGH) # Turn on green
    
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

off_all()


while True: # Run forever
    cmd = input("Enter the colour")
    if (cmd == "red"):
        red_on()
    elif (cmd == "yellow"):
        yellow_on()
    elif (cmd == "green"):
        green_on()
    else:
        print("Give the value red or yellow or green")

