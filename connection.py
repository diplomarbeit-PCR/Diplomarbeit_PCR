from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget, QVBoxLayout, QWidget
import pymysql

from dipl_Kontrolle.ErgebnisWindow_v1 import Ui_Ergebnis
from dipl_Kontrolle.KontrollErgebnis_Vererbt_v1 import Frm_ergeb

class Frm_connect(QMainWindow, Ui_Ergebnis):
    def __init__(self):
        super().__init__()

        self.frm_ergeb = Frm_ergeb()

        self.temp_denat = 95
        self.temp_aneal = 60
        self.temp_elong = 70
        self.value_denat = 10
        self.value_aneal = 30
        self.value_elong = 20

        self.DL_counter = 10
        self.value_light = 24.90

        # Verbindung zur Datenbank herstellen
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Rock4C+',
            database='eduPCR'
        )

        self.cursor_mess = self.connection.cursor()
        self.cursor_phasen = self.connection.cursor()

        