import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QTimer, Signal
import smbus

<<<<<<< HEAD
# https://prod.liveshare.vsengsaas.visualstudio.com/join?682BAC6E36B5C0119F9065998ED1172CB089
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from dipl_Einfuehrung.WarteWindow_v1 import Ui_WarteWindow  

# Definition der I2C-Kommunikationsklasse
class I2CController(QObject):
    i2c_operation_requested = Signal(int)

=======
from dipl_Einfuehrung.WarteWindow_v1 import Ui_WarteWindow


# Definition der I2C-Kommunikationsklasse
class I2CController:
>>>>>>> bcb7fe2849652a972df68d7493ab313a49e0277d
    def __init__(self):
        # Öffne den I2C-Bus 7
        self.bus = smbus.SMBus(7)
        # Adresse des Slave-Geräts
        self.address = 0x04

    def write_to_slave(self, data):
        try:
            # Schreibe Daten an den Slave
            self.bus.write_byte(self.address, data)
            print(f"Daten {data} erfolgreich an Slave gesendet.")
        except Exception as e:
            print(f"Fehler beim Senden von Daten an den Slave: {str(e)}")

    def read_from_slave(self):
        try:
            # Lese Daten vom Slave
            data = self.bus.read_byte(self.address)
            print(f"Daten vom Slave gelesen: {data}")
            return data
        except Exception as e:
            print(f"Fehler beim Lesen von Daten vom Slave: {str(e)}")
            return None

# Hauptfenster der Anwendung
class Frm_WarteWindow(QMainWindow, Ui_WarteWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_WarteWindow()
        self.ui.setupUi(self)

        self.i = 0
        self.i2c_controller = I2CController()  # I2C-Controller erstellen
        self.data_sent = False  # Hält den Zustand, ob die Daten gesendet wurden
        self.lbl_loading = QLabel(self)
        self.lbl_loading.setGeometry(90, 380, 411, 291)
        self.lbl_loading.setStyleSheet("font-size: 250px;")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_loading_animation)
        self.timer.start(500)  # Update every 500 milliseconds
        self.counter = 0
        self.stopped_reading = False  # Hält den Zustand, ob der Leseprozess gestoppt wurde

    def update_loading_animation(self):
        self.counter = (self.counter + 1) % 5
        loading_text = "." * self.counter
        self.lbl_loading.setText(loading_text)
        
        if not self.stopped_reading:
            print("lese Fkt")
            self.read_data_from_slave()


    def send_data_to_slave(self):
        # Hier wird die Methode zum Senden von Daten an den Slave aufgerufen
        self.i2c_controller.write_to_slave(1)

    def read_data_from_slave(self):
    # Nur Daten vom Slave lesen, wenn der Leseprozess nicht gestoppt wurde
        if not self.stopped_reading:
            try:
                data = self.i2c_controller.read_from_slave()
                if data is None:             
                    data = self.i2c_controller.read_from_slave()

                if data == 7:
                    print("7")
                    data = self.i2c_controller.read_from_slave()
                    
                if data == 0:
                    print("0")
                    data = self.i2c_controller.read_from_slave()

                if data == 5 and not self.data_sent:
                    self.data_sent = True
                    print("5 erhalten")
                    self.i += 1
                    print(self.i)
                    # Hier könnten Sie die gewünschten Daten an den Slave senden
                    self.i2c_controller.write_to_slave(10)  # Beispielwert 10 für Daten, die an den Slave gesendet werden sollen
                    self.stopped_reading = True  # Leseprozess stoppen
                    self.close()
            except Exception as e:
                print(f"Fehler beim Lesen von Daten vom Slave: {str(e)}")


