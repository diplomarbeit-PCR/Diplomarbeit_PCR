from PySide6.QtWidgets import QMainWindow

from dipl_Kontrolle.KontrollWindow_v1 import Ui_Kontrolle
from dipl_Kontrolle.ErgebnisWindow_v1 import Ui_Ergebnis

class Frm_kont(QMainWindow, Ui_Kontrolle):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

    value_light = 0
    value_spg = 0

class Frm_ergeb(QMainWindow, Ui_Ergebnis):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)