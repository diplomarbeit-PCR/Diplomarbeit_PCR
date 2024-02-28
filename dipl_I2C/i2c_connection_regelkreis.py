import smbus
import time

# Definieren Sie die Adresse des Arduinos auf dem I2C-Bus
temp_address = 0x12  # Beispieladresse, ersetzen Sie sie durch die tatsächliche Slave-Adresse

# Öffnen Sie den I2C-Bus (abhängig von Ihrem System kann die Busnummer variieren)
bus = smbus.SMBus(7)  # Bus 1 öffnen, Sie können die richtige Busnummer je nach Ihrem Setup anpassen

# Funktion zum Lesen von Daten vom Arduino
def read_data():
    data = []
    for _ in range(3):  # Wir erwarten 3 Datenpunkte (temp_denat, temp_aneal, temp_elong)
        data.append(bus.read_byte(temp_address))
    return data

# Daten vom Arduino lesen
data_received = read_data()

temp_denat = data_received[0] 
temp_aneal = data_received[1] 
temp_elong = data_received[2] 

# Die erhaltenen Daten anzeigen
print("Temperaturen")
print("Temperature (Denat):", temp_denat)
print("Temperature (Aneal):", temp_aneal)
print("Temperature (Elong):", temp_elong)
