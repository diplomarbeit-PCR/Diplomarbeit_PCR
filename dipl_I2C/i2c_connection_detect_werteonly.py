import smbus
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adresse des Slaves
detect_address = 0x27

def readFromDetectorSL():
    try:
        # Nachricht, dass der Messwert 1 gesendet wird
        bus.write_byte(detect_address, 1)
        time.sleep(0.1)  # Kurze Pause für die Kommunikation

        # Lesen des ersten Messwerts (SPG)
        spg = bus.read_byte(detect_address)
        print("Empfangener SPG-Wert:", spg)

        # Nachricht, dass der Messwert 2 gesendet wird
        bus.write_byte(detect_address, 2)
        time.sleep(0.1)  # Kurze Pause für die Kommunikation

        # Lesen des zweiten Messwerts (Licht)
        light = bus.read_byte(detect_address)
        print("Empfangener Licht-Wert:", light)

        return spg, light

    except OSError as e:
        print(f"Fehler beim Lesen vom I2C-Gerät: {e}")
        return None, None

# Hauptprogramm
while True:
    spg, light = readFromDetectorSL()
    time.sleep(1)  # Führt die Messung alle Sekunde erneut durch#
