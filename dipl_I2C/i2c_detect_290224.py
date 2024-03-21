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

    self.p1 = 0
    self.p2 = 0
    self.p3 = 0
    self.p4 = 0
    self.p5 = 0
    self.p6 = 0
    self.p7 = 0
    self.p8 = 0
    
    
    write_to_detect(10)
       
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
                    write_to_detect(10)
                    print(self.i)
                    # Hier könnten Sie die gewünschten Daten an den Slave senden
                    self.stopped_reading = True  # Leseprozess stoppen

                if detect_receive[0] == 1:
                    # Die erhaltenen Daten anzeigen
                    self.p1 == detect_receive[1]
                    write_to_detect(2)

                if detect_receive[0] == 2:
                    self.p2 == detect_receive[1]
                    write_to_detect(3)

                if detect_receive[0] == 3:
                    self.p3 == detect_receive[1]
                    write_to_detect(4)

                if detect_receive[0] == 4:
                    self.p4 == detect_receive[1]
                    write_to_detect(5)

                if detect_receive[0] == 5:
                    self.p5 == detect_receive[1]
                    write_to_detect(6)

                if detect_receive[0] == 6:
                    self.p6 == detect_receive[1]
                    write_to_detect(7)

                if detect_receive[0] == 7:
                    self.p7 == detect_receive[1]
                    write_to_detect(8)

                if detect_receive[0] == 8:
                    self.p8 == detect_receive[1]
                    write_to_detect(9)
                    
                        
        except Exception as e:
            print(f"Fehler beim Lesen von Daten vom Slave: {str(e)}")

def write_to_detect(data):
    try:
        # Schreibe Daten an den Slave
        bus.write_byte(detect_address, data)
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



