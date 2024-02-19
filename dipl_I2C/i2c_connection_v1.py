import smbus
import time

from dipl_Einfuehrung.zeitDefinition_Vererbt_v1 import Frm_zeitDef
from dipl_Phasenablauf.Phasenablauf_Vererbt_v1 import  Frm_denat, Frm_aneal, Frm_elong
from dipl_Kontrolle.KontrollErgebnis_Vererbt_v1 import Frm_kont

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adressen der Slaves
temp_address = 0x26
detect_address = 0x27
beweg_address = 0x028



# Kommunikation mit Detektor
def readFromDetekt():
    frm_kont = Frm_kont()
    try:
        d = bus.read_byte(detect_address)
        # fragt ab, ob <detektor in Nullposition ist und die Probe eingeführt ist
        if d == 1:
            frm_kont.detect_null = bus.read_byte(detect_address)

        if d == :
            frm_kont.detect_null = bus.read_byte(detect_address)

        # fragt nach Spg
        if d == 2:
            frm_kont.value_spg = bus.read_byte(detect_address)

        # fragt nach Lichtintensität    
        if d == 3:
            frm_kont.value_light = bus.read_byte(detect_address)

        else:
            print(f"Noch nicht bereit")
            print(f"Bitte kontrollieren Sie, ob die Probe beim Detektor ist")
            print(f"Bitte kontrollieren Sie, ob der Detektor in Nullposition steht.")

        return frm_kont.value_spg, frm_kont.value_light, frm_kont.detect_null
 
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None


# Kommunikation mit Regelkreis
def readFromTemp():
    frm_denat = Frm_denat()
    frm_aneal = Frm_aneal()
    frm_elong = Frm_elong()

    try:
        t = bus.read_byte(temp_address)
        if t == 1:
            frm_denat.temp_denat = bus.read_byte(temp_address)

        if t == 2:
            frm_aneal.temp_aneal = bus.read_byte(temp_address)
    
        if t == 3:
            frm_elong.temp_elong = bus.read_byte(temp_address)

        else:
            print(f"No valid input")

        return frm_denat.temp_denat, frm_aneal.temp_aneal, frm_elong.temp_elong
 
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

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

        # falls Notaus gedrückt -> Stop everything
        if b == 9:
            #notaus = bus.read_byte(beweg_address)
            print("Notaus")
        
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

