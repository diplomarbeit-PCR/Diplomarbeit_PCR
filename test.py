import smbus
import time

bus_number = 0  # Du kannst auch Bus 0 ausprobieren
address = 0x27
#https://prod.liveshare.vsengsaas.visualstudio.com/join?D782CC7934A2ABFE225732FC1764658FBB54
try:
    bus = smbus.SMBus(bus_number)
except FileNotFoundError:
    print(f"Error: I2C bus {bus_number} not found. Check your connections and bus number.")
    exit()

def writeNumber(value):
    try:
        bus.write_byte(address, value)
        return None
    except OSError as e:
        print(f"Error writing to I2C device: {e}")
        return e

def readNumber():
    try:
        number = bus.read_byte(address)
        return number
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

while True:
    inp = input("Number between 1 and 9: ")
    inp = int(inp)
    if not inp:
        continue

    write_result = writeNumber(inp)
    if write_result is not None:
        # Handle error, for example, you may choose to break the loop or take corrective action.
        break

    print("RPi sends:", inp)
    time.sleep(1)

    recv = readNumber()
    if recv is not None:
        # Handle error, for example, you may choose to break the loop or take corrective action.
        break

    print("Arduino sends:", recv)
