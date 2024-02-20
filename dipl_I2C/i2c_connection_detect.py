import smbus
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adresse des Slaves
detect_address = 0x27

# Kommunikation mit Detektor
def readFromDetect():
    try:
        print("in Lesefkt")
        d = bus.read_byte(detect_address)
        print("gelesen: ", d)

        if d == 5:
            print("in 0-Posi")

        elif d == 7:
            print("Warten")
            time.sleep(2)
        elif d == 9:
            print("Notaus")

        return d
        
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None
    

def readFromDetector():
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

d = readFromDetect()
while True:
    spg, light = readFromDetector()
    time.sleep(1)  # Führt die Messung alle Sekunde erneut durch


    
