import smbus
import time

# I2C-Adresse des Arduino-Slave
SLAVE_ADDRESS = 0x08

# Instanziierung des I2C-Bus
bus = smbus.SMBus(7)

def main():
    # Lies den Wert vom Arduino-Slave
    switch_state = bus.read_byte(SLAVE_ADDRESS)

    # Entscheide, welcher Wert basierend auf dem Zustand des Endschalters gesendet werden soll
    if switch_state == 7:
        print("Received switch state: LOW")
        switch_state = bus.read_byte(SLAVE_ADDRESS)

    elif switch_state == 5:
        print("Received switch state: HIGH")

        # Sende Befehl an den Slave, das Hauptprogramm zu starten
        bus.write_byte(SLAVE_ADDRESS, 4)

        # Warte auf die Bestätigung vom Slave, dass das Hauptprogramm abgeschlossen ist
        while True:
            if bus.read_byte(SLAVE_ADDRESS) == 1:
                break

        # Empfange die gemessenen Werte vom Slave
        value_spg = 0
        value_light = 0

        # Lese die eindeutig gekennzeichneten Werte
        while True:
            data = bus.read_byte(SLAVE_ADDRESS)
            if data == ord('S'): # Kennzeichnung für SPG
                value_spg = bus.read_byte(SLAVE_ADDRESS)
            elif data == ord('L'): # Kennzeichnung für Light
                value_light = bus.read_byte(SLAVE_ADDRESS)
            if value_spg != 0 and value_light != 0:
                break

        # Zeige die gemessenen Werte an
        print("Received values from slave: SPG -", value_spg, ", Light -", value_light)

if __name__ == "__main__":
    main()
