import smbus
import time

# Definieren Sie die Adresse des Arduinos auf dem I2C-Bus
temp_address = 0x12  # Beispieladresse, ersetzen Sie sie durch die tatsächliche Slave-Adresse

# Öffnen Sie den I2C-Bus (abhängig von Ihrem System kann die Busnummer variieren)
bus = smbus.SMBus(7)  # Bus 1 öffnen, Sie können die richtige Busnummer je nach Ihrem Setup anpassen

# Funktion zum Lesen von Daten vom Arduino
def read_data():
    data = []
    for _ in range(8):  # Wir erwarten 3 Datenpunkte (temp_denat, temp_aneal, temp_elong)
        data.append(bus.read_byte(temp_address))
    return data

# Daten vom Arduino lesen
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