from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget
from PySide6.QtCore import QTimer, Signal
from PySide6.QtGui import QFont
import pymysql
import smbus
import time
import subprocess
# Auf die unterschiedlichen Windows zugreifen (QT Deklaration, die in Py umgewandelt wurden)
from dipl_Einfuehrung.einfuehrung_v4 import Ui_StartWindow
from dipl_Einfuehrung.Voraussetzungen_Vererbt_v1 import Frm_voraus
from dipl_Einfuehrung.zeitDefinition_Vererbt_v1 import Frm_zeitDef
from dipl_Einfuehrung.tempDefinition_Vererbt_v1 import Frm_tempDef
from dipl_Einfuehrung.TempAnspruch_Vererbt_v1 import Frm_tempanspruch
from dipl_Einfuehrung.WarteWindow_Vererbt_v1 import Frm_WarteWindow
from dipl_Phasenablauf.Phasenablauf_Vererbt_v1 import Frm_denat, Frm_aneal, Frm_sens, Frm_asens, Frm_elong
from dipl_Kontrolle.KontrollErgebnis_Vererbt_v1 import Frm_kont, Frm_ergeb, Frm_kontanspruch


class Frm_main(QMainWindow, Ui_StartWindow):

    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

        # Öffne den I2C-Bus 7
        self.bus = smbus.SMBus(7)
        # Adresse des Arduino-Slave
        self.beweg_address = 0x04
        # Adresse des Arduino-Slave
        self.temp_address = 0x05
        # Adresse des Arduino-Slave
        self.detect_address = 0x06

        self.timer_seconds = 0
        self.timer = QTimer()
        self.go_Beweg = False
        # mit einem Intervall von 
        self.timer.setInterval(1000)
        
        self.temp_timer = QTimer()
        self.temp_timer.timeout.connect(self.temp_Kontrolle)

        self.beweg_timer = QTimer()
        self.beweg_timer.timeout.connect(self.i2c_pruef)
        
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
        self.frm_tempDef = Frm_tempDef()
        self.frm_tempanspruch = Frm_tempanspruch()
        self.frm_ww = Frm_WarteWindow()
        self.frm_denat = Frm_denat()
        self.frm_aneal = Frm_aneal()
        self.frm_sens = Frm_sens()
        self.frm_asens = Frm_asens()
        self.frm_elong = Frm_elong()
        self.frm_kontanspruch = Frm_kontanspruch()
        self.frm_kont = Frm_kont()
        self.frm_ergeb = Frm_ergeb()

        # Verbinde von Menüpunkt ShutDown
        self.menuShutDown.triggered.connect(self.shutDown) 
         
        # Verbindung des Start-Knopfes mit der Methode erlaubteDauer 
        self.btn_Start.clicked.connect(self.erlaubteTemp)

        # Verbinde von Menüpunkt Weiter
        self.frm_tempanspruch.btn_Weiter.clicked.connect(self.phasen_Ablauf)

        # Verbinde von Menüpunkt Weiter
        self.frm_kontanspruch.btn_Weiter.clicked.connect(self.kontanspruch)

        # Verbindung des Weiter-Knopfes mit der Methode phasen_Ablauf
        self.frm_tempDef.btn_Weiter.clicked.connect(self.erlaubteDauer)

        # Verbindung des Weiter-Knopfes mit der Methode phasen_Ablauf
        self.frm_zeitDef.btn_Weiter.clicked.connect(self.i2c_pruef)

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
        self.stopped_reading = True

        self.frm_kont.tbl_mess1.setColumnCount(2)  # Zwei Spalten
        self.frm_kont.tbl_mess1.setHorizontalHeaderLabels(["Proben", "Lichtintensität"])
        self.frm_kont.tbl_mess2.setColumnCount(2)  # Zwei Spalten
        self.frm_kont.tbl_mess2.setHorizontalHeaderLabels(["Proben", "Lichtintensität"])

        
        self.frm_ergeb.tbl_phasen.setColumnCount(4)  # Fünf Spalten
        self.frm_ergeb.tbl_phasen.setHorizontalHeaderLabels(["Kategorien", "Denaturierung", "Annealing", "Elongation"])
        self.frm_ergeb.tbl_mess1.setColumnCount(2)  # Zwei Spalten
        self.frm_ergeb.tbl_mess1.setHorizontalHeaderLabels(["Probe", "Lichtstärke"])
        self.frm_ergeb.tbl_mess2.setColumnCount(2)  # Zwei Spalten
        self.frm_ergeb.tbl_mess2.setHorizontalHeaderLabels(["Probe", "Lichtstärke"])
        self.frm_ergeb.tbl_dl.setColumnCount(2)  # Zwei Spalten
        self.frm_ergeb.tbl_dl.setHorizontalHeaderLabels(["Kategorie", "Anzahl"])
        
    def erlaubteTemp(self):
        self.frm_voraus.showFullScreen()
        self.hide()
        
        QTimer.singleShot(10000, self.frm_tempDef.showFullScreen)
        QTimer.singleShot(10000, self.frm_voraus.hide)

    def erlaubteDauer(self):
        self.frm_zeitDef.showFullScreen()
        self.frm_tempDef.hide()

    def i2c_pruef(self):
        self.frm_zeitDef.hide()

        # Starte den Timer mit einer Startverzögerung von 0 Millisekunden und einem Intervall von 2000 Millisekunden (2 Sekunden)
        self.beweg_timer.start(0)
        self.beweg_timer.setInterval(1000)
        self.WarteStart()

    def WarteStart(self):
        self.i2c_operation_requested = Signal(int)
        
        self.data_sent = False  # Hält den Zustand, ob die Daten gesendet wurden
        self.stopped_reading_beweg = False  # Hält den Zustand, ob der Leseprozess gestoppt wurde

        print("Senden der Daten ... ")
        print(self.read_data_from_beweg())
        self.read_data_from_beweg()

        if self.stopped_reading_beweg:
            self.timer.stop()  # Stoppen Sie den Timer, da der Leseprozess gestoppt wurde
            self.temp_Kontrolle()

    def read_data_from_beweg(self):
    # Nur Daten vom Slave lesen, wenn der Leseprozess nicht gestoppt wurde
        if not self.stopped_reading_beweg:
            try:
                if self.i == 0:
                    data = self.read_from_beweg()
                    if data is None:             
                        data = self.read_from_beweg()

                    if data == 7:
                        data = self.read_from_beweg()
                        
                    if data == 0:
                        data = self.read_from_beweg()

                    if data == 5 and not self.data_sent:
                        self.data_sent = True
                        print("5 erhalten")
                        self.i += 1
                        print(self.i)
                        # Hier könnten Sie die gewünschten Daten an den Slave senden
                        self.write_to_beweg(1)  # Beispielwert 10 für Daten, die an den Slave gesendet werden sollen
                        self.write_to_beweg(self.frm_zeitDef.value_denat_gesamt)  # Beispielwert 10 für Daten, die an den Slave gesendet werden sollen
                        self.write_to_beweg(2)  # Beispielwert 10 für Daten, die an den Slave gesendet werden sollen
                        self.write_to_beweg(self.frm_zeitDef.value_aneal_gesamt)  # Beispielwert 10 für Daten, die an den Slave gesendet werden sollen
                        self.write_to_beweg(3)  # Beispielwert 10 für Daten, die an den Slave gesendet werden sollen
                        self.write_to_beweg(self.frm_zeitDef.value_elong_gesamt)  # Beispielwert 10 für Daten, die an den Slave gesendet werden sollen

                        self.bus.write_byte(self.temp_address, 1)
                        self.bus.write_byte(self.temp_address, self.frm_tempDef.value_denat)
                        self.bus.write_byte(self.temp_address, 2)
                        self.bus.write_byte(self.temp_address, self.frm_tempDef.value_aneal)
                        self.bus.write_byte(self.temp_address, 3)
                        self.bus.write_byte(self.temp_address, self.frm_tempDef.value_elong)

                        self.stopped_reading_beweg = True  # Leseprozess stoppen
                    
            except Exception as e:
                print(f"Fehler beim Lesen von Daten vom Slave: {str(e)}")

    def write_to_beweg(self, data):
        try:
            # Schreibe Daten an den Slave
            self.bus.write_byte(self.beweg_address, data)
            print(f"Daten {data} erfolgreich an Slave gesendet.")
        except Exception as e:
            print(f"Fehler beim Senden von Daten an den Slave: {str(e)}")

    def read_from_beweg(self):
        try:
            # Lese Daten vom Slave
            data = self.bus.read_byte(self.beweg_address)
            return data
        except Exception as e:
            print(f"Fehler")

    def read_from_temp(self):
        self.data = []
        for _ in range(3):  # Wir erwarten 3 Datenpunkte (temp_denat, temp_aneal, temp_elong)
            self.data.append(self.bus.read_byte(self.temp_address))
        return self.data
    
    def write_to_temp(self, data):
        try:
            # Schreibe Daten an den Slave
            self.bus.write_byte(self.temp_address, data)
        except Exception as e:
            print(f"Fehler beim Senden von Daten an den Slave: {str(e)}")

    def temp_Kontrolle(self):
        self.frm_zeitDef.hide()
        self.beweg_timer.stop()

        # Starte den Timer mit einer Startverzögerung von 0 Millisekunden und einem Intervall von 2000 Millisekunden (2 Sekunden)
        self.temp_timer.start(0)
        self.temp_timer.setInterval(1000)
        self.temp_Messung_Kontrolle()

    def temp_Messung_Kontrolle(self):
    
        # Daten vom Arduino lesen
        temp_received_kont = self.read_from_temp()
        print("tempmessung1")
        self.frm_tempanspruch.temp_denat_kont = temp_received_kont[0] 
        self.frm_tempanspruch.temp_aneal_kont = temp_received_kont[1] 
        self.frm_tempanspruch.temp_elong_kont = temp_received_kont[2] 

        self.frm_tempanspruch.wasser_denat.display(self.frm_tempanspruch.temp_denat_kont)
        self.frm_tempanspruch.wasser_aneal.display(self.frm_tempanspruch.temp_aneal_kont)
        self.frm_tempanspruch.wasser_elong.display(self.frm_tempanspruch.temp_elong_kont)

        self.temperaturen = self.frm_tempDef.value_denat, self.frm_tempDef.value_aneal, self.frm_tempDef.value_elong

        self.frm_tempanspruch.lbl_tempdef.setText(str(self.temperaturen))
        font = QFont()
        font.setPointSize(16)  # Hier die gewünschte Schriftgröße einstellen
        self.frm_tempanspruch.lbl_tempdef.setFont(font)

        self.frm_tempanspruch.showFullScreen()

    def phasen_Ablauf(self):
        self.frm_tempanspruch.hide()

        self.temp_timer.stop()
        self.timer.start()

        # Verbindung des Kontroll-Knopfes mit der Methode kontroll_Erklaerung 
        self.frm_denat.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_aneal.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_sens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_asens.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        self.frm_elong.btn_Kontrolle.clicked.connect(self.kontroll_Erklaerung)
        
        if self.phasen_running == False:
            self.timer.stop()
            self.frm_kontanspruch.showFullScreen()

        else:
            self.write_to_beweg(4)
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

         # Daten vom Arduino lesen
        temp_received = self.read_from_temp()
        print("Tempmessung")
        self.frm_denat.temp_denat = temp_received[0] 
        self.frm_aneal.temp_aneal = temp_received[1] 
        self.frm_elong.temp_elong = temp_received[2] 
        
        self.frm_denat.temp_sensD.display(self.frm_denat.temp_denat)
        self.frm_aneal.temp_sensA.display(self.frm_aneal.temp_aneal)
        self.frm_sens.temp_sensA.display(self.frm_aneal.temp_aneal)
        self.frm_asens.temp_sensA.display(self.frm_aneal.temp_aneal)
        self.frm_elong.temp_sensE.display(self.frm_elong.temp_elong)
        
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
        self.write_to_beweg(5)
        self.DL_counter = 0

    def weiter(self):
        # phasen_Ablauf soll wiederholt werden
        self.phasen_running = True   # Starte phasen_Ablauf
        self.phasen_Ablauf()
        self.frm_kont.hide()
        self.frm_kont.tbl_mess1.clearContents()
        self.frm_kont.tbl_mess2.clearContents()

    def ergebnis(self):
        print("temp_d", self.frm_denat.temp_denat)
        print("temp_a", self.frm_aneal.temp_aneal)
        print("temp_e", self.frm_elong.temp_elong)
        print("dauer_d", self.frm_zeitDef.value_denat)
        print("dauer_a", self.frm_zeitDef.value_aneal_gesamt)
        print("dauer_e", self.frm_zeitDef.value_elong_gesamt)
        print("dl", self.DL_zaehler_value)


        try:
            # INSERT INTO-Anweisung für PhasenWerte
            insert_phasen = """
            INSERT INTO PhasenWerte (Kategorien, Denaturierung, Annealing, Elongation)
            VALUES 
            ("Temperatur in °C", %s, %s, %s),
            ("Dauer in sek", %s, %s, %s)
            """
            self.cursor_phasen.execute(insert_phasen, (self.frm_denat.temp_denat, self.frm_aneal.temp_aneal, self.frm_elong.temp_elong, self.frm_zeitDef.value_denat, self.frm_zeitDef.value_aneal_gesamt, self.frm_zeitDef.value_elong_gesamt))

            # INSERT INTO-Anweisung für Messwerte
            insert_dl = """
            INSERT INTO Durchlauf (Kategorien, Anzahl)
            VALUES 
            ("Durchlauf", %s)
            """
            self.cursor_dl.execute(insert_dl, (self.DL_zaehler_value))

            # Daten aus Tabelle 'PhasenWerte' abrufen)
            self.cursor_phasen.execute("SELECT Kategorien, Denaturierung, Annealing, Elongation FROM PhasenWerte LIMIT 2")
            result_phasen = self.cursor_phasen.fetchall()

            # Daten aus Tabelle 'Messwerte' abrufen
            self.cursor_mess1.execute("SELECT Proben, Lichtstärke FROM Messwerte1 LIMIT 4")
            result_messwerte1 = self.cursor_mess1.fetchall()

            # Daten aus Tabelle 'Messwerte' abrufen
            self.cursor_mess2.execute("SELECT Proben, Lichtstärke FROM Messwerte2 LIMIT 4")
            result_messwerte2 = self.cursor_mess2.fetchall()

            # Daten aus Tabelle 'Durchlauf' abrufen
            self.cursor_dl.execute("SELECT Kategorien, Anzahl FROM Durchlauf LIMIT 1")
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
        self.frm_kont.tbl_mess1.clearContents()
        self.frm_kont.tbl_mess2.clearContents()
        self.frm_ergeb.tbl_phasen.clearContents()
        self.frm_ergeb.tbl_dl.clearContents()
        self.frm_ergeb.tbl_mess1.clearContents()
        self.frm_ergeb.tbl_mess2.clearContents()

    def shutDown(self):
        # Rock herunterfahren
        subprocess.call(['/sbin/shutdown', '-h', 'now'])

    def kontanspruch(self):
        self.posiRight = False
      
        while not self.posiRight:
            n = self.read_from_detect()
            # Nur Daten vom Slave lesen, wenn der Leseprozess nicht gestoppt wurde
            data_sent = False
            if n is None:             
                n = self.read_from_detect()

            if n == 7:
                n = self.read_from_detect()
                                    
            if n == 0:
                n = self.read_from_detect()
                
            if n == 5 and not data_sent:
                data_sent = True
                self.posiRight = True

                data_received = self.read_data()

                self.frm_kont.p1 = data_received[0] 
                self.frm_kont.p2 = data_received[1] 
                self.frm_kont.p3 = data_received[2] 
                self.frm_kont.p4 = data_received[3] 
                self.frm_kont.p5 = data_received[4] 
                self.frm_kont.p6 = data_received[5] 
                self.frm_kont.p7 = data_received[6] 
                self.frm_kont.p8 = data_received[7]

                # Die erhaltenen Daten anzeigen
                # print("Messergebnis")
                # print("Probe1:", self.frm_kont.p1)
                # print("Probe2:", self.frm_kont.p2)
                # print("Probe3:", self.frm_kont.p3)
                # print("Probe4:", self.frm_kont.p4)
                # print("Probe5:", self.frm_kont.p5)
                # print("Probe6:", self.frm_kont.p6)
                # print("Probe7:", self.frm_kont.p7)
                # print("Probe8:", self.frm_kont.p8)

        self.frm_kont.showFullScreen()
        self.frm_kontanspruch.hide()

        try:
                # INSERT INTO-Anweisung für Messwerte
                insert_messwerte1 = """
                INSERT INTO Messwerte1 (Proben, Lichtstärke)
                VALUES 
                ("P1 in Lumen", %s),
                ("P2 in Lumen", %s),
                ("P3 in Lumen", %s),
                ("P4 in Lumen", %s)
                """
                self.cursor_mess1.execute(insert_messwerte1, (self.frm_kont.p1, self.frm_kont.p2, self.frm_kont.p3, self.frm_kont.p4))

                # INSERT INTO-Anweisung für Messwerte
                insert_messwerte2 = """
                INSERT INTO Messwerte2 (Proben, Lichtstärke)
                VALUES 
                ("P5 in Lumen", %s),
                ("P6 in Lumen", %s),
                ("P7 in Lumen", %s),
                ("P8 in Lumen", %s)
                """

                self.cursor_mess2.execute(insert_messwerte2, (self.frm_kont.p5, self.frm_kont.p6, self.frm_kont.p7, self.frm_kont.p8))

                # Daten aus Tabelle 'Messwerte' abrufen
                self.cursor_mess1.execute("SELECT Proben, Lichtstärke FROM Messwerte1 LIMIT 4")
                result_messwerte1 = self.cursor_mess1.fetchall()

                
                # Daten aus Tabelle 'Messwerte' abrufen
                self.cursor_mess2.execute("SELECT Proben, Lichtstärke FROM Messwerte2 LIMIT 4")
                result_messwerte2 = self.cursor_mess2.fetchall()

                # Ergebnisse in tbl_messwerte einfügen
                for row_num, row_data in enumerate(result_messwerte1):
                    self.frm_kont.tbl_mess1.insertRow(row_num)
                    for col_num, col_data in enumerate(row_data):
                        self.frm_kont.tbl_mess1.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))
                        
                # Ergebnisse in tbl_messwerte einfügen
                for row_num, row_data in enumerate(result_messwerte2):
                    self.frm_kont.tbl_mess2.insertRow(row_num)
                    for col_num, col_data in enumerate(row_data):
                        self.frm_kont.tbl_mess2.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

        except pymysql.MySQLError as e:
                print("MySQL-Fehler: {}".format(str(e)))

        except OSError as o:
                print("Fehler: {}".format(str(o)))


    # Funktion zum Lesen von Daten vom Arduino
    def read_data(self):
        data = []
        i = 0
        self.bus.write_byte(self.detect_address, 10)
        time.sleep(1)

        for i in range(8):
            i = i+1
            self.bus.write_byte(self.detect_address, i)
            print(i)
            time.sleep(2)
            
            
        for _ in range(8):  # Wir erwarten 3 Datenpunkte (temp_denat, temp_aneal, temp_elong)
            data.append(self.bus.read_byte(self.detect_address))
            
        return data

    def read_from_detect(self):
        try:
            # Lese Daten vom Slave
            null = self.bus.read_byte(self.detect_address)
            return null
        except Exception as e:
            print("Failed to read")

app = QApplication()
frm_main = Frm_main()
frm_main.showFullScreen()
app.exec()
