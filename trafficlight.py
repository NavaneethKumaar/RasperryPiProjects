import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) # Set pin 10 to be an output pin and set initial value to low (off)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # Set pin 12 to be an output pin and set initial value to low (off)

while True: # Run forever

  GPIO.output(8, GPIO.HIGH) # Turn on red
  sleep(2) # Sleep for 2 second
  GPIO.output(8, GPIO.LOW) # Turn off red
  
  GPIO.output(10, GPIO.HIGH) # Turn on yellow
  sleep(2) # Sleep for 2 second
  GPIO.output(10, GPIO.LOW) # Turn off yellow
  
  GPIO.output(12, GPIO.HIGH) # Turn on green
  sleep(4) # Sleep for 4 second
  GPIO.output(12, GPIO.LOW) # Turn off green
