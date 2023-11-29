from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import smbus2

from dipl_Einfuehrung.einfuehrung_v4 import Ui_StartWindow
from dipl_Phasenablauf.AblaufWindowDenat_v1 import Ui_AblaufWindowDenat
from dipl_Phasenablauf.AblaufWindowAneal_v1 import Ui_AblaufWindowAneal
from dipl_Phasenablauf.AblaufWindowSens_v1 import Ui_AblaufWindowSens
from dipl_Phasenablauf.AblaufWindowASens_v1 import Ui_AblaufWindowASens
from dipl_Phasenablauf.AblaufWindowElong_v1 import Ui_AblaufWindowElong
from dipl_Kontrolle.KontrolLWindow_v1 import Ui_Kontrolle

class Frm_denat(QMainWindow, Ui_AblaufWindowDenat):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

class Frm_aneal(QMainWindow, Ui_AblaufWindowAneal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

class Frm_sens(QMainWindow, Ui_AblaufWindowSens):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

class Frm_asens(QMainWindow, Ui_AblaufWindowASens):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

class Frm_elong(QMainWindow, Ui_AblaufWindowElong):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

class Frm_kont(QMainWindow, Ui_Kontrolle):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Frm_main(QMainWindow, Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.DL_zaehler_value = 0
        self.arduino_address = 8  # I2C-Adresse des Arduinos
        self.bus = smbus2.SMBus(1)  # Abhängig von deinem System, möglicherweise ist 0 anstelle von 1 erforderlich

        self.frm_denat = Frm_denat()
        self.frm_aneal = Frm_aneal()
        self.frm_sens = Frm_sens()
        self.frm_asens = Frm_asens()
        self.frm_elong = Frm_elong()
        self.frm_kont = Frm_kont()

        self.btn_Start.clicked.connect(self.phasen_Ablauf)

        self.frm_denat.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_aneal.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_sens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_asens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_elong.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)

        self.frm_kont.btn_Fortfuehren.clicked.connect(self.weiter)
        self.frm_kont.btn_Beenden.clicked.connect(self.esc)

        self.phasen_running = True  # Flag für den Zustand von phasen_Ablauf

    def phasen_Ablauf(self):
        self.hide()
        taster_value = 1
        self.send_data_to_arduino(taster_value)
        
        if self.phasen_running == False:
            self.frm_kont.show()
        else:
            self.run_phasen_Ablauf()

    def run_phasen_Ablauf(self):
        try:
            
            self.DL_zaehler_value += 1  
            self.frm_denat.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_aneal.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_sens.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_asens.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_elong.update_DL_zaehler(self.DL_zaehler_value)

            self.frm_denat.show()
            QTimer.singleShot(10000, self.frm_denat.hide)
            QTimer.singleShot(10000, self.frm_aneal.show)
            QTimer.singleShot(20000, self.frm_aneal.hide)
            QTimer.singleShot(20000, self.frm_sens.show)
            QTimer.singleShot(30000, self.frm_sens.hide)
            QTimer.singleShot(30000, self.frm_asens.show)
            QTimer.singleShot(40000, self.frm_asens.hide)
            QTimer.singleShot(40000, self.frm_elong.show)
            QTimer.singleShot(50000, self.frm_elong.hide)
            
            QTimer.singleShot(50000, self.phasen_Ablauf)  # Nächste Iteration
        except Exception as e:
            print(f'Fehler bei der I2C-Kommunikation: {e}')

    def send_data_to_arduino(self, data):
        self.bus.write_byte(self.arduino_address, data)
        print(f'Daten an Arduino gesendet: {data}')

    def kontroll_Erklaerung(self):
        self.phasen_running = False  # Stoppe phasen_Ablauf

    def weiter(self):
        self.phasen_running = True   # Starte phasen_Ablauf
        self.frm_kont.hide()
        self.phasen_Ablauf()

    def esc(self):
        self.frm_kont.hide()
        frm_main.show()
        self.phasen_running = True
        self.DL_zaehler_value = 0
        self.btn_Start.clicked.disconnect(self.phasen_Ablauf)  # Disconnect the existing connection
        self.btn_Start.clicked.connect(self.phasen_Ablauf)

if __name__ == '__main__':
    app = QApplication()
    frm_main = Frm_main()
    frm_main.show()
    app.exec()
