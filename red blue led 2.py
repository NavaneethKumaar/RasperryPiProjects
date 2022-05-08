import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def lightControl(blueStatus, redStatus):
 GPIO.output(10, blueStatus) # Turn on blue
 GPIO.output(8, redStatus) # Turn on red
 sleep(1) # Sleep for 1 second
# end of def

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) # Set pin 10 to be an output pin and set initial value to low (off)

while True: # Run forever
  lightControl(GPIO.HIGH,GPIO.HIGH)
  lightControl(GPIO.HIGH,GPIO.LOW)
  lightControl(GPIO.LOW,GPIO.HIGH)
  lightControl(GPIO.LOW,GPIO.LOW)
 