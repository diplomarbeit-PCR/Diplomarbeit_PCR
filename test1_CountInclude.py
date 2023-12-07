from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

# Auf die unterschiedlichen WIndows zugreifen (QT Deklaration, die in Py umgewandelt wurden)
from dipl_Einfuehrung.einfuehrung_v4 import Ui_StartWindow
from dipl_Einfuehrung.Voraussetzung_v1 import Ui_Voraussetzung
from dipl_Einfuehrung.zeitDefVoraus_v1 import Ui_zeitDef_Voraus
from dipl_Phasenablauf.AblaufWindowDenat_v1 import Ui_AblaufWindowDenat
from dipl_Phasenablauf.AblaufWindowAneal_v1 import Ui_AblaufWindowAneal
from dipl_Phasenablauf.AblaufWindowSens_v1 import Ui_AblaufWindowSens
from dipl_Phasenablauf.AblaufWindowASens_v1 import Ui_AblaufWindowASens
from dipl_Phasenablauf.AblaufWindowElong_v1 import Ui_AblaufWindowElong
from dipl_Kontrolle.KontrolLWindow_v1 import Ui_Kontrolle

# Es wird eine Klasse für die Voraussetzungen erstellt
# Hierfür wird deklariert, dass ein MainWIndow verwendet wurde und es auf die Klasse Ui_Voraussetzung
class Frm_vorraus(QMainWindow, Ui_Voraussetzung):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Frm_zeitDef(QMainWindow, Ui_zeitDef_Voraus):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.wasserDauer_denat.valueChanged.connect(self.Value_Denat_change)
        self.wasserDauer_aneal.valueChanged.connect(self.Value_Aneal_change)
        self.wasserDauer_elong.valueChanged.connect(self.Value_Elong_change)

    def Value_Denat_change(self, value):
        self.value_denat = self.wasserDauer_denat.value()
        print(f"DenatWert: {value}")

    def Value_Aneal_change(self, value):
        self.value_aneal = self.wasserDauer_aneal.value() * (1/3) + self.value_denat
        self.value_sens = self.wasserDauer_aneal.value() * (1/3) + self.value_aneal
        self.value_asens = self.wasserDauer_aneal.value() * (1/3) + self.value_sens
        print(f"AnealWert: {value}")
        
    def Value_Elong_change(self, value):
        self.value_elong = self.wasserDauer_elong.value() + self.value_asens
        print(f"ElongWert: {value}")

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

        self.frm_kont.btn_Fortfuehren.clicked.connect(self.weiter)
        self.frm_kont.btn_Beenden.clicked.connect(self.esc)

        self.phasen_running = True  # Flag für den Zustand von phasen_Ablauf

        self.seconds = 0
        self.timer.timeout.connect(self.run_phasen_Ablauf)  # Verbinde den Timer mit der Methode
        
        self.phaseCount = 0
        
        
    def erlaubteDauer(self):
        self.hide()

        self.frm_vorraus.showFullScreen()
        QTimer.singleShot(10000, self.frm_vorraus.hide)
        QTimer.singleShot(10000, self.frm_zeitDef.show)


    def phasen_Ablauf(self):
        self.frm_zeitDef.hide()
        self.timer.start()

        self.frm_denat.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_aneal.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_sens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_asens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_elong.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        
        if self.phasen_running == False:
            self.frm_kont.show()
            self.timer.stop()
        
        else:
            self.run_phasen_Ablauf()
            
            self.phaseCount = 0
            
            self.DL_counter += 1 
            
            self.DL_zaehler_value += 1  
            self.frm_denat.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_aneal.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_sens.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_asens.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_elong.update_DL_zaehler(self.DL_zaehler_value)
    
    def run_phasen_Ablauf(self):
        self.timer.start(1000)  # Timer feuert alle 1000 Millisekunden (1 Sekunde)
        self.seconds += 1
        self.phaseCount += 1
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        seconds = self.seconds % 60

        self.frm_denat.Timer_zaehler.display(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        self.frm_aneal.Timer_zaehler.display(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        self.frm_sens.Timer_zaehler.display(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        self.frm_asens.Timer_zaehler.display(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        self.frm_elong.Timer_zaehler.display(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        
        def check_and_show(phase, start, end):
            if start < self.phaseCount <= end:
                phase.show()
            else:
                phase.hide()

        check_and_show(self.frm_denat, 0, self.frm_zeitDef.value_denat)
        check_and_show(self.frm_aneal, self.frm_zeitDef.value_denat, self.frm_zeitDef.value_aneal)
        check_and_show(self.frm_sens, self.frm_zeitDef.value_aneal, self.frm_zeitDef.value_sens)
        check_and_show(self.frm_asens, self.frm_zeitDef.value_sens, self.frm_zeitDef.value_asens)
        check_and_show(self.frm_elong, self.frm_zeitDef.value_asens, self.frm_zeitDef.value_elong)

            
        if self.DL_counter == 10:
            self.phasen_running = False
            self.DL_counter = 0
            
        if self.phaseCount > (self.frm_zeitDef.value_elong):
            self.phaseCount = 0
            self.phasen_Ablauf()

    def kontroll_Erklaerung(self):
        self.phasen_running = False  # Stoppe phasen_Ablauf
        self.DL_counter = 0

    def weiter(self):
        self.phasen_running = True   # Starte phasen_Ablauf
        self.frm_kont.hide()
        self.phasen_Ablauf()

    def esc(self):
        self.frm_kont.hide()
        frm_main.show()
        self.phasen_running = True
        self.timer.stop()
        self.seconds = 0
        self.DL_zaehler_value = 0
        self.frm_zeitDef.wasserDauer_denat.setValue(35)
        self.frm_zeitDef.wasserDauer_aneal.setValue(45)
        self.frm_zeitDef.wasserDauer_elong.setValue(40)

        self.btn_Start.disconnect(self.erlaubteDauer) 
        self.btn_Start.clicked.connect(self.erlaubteDauer)
        
        self.frm_zeitDef.btn_Weiter.disconnect(self.phasen_Ablauf)
        self.frm_zeitDef.btn_Weiter.clicked.connect(self.phasen_Ablauf)

app = QApplication()
frm_main = Frm_main()
frm_main.showFullScreen()
app.exec()