from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, QTimer

from dipl_Einfuehrung.einfuehrung_v3 import Ui_StartWindow
from dipl_Phasenablauf.AblaufWindowDenat_v1 import Ui_AblaufWindowDenat
from dipl_Phasenablauf.AblaufWindowAneal_v1 import Ui_AblaufWindowAneal
from dipl_Phasenablauf.AblaufWindowSens_v1 import Ui_AblaufWindowSens
from dipl_Phasenablauf.AblaufWindowASens_v1 import Ui_AblaufWindowASens
from dipl_Phasenablauf.AblaufWindowElong_v1 import Ui_AblaufWindowElong

class Frm_denat(QMainWindow, Ui_AblaufWindowDenat):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Frm_aneal(QMainWindow, Ui_AblaufWindowAneal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Frm_sens(QMainWindow, Ui_AblaufWindowSens):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Frm_asens(QMainWindow, Ui_AblaufWindowASens):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Frm_elong(QMainWindow, Ui_AblaufWindowElong):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
class Frm_main(QMainWindow, Ui_StartWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.frm_denat = Frm_denat()
        self.frm_aneal = Frm_aneal()
        self.frm_sens = Frm_sens()
        self.frm_asens = Frm_asens()
        self.frm_elong = Frm_elong()
         
        self.btn_Start.clicked.connect(self.phasen_Ablauf)
        self.frm_denat.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_aneal.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_sens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_asens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_elong.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)

        self.phasen_running = False  # Flag für den Zustand von phasen_Ablauf

    def phasen_Ablauf(self):
        self.hide()
        self.phasen_running = True  # Starte phasen_Ablauf
        self.run_phasen_Ablauf()

    def run_phasen_Ablauf(self):
        #if not self.phasen_running:
         #   return
        
        self.frm_denat.show()
        QTimer.singleShot(1000, self.frm_denat.hide)
        QTimer.singleShot(1000, self.frm_aneal.show)
        QTimer.singleShot(2000, self.frm_aneal.hide)
        QTimer.singleShot(2000, self.frm_sens.show)
        QTimer.singleShot(3000, self.frm_sens.hide)
        QTimer.singleShot(3000, self.frm_asens.show)
        QTimer.singleShot(4000, self.frm_asens.hide)
        QTimer.singleShot(4000, self.frm_elong.show)
        QTimer.singleShot(5000, self.frm_elong.hide)

        if self.phasen_running == False:
            QTimer.singleShot(5000, self.show)

        else:
            QTimer.singleShot(5000, self.run_phasen_Ablauf)  # Nächste Iteration

    def kontroll_Erklaerung(self):
        self.phasen_running = False  # Stoppe phasen_Ablauf


app = QApplication()
frm_main = Frm_main()
frm_main.show()
app.exec()