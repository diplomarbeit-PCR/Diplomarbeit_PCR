import smbus
import time

bus = smbus.SMBus(7)
temp_address = 0x26
detect_address = 0x27
beweg_address = 0x028

t = 0
d = 0
a = 0
b = 0
w = 0
k = 0
s = 0
n = 0

def writeNumber(value):
    bus.write_byte(beweg_address, value)
    return -1

def readFromTemp():
    try:
        t = bus.read_byte(temp_address)
        if t == 1:
            temp_denat = bus.read_byte(temp_address)

        if t == 2:
            temp_aneal = bus.read_byte(temp_address)
    
        if t == 3:
            temp_elong = bus.read_byte(temp_address)

        else:
            print(f"No valid input")

        return temp_denat, temp_aneal, temp_elong
 
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None
    
def readFromDetekt():
    try:
        d = bus.read_byte(detect_address)
        if d == 1:
            value_spg = bus.read_byte(detect_address)

        if d == 2:
            value_light = bus.read_byte(detect_address)
    
        if d == 3:
            detect_null = bus.read_byte(detect_address)

        else:
            print(f"No valid input")

        return value_spg, value_light, detect_null
 
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None
    
def readFromBeweg():
    try:
        b = bus.read_byte(temp_address)
        if t == 1:
            notaus = bus.read_byte(beweg_address)

        if t == 2:
            beweg_null = bus.read_byte(beweg_address)

        else:
            print(f"No valid input")

        return notaus, beweg_null
 
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

while True:
    value_denat = input("Enter Denat value: ")
    value_denat = int(value_denat)
    writeNumber(beweg_address, value_denat)
    print("RPi sends Denat: ", value_denat)
    time.sleep(1)

    value_aneal = input("Enter Aneal value: ")
    value_aneal = int(value_aneal)
    writeNumber(beweg_address, value_aneal)
    print("RPi sends Aneal: ", value_aneal)
    time.sleep(1)

    value_elong = input("Enter Elong value: ")
    value_elong = int(value_elong)
    writeNumber(beweg_address, value_elong)
    print("RPi sends Elong: ", value_elong)
    time.sleep(1)
