from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

import time
import math

from dipl_Einfuehrung.einfuehrung_v4 import Ui_StartWindow
from dipl_Einfuehrung.Vorraussetzung_v1 import Ui_Vorraussetzung, QPixmap
from dipl_Einfuehrung.zeitDefVorraus_v1 import Ui_zeitDef_Voraus
from dipl_Phasenablauf.AblaufWindowDenat_v1 import Ui_AblaufWindowDenat
from dipl_Phasenablauf.AblaufWindowAneal_v1 import Ui_AblaufWindowAneal
from dipl_Phasenablauf.AblaufWindowSens_v1 import Ui_AblaufWindowSens
from dipl_Phasenablauf.AblaufWindowASens_v1 import Ui_AblaufWindowASens
from dipl_Phasenablauf.AblaufWindowElong_v1 import Ui_AblaufWindowElong
from dipl_Kontrolle.KontrolLWindow_v1 import Ui_Kontrolle

class Frm_vorraus(QMainWindow, Ui_Vorraussetzung):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Vorraus_lbl.setPixmap(QPixmap(u"pcrGrundprinzip.jpg"))

class Frm_zeitDef(QMainWindow, Ui_zeitDef_Voraus):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.wasserDauer_aneal = self.wasserDauer_anealing.value() * (1/3)
        self.wasserDauer_sens = self.wasserDauer_anealing.value() * (2/3)
        self.wasserDauer_asens = self.wasserDauer_anealing.value()

class Frm_denat(QMainWindow, Ui_AblaufWindowDenat):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Timer_zaehler.display("00:00:00")

    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

class Frm_aneal(QMainWindow, Ui_AblaufWindowAneal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Timer_zaehler.display("00:00:00")

    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

class Frm_sens(QMainWindow, Ui_AblaufWindowSens):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Timer_zaehler.display("00:00:00")

    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

class Frm_asens(QMainWindow, Ui_AblaufWindowASens):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Timer_zaehler.display("00:00:00")

    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

class Frm_elong(QMainWindow, Ui_AblaufWindowElong):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Timer_zaehler.display("00:00:00")

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

        self.timer_seconds = 0
        self.timer = QTimer()

        self.DL_zaehler_value = 0
        self.DL_counter = 0

        self.frm_vorraus = Frm_vorraus()
        self.frm_zeitDef = Frm_zeitDef()
        self.frm_denat = Frm_denat()
        self.frm_aneal = Frm_aneal()
        self.frm_sens = Frm_sens()
        self.frm_asens = Frm_asens()
        self.frm_elong = Frm_elong()
        self.frm_kont = Frm_kont()
         
        self.btn_Start.clicked.connect(self.erlaubteDauer)

        self.frm_zeitDef.btn_Weiter.clicked.connect(self.phasen_Ablauf)

        self.frm_denat.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_aneal.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_sens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_asens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_elong.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)

        self.frm_kont.btn_Fortfuehren.clicked.connect(self.weiter)
        self.frm_kont.btn_Beenden.clicked.connect(self.esc)

        self.phasen_running = True  # Flag für den Zustand von phasen_Ablauf

    def erlaubteDauer(self):
        self.hide()

        self.frm_vorraus.showFullScreen()
        QTimer.singleShot(10000, self.frm_vorraus.hide)
        QTimer.singleShot(10000, self.frm_zeitDef.showFullScreen)


    def phasen_Ablauf(self):
        self.frm_zeitDef.hide()
        
        if self.phasen_running == False:
            self.frm_kont.show()
        
        else:
            self.run_phasen_Ablauf()
    
    def run_phasen_Ablauf(self):
        self.DL_zaehler_value += 1  
        self.frm_denat.update_DL_zaehler(self.DL_zaehler_value)
        self.frm_aneal.update_DL_zaehler(self.DL_zaehler_value)
        self.frm_sens.update_DL_zaehler(self.DL_zaehler_value)
        self.frm_asens.update_DL_zaehler(self.DL_zaehler_value)
        self.frm_elong.update_DL_zaehler(self.DL_zaehler_value)

        self.DL_counter += 1 

        self.frm_denat.show()
        self.timer.singleShot(self.frm_zeitDef.wasserDauer_denat, self.frm_denat.hide)
        self.timer.singleShot(self.frm_zeitDef.wasserDauer_denat, self.frm_aneal.show)
        self.timer.singleShot(self.frm_zeitDef.wasserDauer_aneal, self.frm_aneal.hide)
        self.timer.singleShot(self.frm_zeitDef.wasserDauer_aneal, self.frm_sens.show)
        self.timer.singleShot(self.frm_zeitDef.wasserDauer_sens, self.frm_sens.hide)
        self.timer.singleShot(self.frm_zeitDef.wasserDauer_sens, self.frm_asens.show)
        self.timer.singleShot(self.frm_zeitDef.wasserDauer_asens, self.frm_asens.hide)
        self.timer.singleShot(self.frm_zeitDef.wasserDauer_asens, self.frm_elong.show)
        self.timer.singleShot(self.frm_zeitDef.wasserDauer_elong, self.frm_elong.hide)
        
        self.timer.singleShot(self.frm_zeitDef.wasserDauer_elong, self.phasen_Ablauf)  # Nächste Iteration 

        if self.DL_counter == 10:
            self.phasen_running = False
            self.DL_counter = 0

    def kontroll_Erklaerung(self):
        self.phasen_running = False  # Stoppe phasen_Ablauf
        self.timer.stop()

    def weiter(self):
        self.phasen_running = True   # Starte phasen_Ablauf
        self.frm_kont.hide()
        self.phasen_Ablauf()

    def esc(self):
        self.frm_kont.hide()
        frm_main.show()
        self.phasen_running = True
        self.timer.stop()
        self.timer_seconds = 0
        self.DL_zaehler_value = 0
        self.btn_Start.clicked.disconnect(self.phasen_Ablauf)  # Disconnect the existing connection
        self.btn_Start.clicked.connect(self.phasen_Ablauf)

app = QApplication()
frm_main = Frm_main()
frm_main.showFullScreen()
app.exec()