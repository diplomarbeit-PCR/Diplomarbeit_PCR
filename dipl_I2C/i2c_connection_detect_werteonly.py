import smbus
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adresse des Slaves
detect_address = 0x27

d = 0

def readFromDetectorSL():
    d = bus.read_byte(detect_address)

    if d == 1:
        spg = bus.read_byte(detect_address)
        spg = int(spg)

    if d == 2:
        light = bus.read_byte(detect_address)
        light = int(light)

    return spg, light