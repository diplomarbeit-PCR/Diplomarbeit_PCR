from PySide6.QtWidgets import QMainWindow

from dipl_Phasenablauf.AblaufWindowDenat_v1 import Ui_AblaufWindowDenat
from dipl_Phasenablauf.AblaufWindowAneal_v1 import Ui_AblaufWindowAneal
from dipl_Phasenablauf.AblaufWindowSens_v1 import Ui_AblaufWindowSens
from dipl_Phasenablauf.AblaufWindowASens_v1 import Ui_AblaufWindowASens
from dipl_Phasenablauf.AblaufWindowElong_v1 import Ui_AblaufWindowElong

class Frm_denat(QMainWindow, Ui_AblaufWindowDenat):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

        # Anzeige der LCD-Anzeige als Uhrenformat definieren
        self.Timer_zaehler.display("00:00:00")

    # sorgt für updaten des Durchlaufzählers
    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

    temp_denat = 0

class Frm_aneal(QMainWindow, Ui_AblaufWindowAneal):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

        # Anzeige der LCD-Anzeige als Uhrenformat definieren
        self.Timer_zaehler.display("00:00:00")

    # sorgt für updaten des Durchlaufzählers
    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)
        
    temp_aneal = 0

class Frm_sens(QMainWindow, Ui_AblaufWindowSens):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

        # Anzeige der LCD-Anzeige als Uhrenformat definieren
        self.Timer_zaehler.display("00:00:00")

    # sorgt für updaten des Durchlaufzählers
    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

class Frm_asens(QMainWindow, Ui_AblaufWindowASens):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

        # Anzeige der LCD-Anzeige als Uhrenformat definieren
        self.Timer_zaehler.display("00:00:00")

    # sorgt für updaten des Durchlaufzählers
    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

class Frm_elong(QMainWindow, Ui_AblaufWindowElong):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

        # Anzeige der LCD-Anzeige als Uhrenformat definieren
        self.Timer_zaehler.display("00:00:00")

    # sorgt für updaten des Durchlaufzählers
    def update_DL_zaehler(self, value):
        self.DL_zaehler.display(value)

    temp_elong = 0