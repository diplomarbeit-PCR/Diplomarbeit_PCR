import smbus
import time
bus = smbus.SMBus(1)

address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

while True:
    inp = input("Number between 1 and 9: ")
    if not inp:
        continue

    writeNumber(inp)
    print ("Rock sends: "), inp
    time.sleep(1)