from PySide6.QtWidgets import QMainWindow

from dipl_Kontrolle.KontrollWindow_v1 import Ui_Kontrolle
from dipl_Kontrolle.ErgebnisWindow_v1 import Ui_Ergebnis

class Frm_kont(QMainWindow, Ui_Kontrolle):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        self.p5 = 0
        self.p6 = 0
        self.p7 = 0
        self.p8 = 0

class Frm_ergeb(QMainWindow, Ui_Ergebnis):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)