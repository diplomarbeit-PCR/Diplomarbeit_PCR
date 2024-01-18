import smbus
import time

bus = smbus.SMBus(7)

address = 0x28
slave_address = 0x27




def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readFromSlave():
    try:
        value = bus.read_byte(slave_address)
        return value
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

while True:
    inp = input("Number between 1 and 9: ")
    inp = int(inp)
    if not inp:
        continue

    writeNumber(inp)
    print ("RPi sends: ", inp)
    time.sleep(1)

    value = readFromSlave()

    if value is not None:
        print(f"Received value from Arduino: {value}")
    else:
        # Handle error, for example, you may choose to break the loop or take corrective action.
        break
