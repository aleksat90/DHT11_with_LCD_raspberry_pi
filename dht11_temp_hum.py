#IMPORTOVANJE MODULA
import sys
import Adafruit_DHT

class TempSensor():
        def getRez(self):
                humidity, temperature = Adafruit_DHT.read_retry(11, 4)
                return humidity, temperature
