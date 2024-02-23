import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Signal, QObject
import smbus
import time

# Definition der I2C-Kommunikationsklasse
class I2CController(QObject):
    i2c_operation_requested = Signal(int)

    def __init__(self):
        super().__init__()
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
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("I2C GUI Beispiel")
        self.setGeometry(100, 100, 400, 200)

        self.i2c_controller = I2CController()

        self.btn_send_data = QPushButton("Daten an Slave senden", self)
        self.btn_send_data.setGeometry(50, 50, 200, 50)
        self.btn_send_data.clicked.connect(self.send_data_to_slave)

        self.btn_read_data = QPushButton("Daten vom Slave lesen", self)
        self.btn_read_data.setGeometry(50, 120, 200, 50)
        self.btn_read_data.clicked.connect(self.read_data_from_slave)

        self.data_sent = False  # Hält den Zustand, ob die Daten gesendet wurden

    def send_data_to_slave(self):
        # Hier wird die Methode zum Senden von Daten an den Slave aufgerufen
        self.i2c_controller.write_to_slave(1)

    def read_data_from_slave(self):
        # Hier wird die Methode zum Lesen von Daten vom Slave aufgerufen
        data = self.i2c_controller.read_from_slave()
        if data == 5 and not self.data_sent:
            self.data_sent = True
            # Hier könnten Sie die gewünschten Daten an den Slave senden
            self.i2c_controller.write_to_slave(10)  # Beispielwert 10 für Daten, die an den Slave gesendet werden sollen
        elif data is not None:
            # Hier könnten Sie die empfangenen Daten weiter verarbeiten oder anzeigen
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
