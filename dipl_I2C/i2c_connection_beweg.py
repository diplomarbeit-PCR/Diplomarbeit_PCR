import smbus
import time

from dipl_Einfuehrung.zeitDefinition_Vererbt_v1 import Frm_zeitDef

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)

beweg_address = 0x28

go_beweg = True
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

def i2c_Beweg():
    frm_zeitDef = Frm_zeitDef()
    while go_beweg == True:
        if b != 5:
            b = readFromBeweg()  

        if b == 7:
           print("Warten")
           time.sleep(2)
           b = readFromBeweg()

        if b == 5:
           writeNumber(1)
           writeNumber(frm_zeitDef.value_denat)
           print ("RPi sends: ", frm_zeitDef.value_denat)
           time.sleep(2)

           writeNumber(2)
           writeNumber(frm_zeitDef.value_aneal_gesamt)
           print ("RPi sends: ", frm_zeitDef.value_aneal_gesamt)
           time.sleep(2)
        
           writeNumber(3)
           writeNumber(frm_zeitDef.value_elong_gesamt)
           print ("RPi sends: ", frm_zeitDef.value_elong_gesamt)
           time.sleep(2)

           # Start Wert
           writeNumber(4)
           time.sleep(2)

           go_beweg = False


   
