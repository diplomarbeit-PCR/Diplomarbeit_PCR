import pymysql
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QWidget)

centralwidget = QWidget()
centralwidget.setObjectName(u"centralwidget")
tbl_phasen = QTableView(centralwidget)
tbl_phasen.setObjectName(u"tbl_phasen")
tbl_phasen.setGeometry(QRect(0, 120, 491, 261))
tbl_m = QTableView(centralwidget)
tbl_m.setObjectName(u"tbl_m")
tbl_m.setGeometry(QRect(0, 390, 491, 211))

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
    host='localhost',     # Hostname oder IP-Adresse deiner MariaDB-Instanz
    user='root',     # Benutzername für den Zugriff auf die Datenbank
    password='Rock4C+',    # Passwort für den Benutzer
    database='eduPCR'    # Name der Datenbank, zu der du dich verbinden möchtest
)

try:
    # Cursor-Objekt erstellen
    with connection.cursor() as cursor:

        # Tabelle 'PhasenWerte' erstellen
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

        # Tabelle 'Messwerte' erstellen
        create_table_messwert = """
        CREATE TABLE IF NOT EXISTS Messwerte (
            Kategorien VARCHAR(50),
            Werte DECIMAL(5,2),
            Einheit VARCHAR(50)
        )
        """
        cursor.execute(create_table_messwert)
        print("Tabelle 'Messwerte' erstellt")

        # Daten in Tabelle 'PhasenWerte' einfügen
        insert_table_phasen = """
        INSERT INTO PhasenWerte
        VALUES
        ("Temperatur", %s, %s, %s, "°C"),
        ("Dauer", %s, %s, %s, "sek")
        """
        cursor.execute(insert_table_phasen, (temp_denat, temp_aneal, temp_elong, value_denat, value_aneal, value_elong))
        print("In Tabelle 'PhasenWerte' eingefügt")

        # Daten aus Tabelle 'PhasenWerte' abrufen
        dae = "SELECT * FROM PhasenWerte"
        cursor.execute(dae)
        result_phasen = cursor.fetchall()

        # Daten aus Tabelle 'Messwerte' abrufen
        mw = "SELECT * FROM Messwerte"
        cursor.execute(mw)
        result_messwerte = cursor.fetchall()

        # Ergebnisse in tbl_phasen einfügen
        for row in result_phasen:
            tbl_phasen.insertRow(tbl_phasen.rowCount())
            for i, item in enumerate(row):
                tbl_phasen.setItem(tbl_phasen.rowCount() - 1, i, QTableWidgetItem(str(item)))

        # Ergebnisse in tbl_m einfügen
        for row in result_messwerte:
            tbl_m.insertRow(tbl_m.rowCount())
            for i, item in enumerate(row):
                tbl_m.setItem(tbl_m.rowCount() - 1, i, QTableWidgetItem(str(item)))

except pymysql.MySQLError as e:
    print("MySQL-Fehler: {}".format(str(e)))

finally:
    # Verbindung schließen
    connection.close()