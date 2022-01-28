from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        print("Aproxime a tag")
        id, text = reader.read()
        print(text)
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
