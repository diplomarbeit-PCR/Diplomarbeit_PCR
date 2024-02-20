import smbus
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Adresse des Arduino-Slave
temp_address = 0x26

def readFromTemp():
    try:
        # Lesen des zweiten Messwerts (Licht)
        value_denat = bus.read_byte(temp_address)
        print("Empfangener Denat-Wert:", value_denat)

        # Lesen des ersten Messwerts (SPG)
        value_aneal = bus.read_byte(temp_address)
        print("Empfangener Aneal-Wert:", value_aneal)

        # Lesen des ersten Messwerts (SPG)
        value_elong = bus.read_byte(temp_address)
        print("Empfangener Elong-Wert:", value_elong)

        return value_denat, value_aneal, value_aneal

    except OSError as e:
        print(f"Fehler beim Lesen vom I2C-Gerät: {e}")
        return None, None

# Hauptprogramm
# Hauptprogramm
while True:
    value_denat, value_aneal, value_elong = readFromTemp()
    time.sleep(1)  # Führt die Messung alle Sekunde erneut durch
