import smbus
import time


# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adressen der Slaves
temp_address = 0x26

# Kommunikation mit Regelkreis
def readFromTemp():
    try:
        # Lesen des zweiten Messwerts (Licht)
        value_denat = bus.read_byte(temp_address)
        print("Empfangener Denat", value_denat)

        # Lesen des ersten Messwerts (SPG)
        value_aneal = bus.read_byte(temp_address)
        print("Empfangener Aneal:", value_aneal)

        value_elong = bus.read_byte(temp_address)
        print("Empfangener Aneal:", value_elong)

        return value_denat, value_aneal, value_elong

    except OSError as e:
        print(f"Fehler beim Lesen vom I2C-Gerät: {e}")
        return None, None

# Hauptprogramm
while True:
    value_denat, value_aneal, value_elong = readFromTemp()
    time.sleep(1)  # Führt die Messung alle Sekunde erneut durch#
