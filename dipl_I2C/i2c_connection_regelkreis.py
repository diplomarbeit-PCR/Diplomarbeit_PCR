import smbus
import struct

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adresse des Slaves
detect_address = 0x27

# Funktion zum Lesen von Float-Werten
def read_float():
    bytes_array = []
    for _ in range(4):  # 4 Bytes für einen Float-Wert
        bytes_array.append(bus.read_byte(detect_address))
    float_value = struct.unpack('f', bytes(bytes_array))[0]
    return float_value

# Hauptprogramm
while True:
    spg = read_float()
    light = read_float()
    third_value = read_float()
    print("SPG-Wert:", spg)
    print("Licht-Wert:", light)
    print("Dritter Wert:", third_value)
