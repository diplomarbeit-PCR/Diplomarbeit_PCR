from PySide6.QtWidgets import QMainWindow

from dipl_Kontrolle.KontrollWindow_v1 import Ui_Kontrolle
from dipl_Kontrolle.ErgebnisWindow_v1 import Ui_Ergebnis

class Frm_kont(QMainWindow, Ui_Kontrolle):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

    
        self.p1 = 41
        self.p2 = 44
        self.p3 = 48
        self.p4 = 39
        self.p5 = 50
        self.p6 = 42
        self.p7 = 43
        self.p8 = 47

class Frm_ergeb(QMainWindow, Ui_Ergebnis):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)