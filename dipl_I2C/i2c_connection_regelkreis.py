import smbus
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Adresse des Arduino-Slave
temp_address = 0x26

def readFromTemp():
    try:
        # Lesen der Daten als Block von 6 Bytes (2 Bytes pro Integer-Wert)
        data = bus.read_i2c_block_data(temp_address, 0, 6)

        # Interpretiere die empfangenen Daten als Integer-Werte
        value_denat = int.from_bytes(data[0:2], byteorder='little', signed=True)
        value_aneal = int.from_bytes(data[2:4], byteorder='little', signed=True)
        value_elong = int.from_bytes(data[4:6], byteorder='little', signed=True)

        print("Empfangener Denat-Wert:", value_denat)
        print("Empfangener Aneal-Wert:", value_aneal)
        print("Empfangener Elong-Wert:", value_elong)

        return value_denat, value_aneal, value_elong

    except OSError as e:
        print(f"Fehler beim Lesen vom I2C-Gerät: {e}")
        return None, None, None

# Hauptprogramm
while True:
    value_denat, value_aneal, value_elong = readFromTemp()
    time.sleep(1)  # Führt die Messung alle Sekunde erneut durch
