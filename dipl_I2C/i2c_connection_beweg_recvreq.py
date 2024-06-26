import smbus
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)

beweg_address = 0x04

value_denat = 10
value_aneal_gesamt = 30
value_elong_gesamt = 20
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
            writeNumber(4)
            

        # falls Notaus gedrückt -> Stop everything
        if b == 9:
            #notaus = bus.read_byte(beweg_address)
            print("Notaus")
        
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

    return(b)

while True:


    if b != 5:
        b = readFromBeweg()  

    if b == 7:
       print("Warten")
       time.sleep(2)
       b = readFromBeweg()

    if b == 5:
        inp = input("Number between 1 and 3: ")
        inp = int(inp)
        if not inp:
            continue

        if inp == 1:
            value = value_denat
            value = int(value)
            writeNumber(inp)
            print ("RPi sends: ", inp)

        if inp == 2:
            value = value_aneal_gesamt
            value = int(value)
            writeNumber(inp)
            print ("RPi sends: ", inp)
        
        if inp == 3:
            value = value_elong_gesamt
            value = int(value)
            writeNumber(inp)
            print ("RPi sends: ", inp)

        if inp != 1 and inp != 2 and inp !=3:
            value = inp

        writeNumber(value)
        print ("RPi sends: ", value)
        time.sleep(1)


   
