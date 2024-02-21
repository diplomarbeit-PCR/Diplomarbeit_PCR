import smbus
import time

from dipl_Kontrolle.KontrollErgebnis_Vererbt_v1 import Frm_kont

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adresse des Slaves
detect_address = 0x27

def readFromDetectorSL():
    frm_kont = Frm_kont()
    try:
        # Lesen des zweiten Messwerts (Licht)
        frm_kont.value_light = bus.read_byte(detect_address)
        print("Empfangener Licht-Wert:", frm_kont.value_light)

        # Lesen des ersten Messwerts (SPG)
        frm_kont.value_spg = bus.read_byte(detect_address)
        print("Empfangener SPG-Wert:", frm_kont.value_spg)

        return frm_kont.value_spg, frm_kont.value_light

    except OSError as e:
        print(f"Fehler beim Lesen vom I2C-Gerät: {e}")
        return None, None
