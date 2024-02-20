import smbus
import time


# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adressen der Slaves

detect_address = 0x27

# Kommunikation mit Detektor
def readFromDetekt():
    try:
        # Daten vom Slave anfordern
        print("in Lesefkt")
        d = bus.read_byte(detect_address)        
        print("gelesen: ", d)

        # fragt ab, ob in 0-Posi
        if d == 5:
            #beweg_null = bus.read_byte(beweg_address)
            print("Nullposi")
            

        # falls Notaus gedrückt -> Stop everything
        if d == 9:
            #notaus = bus.read_byte(beweg_address)
            print("Notaus")

        print(value_spg)    
        print(value_light) 
        return value_spg, value_light
 
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

d = readFromDetekt

while True:

    if d != 5:
        d = readFromDetekt()  

    if d == 7:
       print("Warten")
       time.sleep(2)
       d = readFromDetekt()

    if d == 5:
        
        w = bus.read_byte(detect_address)    

        if w_alt == 1:
            value = bus.read_byte(detect_address)
            value_spg = int(value)
            print ("RPi sends: ", value_spg)
            w_alt = 0

        if w_alt == 2:
            value = bus.read_byte(detect_address)
            value_light = int(value)
            print ("RPi sends: ", value_light)
            w_alt = 0
        
        w_alt = w


   
