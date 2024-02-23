import sys
import smbus
import time

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton
from PySide6.QtCore import Qt, Signal, QObject

# Definition der I2C-Kommunikationsklasse
class I2CController:
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