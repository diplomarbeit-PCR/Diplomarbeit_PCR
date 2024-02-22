import time
import smbus

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)

beweg_address = 0x28
b = 0

# Kommunikation mit Bewegmechanismus

def writeNumber(val):
    bus.write_byte(beweg_address, val)
    return -1

def readFromBeweg():
    try:
        print("in Lesefkt")
        b = bus.read_byte(beweg_address)
        print("gelesen: ", b)
        

        # fragt ab, ob in 0-Posi
        if b == 5:
            #beweg_null = bus.read_byte(beweg_address)
            print("Nullposi")
            

        # falls Notaus gedrückt -> Stop everything
        if b == 9:
            #notaus = bus.read_byte(beweg_address)
            print("Notaus")
        
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

    return(b)





   
