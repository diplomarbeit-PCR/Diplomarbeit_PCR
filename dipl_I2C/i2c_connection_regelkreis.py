import smbus

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Adresse des Arduino-Slave
arduino_address = 0x27

def read_int():
    # Lesen von 2 Bytes für einen Int-Wert
    byte1 = bus.read_byte(arduino_address)
    byte2 = bus.read_byte(arduino_address)
    # Kombinieren der Bytes zu einem Int-Wert
    value = (byte2 << 8) | byte1
    return value

# Hauptprogramm
while True:
    # Anfrage an den Arduino-Slave senden
    bus.write_byte(arduino_address, 1)
    
    # Ersten Wert empfangen
    value1 = read_int()
    print("Empfangener Wert 1:", value1)
    
    # Zweiten Wert empfangen
    value2 = read_int()
    print("Empfangener Wert 2:", value2)
    
    # Dritten Wert empfangen
    value3 = read_int()
    print("Empfangener Wert 3:", value3)
