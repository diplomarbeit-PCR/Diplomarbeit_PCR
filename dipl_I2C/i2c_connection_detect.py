import smbus
import time

# Definieren Sie die Adresse des Arduino-Slave auf dem I2C-Bus
detect_address = 0x06  # Beispieladresse, ersetzen Sie sie durch die tatsächliche Slave-Adresse

# Öffnen Sie den I2C-Bus (abhängig von Ihrem System kann die Busnummer variieren)
bus = smbus.SMBus(7)  # Bus 1 öffnen, Sie können die richtige Busnummer je nach Ihrem Setup anpassen


# def read_data_from_data(self):
#     # Nur Daten vom Slave lesen, wenn der Leseprozess nicht gestoppt wurde
#     if not self.stopped_reading:
#         try:
#             if self.i == 0:
#                 data = self.read_from_beweg()
#                 if data is None:             
#                     data = self.read_from_beweg()

#                 if data == 7:
#                     data = self.read_from_beweg()
                        
#                 if data == 0:
#                     data = self.read_from_beweg()

#                 if data == 5 and not self.data_sent:
#                     self.data_sent = True
#                     print("5 erhalten")
#                     self.stopped_reading = True  # Leseprozess stoppen
                    
                        
#         except Exception as e:
#             print(f"Fehler beim Lesen von Daten vom Slave: {str(e)}")

def write_to_data(self, data):
        try:
            # Schreibe Daten an den Slave
            self.bus.write_byte(self.detect_address, data)
            print(f"Daten {data} erfolgreich an Slave gesendet.")
        except Exception as e:
            print(f"Fehler beim Senden von Daten an den Slave: {str(e)}")

def read_from_detect(self):
    data = []
    for _ in range(3):  # Wir erwarten 3 Datenpunkte (temp_denat, temp_aneal, temp_elong)
        data.append(bus.read_byte(detect_address))
    return data

time.sleep(10)

write_to_data(4)

time.sleep(10)

# Daten vom Arduino lesen
data_received = read_from_detect()

value_spg = data_received[0] 
value_light = data_received[1] 

# Die erhaltenen Daten anzeigen
print("Messwerte")
print("SPG:", value_spg)
print("Licht:", value_light)