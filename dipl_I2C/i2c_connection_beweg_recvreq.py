import smbus
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)

beweg_address = 0x28

value_denat = 10
value_aneal_gesamt = 30
value_elong_gesamt = 20

# Kommunikation mit Bewegmechanismus

def writeNumber(val):
    bus.write_byte(beweg_address, val)
    return -1

def readFromBeweg():
    try:
        b = bus.read_byte(beweg_address)

        # fragt ab, ob in 0-Posi
        if b == 5:
            beweg_null = bus.read_byte(beweg_address)
        
        # falls Notaus gedrückt -> Stop everything
        if b == 9:
            notaus = bus.read_byte(beweg_address)

        else:
            print(f"No valid input")

        return notaus, beweg_null
 
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

while True:
    inp = input("Number between 1 and 3: ")
    inp = int(inp)
    if not inp:
        continue

    if inp == 1:
        #writeNumber(inp)
        value = value_denat
        value = int(value)
        writeNumber(inp)
        print ("RPi sends: ", inp)


        
    if inp == 2:
        #writeNumber(inp)
        value = value_aneal_gesamt
        value = int(value)
        writeNumber(inp)
        print ("RPi sends: ", inp)


        
    if inp == 3:
        value = value_elong_gesamt
        value = int(value)
        writeNumber(inp)
        print ("RPi sends: ", inp)

    else:
        value = int(inp)

    time.sleep(2)
    writeNumber(value)
    print ("RPi sends: ", value)
    time.sleep(1)

   
