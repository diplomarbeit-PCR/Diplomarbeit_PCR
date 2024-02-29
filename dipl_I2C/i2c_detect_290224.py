import smbus
import time

# Definieren Sie die Adresse des Arduinos auf dem I2C-Bus
detect_address = 0x06 # Beispieladresse, ersetzen Sie sie durch die tatsächliche Slave-Adresse

# Öffnen Sie den I2C-Bus (abhängig von Ihrem System kann die Busnummer variieren)
bus = smbus.SMBus(7)  # Bus 1 öffnen, Sie können die richtige Busnummer je nach Ihrem Setup anpassen

def WarteStart(self):
      
    self.data_sent = False  # Hält den Zustand, ob die Daten gesendet wurden
    self.stopped_reading = False  # Hält den Zustand, ob der Leseprozess gestoppt wurde
    self.i = 0

    print ("show WW")
    print("Senden der Daten ...")
    print ("hide Zeit")
            
       
    while not self.stopped_reading:
        self.frm_ww.showFullScreen()
        print("Senden der Daten ... ")
        print(self.read_data_from_detect())
        self.read_data_from_detect()

    if self.stopped_reading:
        self.timer.stop()  # Stoppen Sie den Timer, da der Leseprozess gestoppt wurde
        print("Leseprozess gestoppt.")

def read_data_from_detect(self):
    # Nur Daten vom Slave lesen, wenn der Leseprozess nicht gestoppt wurde
    if not self.stopped_reading:
        try:
            if self.i == 0:
                detect_receive = self.read_from_detect()
                        
                if detect_receive[0] == 0 and detect_receive[1] == 7:
                    detect_receive = self.read_from_detect()

                if detect_receive[0] == 0 and detect_receive[1] == 5 and not self.data_sent:
                    self.data_sent = True
                    print("5 erhalten")
                    self.i += 1
                    print(self.i)
                    # Hier könnten Sie die gewünschten Daten an den Slave senden
                    self.stopped_reading = True  # Leseprozess stoppen

                if detect_receive[0] != 0:
                    self.value_spg = detect_received[0] 
                    self.value_light = detect_received[1] 

                    # Die erhaltenen Daten anzeigen
                    print("Messwerte")
                    print("SPG:", self.value_spg)
                    print("Licht:", self.value_light)
                    self.data_sent = True
                    self.stopped_reading = True  # Leseprozess stoppen
                        
        except Exception as e:
            print(f"Fehler beim Lesen von Daten vom Slave: {str(e)}")

def write_to_detect(self, data):
    try:
        # Schreibe Daten an den Slave
        self.bus.write_byte(self.detect_address, data)
        print(f"Daten {data} erfolgreich an Slave gesendet.")
    except Exception as e:
        print(f"Fehler beim Senden von Daten an den Slave: {str(e)}")


# Funktion zum Lesen von Daten vom Arduino
def read_from_detect():
    data = []
    for _ in range(2):  # Wir erwarten 2 Datenpunkte 
        data.append(bus.read_byte(detect_address))
    return data

# Daten vom Arduino lesen
detect_received = read_from_detect()



