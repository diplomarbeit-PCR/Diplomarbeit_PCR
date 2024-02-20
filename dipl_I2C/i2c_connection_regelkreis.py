import smbus
import struct
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Adresse des Arduino-Slave
arduino_address = 0x27

# Funktion zum Lesen von Float-Werten
def read_float():
    bytes_array = []
    for _ in range(4):  # 4 Bytes für einen Float-Wert
        bytes_array.append(bus.read_byte(arduino_address))
    float_value = struct.unpack('f', bytes(bytes_array))[0]
    return float_value

# Hauptprogramm
while True:
    # Anfrage an den Arduino-Slave senden
    bus.write_byte(arduino_address, 1)
    time.sleep(0.1)
    
    # Ersten Wert (SPG) empfangen
    spg = read_float()
    print("Empfangener SPG-Wert:", spg)
    
    # Zweiten Wert (Licht) empfangen
    bus.write_byte(arduino_address, 2)
    time.sleep(0.1)
    light = read_float()
    print("Empfangener Licht-Wert:", light)

    # Dritten Wert empfangen
    bus.write_byte(arduino_address, 3)
    time.sleep(0.1)
    third_value = read_float()
    print("Empfangener Dritter Wert:", third_value)
