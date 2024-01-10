import smbus
import time
bus = smbus.SMBus(1)

address = 0x05

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    inp = input("Number between 1 and 9: ")
    if not inp:
        continue

    writeNumber(inp)
    print ("RPi sends: ", inp)
    time.sleep(1)

    recv = readNumber()
    print ("Arduino sends: ", recv)