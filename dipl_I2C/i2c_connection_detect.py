import smbus
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adresse des Slaves
detect_address = 0x27

value_spg = 0
value_light = 0
d_alt = 0

# Kommunikation mit Detektor
def readFromDetect():
    try:
        print("in Lesefkt")
        d = bus.read_byte(detect_address)
        print("gelesen: ", d)

        return d
        
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

while True:
    d = readFromDetect()

    if d == 5:
        if d_alt == 1:
            print("spgs Funktion")
            value_spg = bus.read_byte(detect_address)
            print("RPi sends spg:", value_spg)
        elif d_alt == 2:
            print("Licht funktion")
            value_light = bus.read_byte(detect_address)
            print("RPi sends light:", value_light)

    elif d == 7:
        print("Warten")
        time.sleep(2)
    elif d == 9:
        print("Notaus")

    d_alt = d
