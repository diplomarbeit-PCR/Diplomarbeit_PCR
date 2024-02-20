import smbus
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adresse des Slaves
detect_address = 0x27

def readFromDetectorSL():
    try:
        # Lesen des zweiten Messwerts (Licht)
        light = bus.read_byte(detect_address)
        print("Empfangener Licht-Wert:", light)

        # Lesen des ersten Messwerts (SPG)
        spg = bus.read_byte(detect_address)
        print("Empfangener SPG-Wert:", spg)

        return spg, light

    except OSError as e:
        print(f"Fehler beim Lesen vom I2C-Gerät: {e}")
        return None, None

# Hauptprogramm
while True:
    spg, light = readFromDetectorSL()
    time.sleep(1)  # Führt die Messung alle Sekunde erneut durch#
