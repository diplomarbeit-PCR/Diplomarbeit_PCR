import time
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

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
        self.timer.setInterval(1000)

        self.DL_zaehler_value = 0
        self.interval = 0

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

        self.timer.timeout.connect(self.run_phasen_Ablauf)  # Verbinde den Timer mit der Methode

    def phasen_Ablauf(self):
        self.hide()
        self.interval = 0  

        if self.phasen_running == False:
            self.frm_kont.showFullScreen()
            self.timer.stop()
        else:     
            self.DL_zaehler_value += 1
            self.frm_denat.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_aneal.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_sens.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_asens.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_elong.update_DL_zaehler(self.DL_zaehler_value)
            self.timer.start(1000)  # Starte den Timer mit einer Sekunde Intervall
            

    def run_phasen_Ablauf(self):
        self.timer_seconds += 1
        self.interval += 1

        self.frm_denat.Timer_zaehler.display(time.strftime('%H:%M:%S', time.gmtime(self.timer_seconds)))
        self.frm_aneal.Timer_zaehler.display(time.strftime('%H:%M:%S', time.gmtime(self.timer_seconds)))
        self.frm_sens.Timer_zaehler.display(time.strftime('%H:%M:%S', time.gmtime(self.timer_seconds)))
        self.frm_asens.Timer_zaehler.display(time.strftime('%H:%M:%S', time.gmtime(self.timer_seconds)))
        self.frm_elong.Timer_zaehler.display(time.strftime('%H:%M:%S', time.gmtime(self.timer_seconds)))

        if self.interval <= 11:
            self.frm_denat.showFullScreen()

        elif self.interval >= 12 and self.interval <= 21:
            self.frm_denat.hide()
            self.frm_aneal.showFullScreen()
        
        elif self.interval >= 22 and self.interval <= 31:
            self.frm_aneal.hide()
            self.frm_sens.showFullScreen()

        elif self.interval >= 32 and self.interval <= 41:
            self.frm_sens.hide()
            self.frm_asens.showFullScreen()
        
        elif self.interval >= 42 and self.interval <= 51:
            self.frm_asens.hide()
            self.frm_elong.showFullScreen()

        else:
            self.frm_elong.hide()
            self.phasen_Ablauf  # Nächste Iteration 

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
        self.timer.stop()
        self.timer_seconds = 0
        self.DL_zaehler_value = 0
        self.interval = 0
        self.btn_Start.clicked.disconnect(self.phasen_Ablauf)  # Disconnect the existing connection
        self.btn_Start.clicked.connect(self.phasen_Ablauf)

app = QApplication()
frm_main = Frm_main()
frm_main.showFullScreen()
app.exec()