import smbus
import time

# Definieren Sie die Adresse des Arduino-Slave auf dem I2C-Bus
detect_address = 0x06  # Beispieladresse, ersetzen Sie sie durch die tatsächliche Slave-Adresse

# Öffnen Sie den I2C-Bus (abhängig von Ihrem System kann die Busnummer variieren)
bus = smbus.SMBus(7)  # Bus 1 öffnen, Sie können die richtige Busnummer je nach Ihrem Setup anpassen


def read_data_from_data(self):
    # Nur Daten vom Slave lesen, wenn der Leseprozess nicht gestoppt wurde
    if not self.stopped_reading:
        try:
            if self.i == 0:
                data = self.read_from_beweg()
                if data is None:             
                    data = self.read_from_beweg()

                if data == 7:
                    data = self.read_from_beweg()
                        
                if data == 0:
                    data = self.read_from_beweg()

                if data == 5 and not self.data_sent:
                    self.data_sent = True
                    print("5 erhalten")
                    self.stopped_reading = True  # Leseprozess stoppen
                    
                        
        except Exception as e:
            print(f"Fehler beim Lesen von Daten vom Slave: {str(e)}")

def write_to_data(self, data):
        try:
            # Schreibe Daten an den Slave
            self.bus.write_byte(self.detect_address, data)
            print(f"Daten {data} erfolgreich an Slave gesendet.")
        except Exception as e:
            print(f"Fehler beim Senden von Daten an den Slave: {str(e)}")

def read_from_detect(self):
        try:
            # Lese Daten vom Slave
            data = self.bus.read_byte(self.beweg_address)
            return data
        except Exception as e:
            print(f"Fehler")