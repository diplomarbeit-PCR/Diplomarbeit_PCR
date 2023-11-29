import smbus
import time

# Adresse des Arduino auf dem I2C-Bus
arduino_address = 0x12

# Öffnen Sie den I2C-Bus (normalerweise Bus 1 auf einem Raspberry Pi)
bus = smbus.SMBus(1)

# Funktion zum Senden eines Signals an den Arduino über I2C
def send_signal():
    try:
        # Senden Sie das Signal (in diesem Fall die Zahl 1) an die Arduino-Adresse
        bus.write_byte(arduino_address, 1)
        print("Signal erfolgreich gesendet")
    except Exception as e:
        print(f"Fehler beim Senden des Signals: {e}")

# Beispiel: Signal alle 5 Sekunden senden
while True:
    send_signal()
    time.sleep(5)