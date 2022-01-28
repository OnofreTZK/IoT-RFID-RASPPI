from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        text = 'Tiago Onofre'
        print("Aproxime a tag")
        reader.write(text)
        print('Escrita' )
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
