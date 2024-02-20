import smbus
import time


# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adressen der Slaves

detect_address = 0x27



# Kommunikation mit Detektor
def readFromDetekt():
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
                    value_spg = bus.read()
                    print("Messwert 1:", value_spg)
            elif d == 2:
                # Nachricht erhalten, dass der Messwert 2 gesendet wird
                print("Nachricht erhalten: Messwert 2 wird gesendet")
                # Messwert 2 anfordern
                bus.request_from(detect_address)
                if bus.available():
                    value_light = bus.read()
                    print("Messwert 2:", value_light)
            else:
                # Nachricht erhalten, dass die Bedingung nicht erfüllt ist
                print("Bedingung nicht erfüllt")

            print(value_spg)    
            print(value_light) 
        return value_spg, value_light
 
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None
