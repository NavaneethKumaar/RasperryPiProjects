import RPi.GPIO as GPIO
from time import sleep
from mfrc522 import SimpleMFRC522


 
#pip install mfrc522
 
def ledOn():
    GPIO.output(LED, GPIO.HIGH)  #Turn on LED
    sleep(1)                #Wait 5 Seconds
    GPIO.output(LED, GPIO.LOW)   #Turn off LED



#Configure LED Output Pin
LED = 8
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create an object of the class MFRC522
reader = SimpleMFRC522()
 
my_uid=1067589061223
nameDictionary={1067589061223:'Navaneeth'}
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while True:
    
    id, text = reader.read()
    #print("ID: %s\nText: %s\n" % (id,text))
    print("ID: '%s'" %(nameDictionary[id]))
    
    if id == my_uid:                #Open the Doggy Door if matching UIDs
        print("Authorize Entry")
        ledOn()
    else:                            #Don't open if UIDs don't match
        print("Access Denied")
     