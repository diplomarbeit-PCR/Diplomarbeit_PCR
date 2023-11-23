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

        self.btn_Start.clicked.connect(self.phasen_Ablauf)

    def phasen_Ablauf(self):
        frm_main.hide()
        frm_denat.show()
        QTimer.singleShot(10000, frm_denat.hide)  
        QTimer.singleShot(10000, frm_aneal.show)  
        QTimer.singleShot(20000, frm_aneal.hide)  
        QTimer.singleShot(20000, frm_sens.show)  
        QTimer.singleShot(30000, frm_sens.hide)  
        QTimer.singleShot(30000, frm_asens.show)  
        QTimer.singleShot(40000, frm_asens.hide) 
        QTimer.singleShot(40000, frm_elong.show)  

app = QApplication()
frm_main = Frm_main()
frm_main.show()
frm_denat = Frm_denat()
frm_aneal = Frm_aneal()
frm_sens = Frm_sens()
frm_asens = Frm_asens()
frm_elong = Frm_elong()
app.exec()
