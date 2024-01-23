import smbus
import time

bus = smbus.SMBus(7)

address = 0x28

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

while True:
    inp = input("Number between 1 and 9: ")
    inp = int(inp)
    if not inp:
        continue

    writeNumber(inp)
    print ("RPi sends: ", inp)
    time.sleep(1)

   