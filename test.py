import smbus
import time
import os
<<<<<<< HEAD
bus = smbus.SMBus(2)
=======
bus = smbus.SMBus(10)
>>>>>>> 00366816db37c65ba73638dd8ad8ecdc7473ccbc

address = 0x27

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    inp = input("Number between 1 and 9: ")
    inp = int(inp)
    if not inp:
        continue

    writeNumber(inp)
    print ("RPi sends: ", inp)
    time.sleep(1)

    recv = readNumber()
    print ("Arduino sends: ", recv)