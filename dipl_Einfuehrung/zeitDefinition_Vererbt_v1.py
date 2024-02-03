# Es wird eine Klasse für die Zeit-Definition erstellt
# Hier wird deklariert, dass ein MainWindow verwendet wurde und es auf die Klasse Ui_Voraussetzung zugreift.
# Diese wird von der zeitDefVoraus.py Datei entnommen 
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zeitDefVoraus_v2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTextEdit, QWidget)

class Ui_zeitDef_Voraus(object):
    def setupUi(self, zeitDef_Voraus):
        if not zeitDef_Voraus.objectName():
            zeitDef_Voraus.setObjectName(u"zeitDef_Voraus")
        zeitDef_Voraus.resize(489, 733)
        self.centralwidget = QWidget(zeitDef_Voraus)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 130, 431, 461))
        self.textEdit.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-2, 50, 491, 61))
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(30)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_Weiter = QPushButton(self.centralwidget)
        self.btn_Weiter.setObjectName(u"btn_Weiter")
        self.btn_Weiter.setGeometry(QRect(170, 610, 151, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial Narrow"])
        font1.setPointSize(20)
        self.btn_Weiter.setFont(font1)
        self.Dauer_line = QLineEdit(self.centralwidget)
        self.Dauer_line.setObjectName(u"Dauer_line")
        self.Dauer_line.setGeometry(QRect(70, 530, 151, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial Narrow"])
        font2.setPointSize(15)
        self.Dauer_line.setFont(font2)
        self.Dauer_line.setAlignment(Qt.AlignCenter)
        self.Dauer_line.setReadOnly(True)
        self.wasserDauer_elong = QSpinBox(self.centralwidget)
        self.wasserDauer_elong.setObjectName(u"wasserDauer_elong")
        self.wasserDauer_elong.setRange(20, 60)    # Setze die Mindest- und Höchstwerte
        self.wasserDauer_elong.setValue(40)    # Setze den Startwert
        self.wasserDauer_elong.setGeometry(QRect(260, 520, 161, 51))
        self.wasserDauer_elong.setAlignment(Qt.AlignCenter)
        self.wasserDauer_elong.setReadOnly(False)
        self.Dauer_line_2 = QLineEdit(self.centralwidget)
        self.Dauer_line_2.setObjectName(u"Dauer_line_2")
        self.Dauer_line_2.setGeometry(QRect(70, 470, 151, 31))
        self.Dauer_line_2.setFont(font2)
        self.Dauer_line_2.setAlignment(Qt.AlignCenter)
        self.Dauer_line_2.setReadOnly(True)
        self.wasserDauer_aneal = QSpinBox(self.centralwidget)
        self.wasserDauer_aneal.setObjectName(u"wasserDauer_aneal")
        self.wasserDauer_aneal.setRange(30, 60)    # Setze die Mindest- und Höchstwerte
        self.wasserDauer_aneal.setValue(45)    # Setze den Startwert
        self.wasserDauer_aneal.setGeometry(QRect(260, 460, 161, 51))
        self.wasserDauer_aneal.setAlignment(Qt.AlignCenter)
        self.wasserDauer_aneal.setReadOnly(False)
        self.Dauer_line_3 = QLineEdit(self.centralwidget)
        self.Dauer_line_3.setObjectName(u"Dauer_line_3")
        self.Dauer_line_3.setGeometry(QRect(70, 410, 151, 31))
        self.Dauer_line_3.setFont(font2)
        self.Dauer_line_3.setAlignment(Qt.AlignCenter)
        self.Dauer_line_3.setReadOnly(True)
        self.wasserDauer_denat = QSpinBox(self.centralwidget)
        self.wasserDauer_denat.setObjectName(u"wasserDauer_denat")
        self.wasserDauer_denat.setRange(10, 60)    # Setze die Mindest- und Höchstwerte
        self.wasserDauer_denat.setValue(35)    # Setze den Startwert
        self.wasserDauer_denat.setGeometry(QRect(260, 400, 161, 51))
        self.wasserDauer_denat.setAlignment(Qt.AlignCenter)
        self.wasserDauer_denat.setReadOnly(False)
        zeitDef_Voraus.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(zeitDef_Voraus)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        zeitDef_Voraus.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(zeitDef_Voraus)
        self.statusbar.setObjectName(u"statusbar")
        zeitDef_Voraus.setStatusBar(self.statusbar)

        self.retranslateUi(zeitDef_Voraus)

        QMetaObject.connectSlotsByName(zeitDef_Voraus)
    # setupUi

    def retranslateUi(self, zeitDef_Voraus):
        zeitDef_Voraus.setWindowTitle(QCoreApplication.translate("zeitDef_Voraus", u"Voraussetzungen", None))
        self.textEdit.setHtml(QCoreApplication.translate("zeitDef_Voraus", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#9cd4d6\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Bitte definieren Sie je nach verwendetem Primer, wie lange die Probe in den einzelnen Phasen sein soll.<br />Nachdem Sie fertig sind und die Probe eingelegt wurde, bet\u00e4tigen Sie bitte den WEITER Button. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-blo"
                        "ck-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Denaturiernugsdauer: 10 Sek - 1 Min</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Annealingsdauer: 30 Sek - 1 Min</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Elongationsdauer: 20 Sek - 1 Min</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("zeitDef_Voraus", u"Dauerbestimmung", None))
        self.btn_Weiter.setText(QCoreApplication.translate("zeitDef_Voraus", u"Weiter", None))
        self.Dauer_line.setText(QCoreApplication.translate("zeitDef_Voraus", u"Elongation:", None))
        self.Dauer_line_2.setText(QCoreApplication.translate("zeitDef_Voraus", u"Annealing:", None))
        self.Dauer_line_3.setText(QCoreApplication.translate("zeitDef_Voraus", u"Danaturierung:", None))
    # retranslateUi

class Frm_zeitDef(QMainWindow, Ui_zeitDef_Voraus):
    def __init__(self):
        super().__init__()
        # Initialisierung der Benutzeroberfläche 
        self.setupUi(self)

        # Standardwerte setzen
        self.value_denat = 35
        self.value_aneal = 45 * (1/3) + self.value_denat
        self.value_sens = 45 * (1/3) + self.value_aneal
        self.value_asens = 45 * (1/3) + self.value_sens
        self.value_elong = 40 + self.value_asens
        self.value_aneal_gesamt = 45
        self.value_elong_gesamt = 40

        # Ändert sich der Wert von wasserDauer_..., so wird die jeweilige Methode aufgerufen
        self.wasserDauer_denat.valueChanged.connect(self.Value_Denat_change)
        self.wasserDauer_aneal.valueChanged.connect(self.Value_Aneal_change)
        self.wasserDauer_elong.valueChanged.connect(self.Value_Elong_change)

    def Value_Denat_change(self, value):
        # neuer Wert wird in der Instanz-Variable value_denat gespeichert
        self.value_denat = self.wasserDauer_denat.value()
        # neuer Wert wird ausgegeben
        print(f"DenatWert: {value}")

    def Value_Aneal_change(self, value):
        # neuer Wert wird durch 3 geteilt und in den Instanz-Variablen gespeichert
        # Instanz-Variable wird mit dem jeweils vorherigen Wert addiert, um sicherzustellen, dass sie alle nach einander ablaufen
        self.value_aneal_gesamt = self.wasserDauer_aneal.value()
        self.value_aneal = self.wasserDauer_aneal.value() * (1/3) + self.value_denat
        self.value_sens = self.wasserDauer_aneal.value() * (1/3) + self.value_aneal
        self.value_asens = self.wasserDauer_aneal.value() * (1/3) + self.value_sens
        # der orgiginal Wert (bevor 3-facher Teilung) wird ausgegeben
        print(f"AnealWert: {value}")
        
    def Value_Elong_change(self, value):
        # neuer Wert wird in der Instanz-Variable value_elong gespeichert
        # Instanz-Variable wird mit dem jeweils vorherigen Wert addiert, um sicherzustellen, dass sie alle nach einander ablaufen
        self.value_elong_gesamt = self.wasserDauer_elong.value()
        self.value_elong = self.wasserDauer_elong.value() + self.value_asens
        # neuer Wert wird ausgegeben
        print(f"ElongWert: {value}")