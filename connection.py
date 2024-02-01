from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget, QVBoxLayout, QWidget
import pymysql

from dipl_Kontrolle.ErgebnisWindow_v1 import Ui_Ergebnis

class MainWindow(QMainWindow, Ui_Ergebnis):
    def __init__(self):
        super().__init__()

        temp_denat = 95
        temp_aneal = 60
        temp_elong = 70
        value_denat = 10
        value_aneal = 30
        value_elong = 20

        DL_counter = 10
        value_light = 24.90

        # Verbindung zur Datenbank herstellen
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Rock4C+',
            database='eduPCR'
        )

        # Tabellenwidget für PhasenWerte erstellen
        self.tbl_phasen = QTableWidget()
        self.tbl_phasen.setColumnCount(5)  # Fünf Spalten
        self.tbl_phasen.setHorizontalHeaderLabels(["Kategorien", "Denaturierung", "Annealing", "Elongation", "Einheit"])

        # Tabellenwidget für Messwerte erstellen
        self.tbl_messwerte = QTableWidget()
        self.tbl_messwerte.setColumnCount(2)  # Zwei Spalten
        self.tbl_messwerte.setHorizontalHeaderLabels(["Kategorien", "Anzahl"])

        # Ein zentrales Widget für die Hauptanzeige erstellen
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.tbl_phasen)
        layout.addWidget(self.tbl_messwerte)

        # MainWindow mit dem zentralen Widget einrichten
        self.setCentralWidget(central_widget)

        try:
            with connection.cursor() as cursor:
                # Tabelle 'PhasenWerte' erstellen, falls nicht vorhanden
                create_table_phasen = """
                CREATE TABLE IF NOT EXISTS PhasenWerte (
                    Kategorien VARCHAR(50),
                    Denaturierung DECIMAL(5,2),
                    Annealing DECIMAL(5,2),
                    Elongation DECIMAL(5,2),
                    Einheit VARCHAR(50)
                )
                """
                cursor.execute(create_table_phasen)
                print("Tabelle 'PhasenWerte' erstellt")

                # Tabelle 'Messwerte' erstellen, falls nicht vorhanden
                create_table_messwert = """
                CREATE TABLE IF NOT EXISTS Messwerte (
                    Kategorien VARCHAR(50),
                    Anzahl DECIMAL(5,2)
                )
                """
                cursor.execute(create_table_messwert)
                print("Tabelle 'Messwerte' erstellt")

                # INSERT INTO-Anweisung für PhasenWerte
                insert_phasen = """
                INSERT INTO PhasenWerte (Kategorien, Denaturierung, Annealing, Elongation, Einheit)
                VALUES 
                ("Temperatur", %s, %s, %s, "°C"),
                ("Dauer", %s, %s, %s, "sek")
                """
                cursor.execute(insert_phasen, (temp_denat, temp_aneal, temp_elong, value_denat, value_aneal, value_elong))

                # INSERT INTO-Anweisung für Messwerte
                insert_messwerte = """
                INSERT INTO Messwerte (Kategorien, Anzahl)
                VALUES 
                ("Durchläufe", %s),
                ("Lichtstärke in Lumen", %s )
                """
                cursor.execute(insert_messwerte, (DL_counter, value_light))

                # Daten aus Tabelle 'PhasenWerte' abrufen
                cursor.execute("SELECT * FROM PhasenWerte")
                result_phasen = cursor.fetchall()

                # Daten aus Tabelle 'Messwerte' abrufen
                cursor.execute("SELECT * FROM Messwerte")
                result_messwerte = cursor.fetchall()

                # Ergebnisse in tbl_phasen einfügen
                self.tbl_phasen.insertRow(result_phasen)

                # Ergebnisse in tbl_messwerte einfügen
                self.tbl_messwerte.insertRow(result_messwerte)

        except pymysql.MySQLError as e:
            print("MySQL-Fehler: {}".format(str(e)))

        finally:
            # Verbindung schließen
            connection.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
