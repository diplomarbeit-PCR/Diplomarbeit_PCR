from PySide6.QtWidgets import QMainWindow
from dipl_Kontrolle.ErgebnisWindow_v1 import Ui_Ergebnis
import pymysql

class Frm_ergeb(QMainWindow, Ui_Ergebnis):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

        # Daten aus der Datenbank abrufen und in Labels anzeigen
        self.get_and_display_data()

    def get_and_display_data(self):
        # Verbindung zur Datenbank herstellen
        connection = pymysql.connect(
            host='localhost',     # Hostname oder IP-Adresse deiner MariaDB-Instanz
            user='root',     # Benutzername für den Zugriff auf die Datenbank
            password='Rock4C+',    # Passwort für den Benutzer
            database='eduPCR'    # Name der Datenbank, zu der du dich verbinden möchtest
        )

        try:
            with connection.cursor() as cursor:
                # Daten aus Tabelle 'PhasenWerte' abrufen
                cursor.execute("SELECT * FROM PhasenWerte")
                phasen_data = cursor.fetchall()

                # Daten aus Tabelle 'Messwerte' abrufen
                cursor.execute("SELECT * FROM Messwerte")
                messwerte_data = cursor.fetchall()

        except pymysql.MySQLError as e:
            print("MySQL-Fehler: {}".format(str(e)))

        finally:
            # Verbindung schließen
            connection.close()

        # Daten in Labels anzeigen
        phasen_text = ""
        for row in phasen_data:
            phasen_text += f"{row['Kategorien']}: {row['Denaturierung']} {row['Annealing']} {row['Elongation']} {row['Einheit']}\n"
        self.tbl_phasen.setText(phasen_text)

        messwerte_text = ""
        for row in messwerte_data:
            messwerte_text += f"{row['Kategorien']}: {row['Werte']} {row['Einheit']}\n"
        self.tbl_m.setText(messwerte_text)
