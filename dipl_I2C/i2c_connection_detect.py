import smbus
import time


# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adressen der Slaves

detect_address = 0x27

value_spg = 0
value_light = 0
d = 0
d_alt = 0

# Kommunikation mit Detektor
def readFromDetect():
    try:
        print("in Lesefkt")
        d = bus.read_byte(detect_address)
        print("gelesen: ", d)
        

        # fragt ab, ob in 0-Posi
        if d == 5:
            print("Nullposi")
            

        # falls Notaus gedrückt -> Stop everything
        if d == 9:
            print("Notaus")
        
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

    return(d)

while True:


    if d != 5:
        d = readFromDetect()  

    if d == 7:
       print("Warten")
       time.sleep(2)
       d = readFromDetect()

    if d == 5:
        

        if d_alt == 1:
            value = readFromDetect()
            value_spg = int(value)
            print ("RPi sends: ", value_spg)
            d_alt = 0

        if d_alt == 2:
            value = readFromDetect
            value_light = int(value)
            print ("RPi sends: ", value_light)
            d_alt = 0

        d_alt = d
        



   
