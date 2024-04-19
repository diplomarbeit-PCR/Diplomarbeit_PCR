from PySide6.QtWidgets import QMainWindow, QApplication

from dipl_Kontrolle.KontrollAnspruchWindow_v1 import Ui_KontrollAnspruch
from dipl_Kontrolle.KontrollWindow_v1 import Ui_Kontrolle
from dipl_Kontrolle.ErgebnisWindow_v1 import Ui_Ergebnis

class Frm_kontanspruch(QMainWindow, Ui_KontrollAnspruch):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

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

        self.tbl_mess1.setColumnCount(2)  # Zwei Spalten
        self.tbl_mess1.setHorizontalHeaderLabels(["Proben", "Lichtintensität"])
        self.tbl_mess2.setColumnCount(2)  # Zwei Spalten
        self.tbl_mess2.setHorizontalHeaderLabels(["Proben", "Lichtintensität"])

class Frm_ergeb(QMainWindow, Ui_Ergebnis):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

        self.tbl_phasen.setColumnCount(4)  # Fünf Spalten
        self.tbl_phasen.setHorizontalHeaderLabels(["Kategorien", "Denaturierung", "Annealing", "Elongation"])
        self.tbl_mess1.setColumnCount(2)  # Zwei Spalten
        self.tbl_mess1.setHorizontalHeaderLabels(["Probe", "Lichtstärke"])
        self.tbl_mess2.setColumnCount(2)  # Zwei Spalten
        self.tbl_mess2.setHorizontalHeaderLabels(["Probe", "Lichtstärke"])
        self.tbl_dl.setColumnCount(2)  # Zwei Spalten
        self.tbl_dl.setHorizontalHeaderLabels(["Kategorie", "Anzahl"])
