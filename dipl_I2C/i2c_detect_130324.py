import smbus
import time

# Definieren Sie die Adresse des Arduinos auf dem I2C-Bus
detect_address = 0x10 # Beispieladresse, ersetzen Sie sie durch die tatsächliche Slave-Adresse

# Öffnen Sie den I2C-Bus (abhängig von Ihrem System kann die Busnummer variieren)
bus = smbus.SMBus(7)  # Bus 1 öffnen, Sie können die richtige Busnummer je nach Ihrem Setup anpassen

def wait_start():
    data_sent = False  # Hält den Zustand, ob die Daten gesendet wurden
    stopped_reading = False  # Hält den Zustand, ob der Leseprozess gestoppt wurde
    i = 0
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    p6 = 0
    p7 = 0
    p8 = 0

    print("Warte auf Start...")
    
    while not stopped_reading:
        print("Senden der Daten ... ")
        print(read_from_detect())
        detect_receive = read_from_detect()

        if detect_receive[0] == 0 and detect_receive[1] == 7 and not data_sent:
                data_sent = True

            # Überprüfen Sie die empfangenen Daten und handeln Sie entsprechend
        if detect_receive[0] == 0 and detect_receive[1] == 5 and not data_sent:
                data_sent = True
                print("Startsignal empfangen. Senden von Daten an den Slave...")
                write_to_detect(10)

    if stopped_reading:
        time(1000)
        detect_receive = read_from_detect()
        if detect_receive[0] == 1:
                # Die erhaltenen Daten anzeigen
                p1 == detect_receive[1]
                write_to_detect(2)

        if detect_receive[0] == 2:
                p2 == detect_receive[1]
                write_to_detect(3)

        if detect_receive[0] == 3:
                p3 == detect_receive[1]
                write_to_detect(4)

        if detect_receive[0] == 4:
                p4 == detect_receive[1]
                write_to_detect(5)

        if detect_receive[0] == 5:
                p5 == detect_receive[1]
                write_to_detect(6)

        if detect_receive[0] == 6:
                p6 == detect_receive[1]
                write_to_detect(7)

        if detect_receive[0] == 7:
                p7 == detect_receive[1]
                write_to_detect(8)

        if detect_receive[0] == 8:
                p8 == detect_receive[1]
                stopped_reading = True  # Leseprozess stoppen
                write_to_detect(9)

        
        

    # try:
        
    #     while not stopped_reading:
    #         # Lesen Sie Daten vom Slave, wenn der Leseprozess nicht gestoppt wurde
    #         detect_receive = read_from_detect()

    #         if detect_receive[0] == 0 and detect_receive[1] == 7 and not data_sent:
    #             data_sent = True

    #         # Überprüfen Sie die empfangenen Daten und handeln Sie entsprechend
    #         if detect_receive[0] == 0 and detect_receive[1] == 5 and not data_sent:
    #             data_sent = True
    #             print("Startsignal empfangen. Senden von Daten an den Slave...")
    #             write_to_detect(10)

    #         if detect_receive[0] == 1:
    #             # Die erhaltenen Daten anzeigen
    #             p1 == detect_receive[1]
    #             write_to_detect(2)

    #         if detect_receive[0] == 2:
    #             p2 == detect_receive[1]
    #             write_to_detect(3)

    #         if detect_receive[0] == 3:
    #             p3 == detect_receive[1]
    #             write_to_detect(4)

    #         if detect_receive[0] == 4:
    #             p4 == detect_receive[1]
    #             write_to_detect(5)

    #         if detect_receive[0] == 5:
    #             p5 == detect_receive[1]
    #             write_to_detect(6)

    #         if detect_receive[0] == 6:
    #             p6 == detect_receive[1]
    #             write_to_detect(7)

    #         if detect_receive[0] == 7:
    #             p7 == detect_receive[1]
    #             write_to_detect(8)

    #         if detect_receive[0] == 8:
    #             p8 == detect_receive[1]
    #             stopped_reading = True  # Leseprozess stoppen
    #             write_to_detect(9)

    #         return p1,p2,p3,p4,p5,p6,p7,p8

    # except Exception as e:
    #     print(f"Fehler aufgetreten: {str(e)}")
    # finally:
    #     # Hier könnten Sie Aufräumarbeiten durchführen, falls erforderlich
    #     pass

def write_to_detect(data):
    try:
        # Schreiben Sie Daten an den Slave
        bus.write_byte(detect_address, data)
    except Exception as e:
        print(f"Fehler beim Senden von Daten an den Slave: {str(e)}")

def read_from_detect():
    try:
        # Lesen Sie Daten vom Slave (wir erwarten 2 Datenpunkte)
        return [bus.read_byte(detect_address) for _ in range(2)]
    except Exception as e:
        print(f"Fehler beim Lesen von Daten vom Slave: {str(e)}")

if __name__ == "__main__":
    wait_start()
