import smbus
import time

# Definieren Sie die Adresse des Arduinos auf dem I2C-Bus
temp_address = 0x12  # Beispieladresse, ersetzen Sie sie durch die tatsächliche Slave-Adresse

# Öffnen Sie den I2C-Bus (abhängig von Ihrem System kann die Busnummer variieren)
bus = smbus.SMBus(7)  # Bus 1 öffnen, Sie können die richtige Busnummer je nach Ihrem Setup anpassen

null = 0

# Funktion zum Lesen von Daten vom Arduino
def read_data():
    data = []
    i = 0
    bus.write_byte(temp_address, 10)
    time.sleep(1)

    for i in range(8):
        i = i+1
        bus.write_byte(temp_address, i)
        print(i)
        time.sleep(1)
        
        
    for _ in range(8):  # Wir erwarten 3 Datenpunkte (temp_denat, temp_aneal, temp_elong)
        data.append(bus.read_byte(temp_address))
        

    return data

def read_detect_null():
    null = read_from_detect()
    # Nur Daten vom Slave lesen, wenn der Leseprozess nicht gestoppt wurde
    data_sent = False
    if null is None:             
        null = read_from_detect()

    if null == 7:
        null = read_from_detect()
                        
    if null == 0:
        null = read_from_detect()
    
    if null == 5 and not data_sent:
        data_sent = True

        data_received = read_data()

        temp_d = data_received[0] 
        temp_a = data_received[1] 
        temp_e = data_received[2] 
        temp_de = data_received[3] 
        temp_an = data_received[4] 
        temp_el = data_received[5] 
        temp_den = data_received[6] 
        temp_ane = data_received[7] 

        # Die erhaltenen Daten anzeigen
        print("Temperaturen")
        print("Temperature (Denat):", temp_d)
        print("Temperature (Aneal):", temp_a)
        print("Temperature (Elong):", temp_e)
        print("Temperature (Denat):", temp_de)
        print("Temperature (Aneal):", temp_an)
        print("Temperature (Elong):", temp_el)
        print("Temperature (Denat):", temp_den)
        print("Temperature (Aneal):", temp_ane)

def read_from_detect():
    try:
        # Lese Daten vom Slave
        null = bus.read_byte(temp_address)
        return null
    except Exception as e:
        print("Failed to read")
        
while True:
    read_detect_null()
