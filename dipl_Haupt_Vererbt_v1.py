from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget
from PySide6.QtCore import QTimer
import pymysql
# Auf die unterschiedlichen WIndows zugreifen (QT Deklaration, die in Py umgewandelt wurden)
from dipl_Einfuehrung.einfuehrung_v4 import Ui_StartWindow
from dipl_Einfuehrung.Voraussetzungen_Vererbt_v1 import Frm_voraus
from dipl_Einfuehrung.zeitDefinition_Vererbt_v1 import Frm_zeitDef
from dipl_Einfuehrung.WarteWindow_Vererbt_v1 import Frm_WarteWindow
from dipl_Phasenablauf.Phasenablauf_Vererbt_v1 import Frm_denat, Frm_aneal, Frm_sens, Frm_asens, Frm_elong
from dipl_Kontrolle.KontrollErgebnis_Vererbt_v1 import Frm_kont, Frm_ergeb

class Frm_main(QMainWindow, Ui_StartWindow):

    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

        self.timer_seconds = 0
        self.timer = QTimer()
        # mit einem Intervall von 
        self.timer.setInterval(1000)
        
        # Verbindung zur Datenbank herstellen
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Rock4C+',
            database='eduPCR'
        )

        self.cursor_mess1 = self.connection.cursor()
        self.cursor_mess2 = self.connection.cursor()
        self.cursor_phasen = self.connection.cursor()
        self.cursor_dl = self.connection.cursor()

        self.DL_zaehler_value = 0
        self.DL_counter = 0

        self.frm_voraus = Frm_voraus()
        self.frm_zeitDef = Frm_zeitDef()
        self.frm_ww = Frm_WarteWindow()
        self.frm_denat = Frm_denat()
        self.frm_aneal = Frm_aneal()
        self.frm_sens = Frm_sens()
        self.frm_asens = Frm_asens()
        self.frm_elong = Frm_elong()
        self.frm_kont = Frm_kont()
        self.frm_ergeb = Frm_ergeb()

        
        self.frm_denat.temp_denat = 94
        self.frm_aneal.temp_aneal = 65
        self.frm_elong.temp_elong = 67
        self.frm_kont.p1 = 40.1
        self.frm_kont.p2 = 17.39
        self.frm_kont.p3 = 40.1
        self.frm_kont.p4 = 17.39
        self.frm_kont.p5 = 40.1
        self.frm_kont.p6 = 17.39
        self.frm_kont.p7 = 40.1
        self.frm_kont.p8 = 17.39
         
        # Verbindung des Start-Knopfes mit der Methode erlaubteDauer 
        self.btn_Start.clicked.connect(self.erlaubteDauer)

        # Verbindung des Weiter-Knopfes mit der Methode phasen_Ablauf
        self.frm_zeitDef.btn_Weiter.clicked.connect(self.WarteStart)

        # Verbindung des Fortfuehren-Knopfes mit der Methode weiter
        self.frm_kont.btn_Fortfuehren.clicked.connect(self.weiter)
        # Verbindung des Beenden-Knopfes mit der Methode esc
        self.frm_kont.btn_Beenden.clicked.connect(self.ergebnis)
        # Verbindung des Beenden-Knopfes mit der Methode esc
        self.frm_ergeb.btn_Ende.clicked.connect(self.esc)

        self.phasen_running = True  # Flag für den Zustand von phasen_Ablauf

        self.seconds = 0
        self.timer.timeout.connect(self.run_phasen_Ablauf)  # Verbinde den Timer mit der Methode
        
        self.phaseCount = 0
        
        
    def erlaubteDauer(self):
        self.frm_voraus.showFullScreen()
        self.hide()
        
        QTimer.singleShot(10000, self.frm_zeitDef.showFullScreen)
        QTimer.singleShot(10000, self.frm_voraus.hide)

    def WarteStart(self):
        self.frm_ww.showFullScreen()
        self.frm_zeitDef.hide()

        QTimer.singleShot(10000, self.phasen_Ablauf)

    def WarteKont(self):
        self.frm_ww.showFullScreen()

        QTimer.singleShot(10000, self.frm_kont.showFullScreen)
        QTimer.singleShot(10000, self.frm_ww.hide)

    def phasen_Ablauf(self):
        self.frm_ww.hide()
        self.timer.start()

        # Verbindung des Kontroll-Knopfes mit der Methode kontroll_Erklaerung 
        self.frm_denat.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_aneal.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_sens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_asens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_elong.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        
        if self.phasen_running == False:
            self.timer.stop()
            self.WarteKont()
        
        else:
            self.run_phasen_Ablauf()
            
            self.phaseCount = 0
            
            self.DL_counter += 1 
            
            self.DL_zaehler_value += 1  
            self.frm_denat.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_aneal.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_sens.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_asens.update_DL_zaehler(self.DL_zaehler_value)
            self.frm_elong.update_DL_zaehler(self.DL_zaehler_value)
    
    def run_phasen_Ablauf(self):
        self.timer.start(1000)  # Timer feuert alle 1000 Millisekunden (1 Sekunde)
        self.seconds += 1
        self.phaseCount += 1
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        seconds = self.seconds % 60

        # Count Up Timer - Zeit zählt nach oben
        self.frm_denat.Timer_zaehler.display(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        self.frm_aneal.Timer_zaehler.display(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        self.frm_sens.Timer_zaehler.display(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        self.frm_asens.Timer_zaehler.display(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        self.frm_elong.Timer_zaehler.display(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        
        # Funktion - nimmt drei Parameter entgegen: phase, start und end
        # überprüft, dass self.phaseCount zwischen start und end (einschließlich start und ausschließlich end) liegt
        # liegt dazwischen: Methode show() auf dem phase-Objekt wird aufgerufen
        # liegt nicht dazwischen: Methode hide() wird aufgerufen
        # start und end mit check_and_show definiert
        # phase-Pbjekt erkennt anhand check_and_show was ausgefürht werden muss
        def check_and_show(phase, start, end):
            if start < self.phaseCount <= end:
                phase.showFullScreen()
            else:
                phase.hide()

        # sagt welches Window, BeginnWert von Anziege, EndWert von Anzeige
        check_and_show(self.frm_denat, 0, self.frm_zeitDef.value_denat)
        check_and_show(self.frm_aneal, self.frm_zeitDef.value_denat, self.frm_zeitDef.value_aneal)
        check_and_show(self.frm_sens, self.frm_zeitDef.value_aneal, self.frm_zeitDef.value_sens)
        check_and_show(self.frm_asens, self.frm_zeitDef.value_sens, self.frm_zeitDef.value_asens)
        check_and_show(self.frm_elong, self.frm_zeitDef.value_asens, self.frm_zeitDef.value_elong)
            
        # alle 10 Durchläufe soll automatisch das Kontrollfenster geöffnet werden
        # beginnt von vorne zu zählen, wenn manuell der Kontrollknopf betätigt wird
        if self.DL_counter == 10:
            self.phasen_running = False
            self.DL_counter = 0

        # ist phaseCount größer als value_elong, soll die phasen_Ablauf Methode wiederholt werden  
        if self.phaseCount > (self.frm_zeitDef.value_elong):
            self.phaseCount = 0
            self.phasen_Ablauf()

    def kontroll_Erklaerung(self):
        self.phasen_running = False  # Stoppe phasen_Ablauf
        self.DL_counter = 0

    def weiter(self):
        # phasen_Ablauf soll wiederholt werden
        self.phasen_running = True   # Starte phasen_Ablauf
        self.phasen_Ablauf()
        self.frm_kont.hide()

    def ergebnis(self):
        self.frm_ergeb.tbl_phasen.setColumnCount(4)  # Fünf Spalten
        self.frm_ergeb.tbl_phasen.setHorizontalHeaderLabels(["Kategorien", "Denaturierung", "Annealing", "Elongation"])
        self.frm_ergeb.tbl_mess1.setColumnCount(2)  # Zwei Spalten
        self.frm_ergeb.tbl_mess1.setHorizontalHeaderLabels(["Probe", "Lichtstärke in Lumen"])
        self.frm_ergeb.tbl_mess2.setColumnCount(2)  # Zwei Spalten
        self.frm_ergeb.tbl_mess2.setHorizontalHeaderLabels(["Probe", "Lichtstärke in Lumen"])
        self.frm_ergeb.tbl_dl.setColumnCount(2)  # Zwei Spalten
        self.frm_ergeb.tbl_dl.setHorizontalHeaderLabels(["Kategorie", "Anzahl"])

        print("temp_d", self.frm_denat.temp_denat)
        print("temp_a", self.frm_aneal.temp_aneal)
        print("temp_e", self.frm_elong.temp_elong)
        print("dauer_d", self.frm_zeitDef.value_denat)
        print("dauer_a", self.frm_zeitDef.value_aneal_gesamt)
        print("dauer_e", self.frm_zeitDef.value_elong_gesamt)
        print("dl", self.DL_zaehler_value)


        try:
            # Tabelle 'PhasenWerte' erstellen, falls nicht vorhanden
            create_table_phasen = """
            CREATE TABLE IF NOT EXISTS PhasenWerte (
                Kategorien VARCHAR(50),
                Denaturierung DECIMAL(5,2),
                Annealing DECIMAL(5,2),
                Elongation DECIMAL(5,2)
            )
            """
            self.cursor_phasen.execute(create_table_phasen)
            print("Tabelle 'PhasenWerte' erstellt")

            # Tabelle 'Messwerte' erstellen, falls nicht vorhanden
            create_table_messwert1 = """
            CREATE TABLE IF NOT EXISTS Messwerte1 (
                Probe VARCHAR(5),
                Lichtstärke in Lumen DECIMAL(5,2)
            )
            """
            self.cursor_mess1.execute(create_table_messwert1)
            print("Tabelle 'Messwerte1' erstellt")

            # Tabelle 'Messwerte' erstellen, falls nicht vorhanden
            create_table_messwert2 = """
            CREATE TABLE IF NOT EXISTS Messwerte2 (
                Probe VARCHAR(5),
                Lichtstärke in Lumen DECIMAL(5,2)
            )
            """
            self.cursor_mess2.execute(create_table_messwert2)
            print("Tabelle 'Messwerte2' erstellt")

            # Tabelle 'Durchläufe' erstellen, falls nicht vorhanden
            create_table_dl = """
            CREATE TABLE IF NOT EXISTS Durchlauf (
                Kategorie VARCHAR(50),
                Anzahl DECIMAL(5,2)
            )
            """
            self.cursor_dl.execute(create_table_dl)
            print("Tabelle 'Durchlauf' erstellt")

            # INSERT INTO-Anweisung für PhasenWerte
            insert_phasen = """
            INSERT INTO PhasenWerte (Kategorien, Denaturierung, Annealing, Elongation)
            VALUES 
            ("Temperatur in °C", %s, %s, %s),
            ("Dauer in sek", %s, %s, %s)
            """
            self.cursor_phasen.execute(insert_phasen, (self.frm_denat.temp_denat, self.frm_aneal.temp_aneal, self.frm_elong.temp_elong, self.frm_zeitDef.value_denat, self.frm_zeitDef.value_aneal_gesamt, self.frm_zeitDef.value_elong_gesamt))

            # INSERT INTO-Anweisung für Messwerte
            insert_messwerte = """
            INSERT INTO Messwerte1 (Probe, Lichtstärke in Lumen)
            VALUES 
            ("P1", %s),
            ("P2", %s),
            ("P3", %s),
            ("P4", %s)
            """
            self.cursor_mess1.execute(insert_messwerte, (self.frm_kont.p1, self.frm_kont.p2, self.frm_kont.p3, self.frm_kont.p4))

            # INSERT INTO-Anweisung für Messwerte
            insert_messwerte = """
            INSERT INTO Messwerte2 (Probe, Lichtstärke in Lumen)
            VALUES 
            ("P5", %s),
            ("P6", %s),
            ("P7", %s),
            ("P8", %s)
            """
            self.cursor_mess2.execute(insert_messwerte, (self.frm_kont.p5, self.frm_kont.p6, self.frm_kont.p7, self.frm_kont.p8))


            # INSERT INTO-Anweisung für Messwerte
            insert_dl = """
            INSERT INTO Durchlauf (Kategorie, Anzahl)
            VALUES 
            ("Durchlauf", %s)
            """
            self.cursor_dl.execute(insert_dl, (self.DL_zaehler_value))

            # Daten aus Tabelle 'PhasenWerte' abrufen
            self.cursor_phasen.execute("SELECT * FROM PhasenWerte")
            result_phasen = self.cursor_phasen.fetchall()

            # Daten aus Tabelle 'Messwerte' abrufen
            self.cursor_mess1.execute("SELECT * FROM Messwert1")
            result_messwerte1 = self.cursor_mess1.fetchall()

            
            # Daten aus Tabelle 'Messwerte' abrufen
            self.cursor_mess2.execute("SELECT * FROM Messwerte2")
            result_messwerte2 = self.cursor_mess2.fetchall()

            # Daten aus Tabelle 'Messwerte' abrufen
            self.cursor_dl.execute("SELECT * FROM Durchlauf")
            result_dl = self.cursor_dl.fetchall()

            # Ergebnisse in tbl_phasen einfügen
            for row_num, row_data in enumerate(result_phasen):
                self.frm_ergeb.tbl_phasen.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                    self.frm_ergeb.tbl_phasen.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

            # Ergebnisse in tbl_messwerte einfügen
            for row_num, row_data in enumerate(result_messwerte1):
                self.frm_ergeb.tbl_mess1.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                    self.frm_ergeb.tbl_mess1.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

                    
            # Ergebnisse in tbl_messwerte einfügen
            for row_num, row_data in enumerate(result_messwerte2):
                self.frm_ergeb.tbl_mess2.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                    self.frm_ergeb.tbl_mess2.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

            # Ergebnisse in tbl_messwerte einfügen
            for row_num, row_data in enumerate(result_dl):
                self.frm_ergeb.tbl_dl.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                    self.frm_ergeb.tbl_dl.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

        except pymysql.MySQLError as e:
            print("MySQL-Fehler: {}".format(str(e)))

        except OSError as o:
            print("Fehler: {}".format(str(o)))

        finally:
            # Verbindung schließen
            self.connection.close()

        # phasen_Ablauf soll wiederholt werden
        self.frm_ergeb.showFullScreen()
        self.frm_kont.hide()

    def esc(self):
        # alles auf Start Einstellungen zurücksetzen
        frm_main.showFullScreen()
        self.frm_ergeb.hide()
        self.phasen_running = True
        self.timer.stop()
        self.seconds = 0
        self.DL_zaehler_value = 0
        self.frm_zeitDef.wasserDauer_denat.setValue(35)
        self.frm_zeitDef.wasserDauer_aneal.setValue(45)
        self.frm_zeitDef.wasserDauer_elong.setValue(40)

app = QApplication()
frm_main = Frm_main()
frm_main.showFullScreen()
app.exec()
