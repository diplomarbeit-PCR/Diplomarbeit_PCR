from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget
import pymysql



class MainWindow(QMainWindow):
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
        self.setCentralWidget(self.tbl_phasen)

        # Tabellenwidget für Messwerte erstellen
        self.tbl_messwerte = QTableWidget()
        self.tbl_messwerte.setColumnCount(3)  # Drei Spalten
        self.tbl_messwerte.setHorizontalHeaderLabels(["Kategorien", "Werte", "Einheit"])
        self.setCentralWidget(self.tbl_messwerte)

        try:
            with connection.cursor() as cursor:
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
                INSERT INTO Messwerte (Kategorien, Werte, Einheit)
                VALUES 
                ("Durchläufe", %s, ""),
                ("Lichtstärke", %s, "lum")
                """
                cursor.execute(insert_messwerte, (DL_counter, value_light))

                # Daten aus Tabelle 'PhasenWerte' abrufen
                cursor.execute("SELECT * FROM PhasenWerte")
                result_phasen = cursor.fetchall()

                # Daten aus Tabelle 'Messwerte' abrufen
                cursor.execute("SELECT * FROM Messwerte")
                result_messwerte = cursor.fetchall()

                # Ergebnisse in tbl_phasen einfügen
                for row_num, row_data in enumerate(result_phasen):
                    self.tbl_phasen.insertRow(row_num)
                    for col_num, col_data in enumerate(row_data):
                        self.tbl_phasen.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

                # Ergebnisse in tbl_messwerte einfügen
                for row_num, row_data in enumerate(result_messwerte):
                    self.tbl_messwerte.insertRow(row_num)
                    for col_num, col_data in enumerate(row_data):
                        self.tbl_messwerte.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

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
    sys.exit(app.exec_())
