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
        # Daten vom Slave anfordern
        bus.request_from(detect_address)
        if bus.available():
            d = bus.read()
            if d == 1:
                # Nachricht erhalten, dass der Messwert 1 gesendet wird
                print("Nachricht erhalten: Messwert 1 wird gesendet")
                # Messwert 1 anfordern
                bus.request_from(detect_address)
                if bus.available():
                    frm_kont.value_spg = bus.read()
                    print("Messwert 1:", frm_kont.value_spg)
            elif d == 2:
                # Nachricht erhalten, dass der Messwert 2 gesendet wird
                print("Nachricht erhalten: Messwert 2 wird gesendet")
                # Messwert 2 anfordern
                bus.request_from(detect_address)
                if bus.available():
                    frm_kont.value_light = bus.read()
                    print("Messwert 2:", frm_kont.value_light)
            else:
                # Nachricht erhalten, dass die Bedingung nicht erfüllt ist
                print("Bedingung nicht erfüllt")

            print(frm_kont.value_spg)    
            print(frm_kont.value_light) 
        return frm_kont.value_spg, frm_kont.value_light
 
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
        if t_alt == 1:
            frm_denat.temp_denat = t
            t_alt = 0

        if t_alt == 2:
            frm_aneal.temp_aneal = t
            t_alt = 0

        if t_alt == 3:
            frm_elong.temp_elong = t
            t_alt = 0
        else:
            print(f"No valid input")

        t_alt = t

        print(frm_denat.temp_denat) 
        print(frm_aneal.temp_aneal) 
        print(frm_elong.temp_elong) 
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

