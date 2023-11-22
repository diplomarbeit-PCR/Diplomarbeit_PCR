from PySide6.QtWidgets import QApplication, QMainWindow
import time

from dipl_Einfuehrung.einfuehrung_v3 import Ui_StartWindow
from dipl_Phasenablauf.AblaufWindowDenat_v1 import Ui_AblaufWindowDenat
from dipl_Phasenablauf.AblaufWindowAneal_v1 import Ui_AblaufWindowAneal
from dipl_Phasenablauf.AblaufWindowElong_v1 import Ui_AblaufWindowElong

class Frm_denat(QMainWindow, Ui_AblaufWindowDenat):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Frm_aneal(QMainWindow, Ui_AblaufWindowAneal):
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

        self.btn_Start.clicked.connect(self.denat_Ablauf)

    def denat_Ablauf(self):
        frm_main.hide()
        frm_denat.show()
        time.sleep(10)
        frm_denat.hide()
        frm_aneal.show()
        time.sleep(10)
        frm_aneal.hide()
        frm_elong.show()


app = QApplication()
frm_main = Frm_main()
frm_main.show()
frm_denat = Frm_denat()
frm_aneal = Frm_aneal()
frm_elong = Frm_elong()
app.exec()
