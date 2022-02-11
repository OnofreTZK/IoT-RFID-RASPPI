from time import sleep
import json
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()


class RaspPIManager(object):

    def __init__(self):
        ''' Constructor '''
        self.listOfAccess = []
        self.isReading = False

    def writeTag(self, data):
        ''' Write function '''

        while True:
            #text = 'Tiago Onofre'
            print("Aproxime a tag")
            reader.write(json.dumps(data))
            print('Tag preenchida!')
            sleep(5)
            GPIO.cleanup()
            break

    def readTag(self):
        ''' Read function '''

        try:
            while True:
                print("Aproxime a tag")
                id, data = reader.read()
                print(data)
                # send data to repo
                sleep(5)
        except KeyboardInterrupt:
            GPIO.cleanup()
            raise

    def argsService(self, args):
        ''' Arguments processing '''

        if len(args) != 2:
            print('''Por favor execute conforme o exemplo:
python3 raspberry.py r ou w
r -> leitura
w -> escrita''')
            sys.exit(1)

        if args[1].lower() == 'r':
            self.isReading = True

    def exec(self, args):
        ''' Main method '''

        self.argsService(args)

        if self.isReading:
            print("reading method")
            sys.exit(0)
        #else

        print("writing method")
        sys.exit(0)



#--------------------------------------------------------------------------------------------------

manager = RaspPIManager()

manager.exec(sys.argv)
