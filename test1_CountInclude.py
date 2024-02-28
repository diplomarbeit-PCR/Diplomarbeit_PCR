import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QTimer, Signal, QObject
import smbus
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from dipl_Einfuehrung.WarteWindow_v1 import Ui_WarteWindow 

# https://prod.liveshare.vsengsaas.visualstudio.com/join?31FC76570F4708D5644412F5BE43DF2DDEF7

# Definition der I2C-Kommunikationsklasse
class I2CController(QObject):
    i2c_operation_requested = Signal(int)

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

        self.i2c_controller = I2CController()  # I2C-Controller erstellen
        self.lbl_loading = QLabel(self)
        self.lbl_loading.setGeometry(90, 380, 411, 291)
        self.lbl_loading.setStyleSheet("font-size: 250px;")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_loading_animation)
        self.counter = 0
           
    def update_loading_animation(self):
        self.counter = (self.counter + 1) % 5
        loading_text = "." * self.counter
        self.lbl_loading.setText(loading_text)
        
