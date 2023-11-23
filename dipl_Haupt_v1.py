from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

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

class Frm_sens(QMainWindow, Ui_AblaufWindowAneal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Frm_asens(QMainWindow, Ui_AblaufWindowAneal):
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

        self.btn_Start.clicked.connect(self.phasen_Ablauf)

    def phasen_Ablauf(self):
        frm_main.hide()
        frm_denat.show()
        QTimer.singleShot(10000, frm_denat.hide)  # Verzögerung von 5000 ms (5 Sekunden)
        QTimer.singleShot(10000, frm_aneal.show)  # Verzögerung von 10000 ms (10 Sekunden)
        QTimer.singleShot(20000, frm_aneal.hide)  # Verzögerung von 15000 ms (15 Sekunden)
        QTimer.singleShot(10000, frm_sens.show)  # Verzögerung von 10000 ms (10 Sekunden)
        QTimer.singleShot(20000, frm_sens.hide)  # Verzögerung von 15000 ms (15 Sekunden)
        QTimer.singleShot(10000, frm_asens.show)  # Verzögerung von 10000 ms (10 Sekunden)
        QTimer.singleShot(20000, frm_asens.hide)  # Verzögerung von 15000 ms (15 Sekunden)
        QTimer.singleShot(20000, frm_elong.show)  # Verzögerung von 20000 ms (20 Sekunden)

app = QApplication()
frm_main = Frm_main()
frm_main.show()
frm_denat = Frm_denat()
frm_aneal = Frm_aneal()
frm_elong = Frm_elong()
app.exec()
