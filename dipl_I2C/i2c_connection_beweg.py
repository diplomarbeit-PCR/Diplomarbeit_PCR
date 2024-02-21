import smbus
import time

from dipl_Einfuehrung.zeitDefinition_Vererbt_v1 import Frm_zeitDef

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)

beweg_address = 0x28

value_denat = 10
value_aneal_gesamt = 30
value_elong_gesamt = 20

# Kommunikation mit Bewegmechanismus
def writeBeweg(val):
    bus.write_byte(beweg_address, val)
    return -1

def readFromBeweg():
    frm_zeitDef = Frm_zeitDef()
    try:
        b = bus.read_byte(beweg_address)

        # fragt ab, ob in 0-Posi
        if b == 5:
            print("Nullposi")
            writeBeweg(1)
            writeBeweg(frm_zeitDef.value_denat)
            writeBeweg(2)
            writeBeweg(frm_zeitDef.value_aneal_gesamt)
            writeBeweg(3)
            writeBeweg(frm_zeitDef.value_elong_gesamt)

        if b == 7:
            #noch nicht in 0-Posi
            print("Warte")

        # falls Notaus gedrückt -> Stop everything
        if b == 9:
            #notaus = bus.read_byte(beweg_address)
            print("Notaus")
        
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

