# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EInfuehrungAnspruchWindow_v1.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_TempAnspruch(object):
    def setupUi(self, TempAnspruch):
        if not TempAnspruch.objectName():
            TempAnspruch.setObjectName(u"TempAnspruch")
        TempAnspruch.resize(489, 733)
        self.centralwidget = QWidget(TempAnspruch)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(60, 120, 371, 301))
        self.textEdit.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-2, 50, 491, 61))
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(35)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_Weiter = QPushButton(self.centralwidget)
        self.btn_Weiter.setObjectName(u"btn_Weiter")
        self.btn_Weiter.setGeometry(QRect(170, 620, 151, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial Narrow"])
        font1.setPointSize(20)
        self.btn_Weiter.setFont(font1)
        self.temp_lbl = QLabel(self.centralwidget)
        self.temp_lbl.setObjectName(u"temp_lbl")
        self.temp_lbl.setPixmap(QPixmap(r"/home/arog/Diplomarbeit_PCR/dipl_Einfuehrung/LEDUebergang.png"))
        self.temp_lbl.setGeometry(QRect(60, 440, 361, 171))
        TempAnspruch.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TempAnspruch)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        TempAnspruch.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TempAnspruch)
        self.statusbar.setObjectName(u"statusbar")
        TempAnspruch.setStatusBar(self.statusbar)

        self.retranslateUi(TempAnspruch)

        QMetaObject.connectSlotsByName(TempAnspruch)
    # setupUi

    def retranslateUi(self, TempAnspruch):
        TempAnspruch.setWindowTitle(QCoreApplication.translate("TempAnspruch", u"Einf\u00fchrung", None))
        self.textEdit.setHtml(QCoreApplication.translate("TempAnspruch", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#9cd4d6\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Jedes Heizbad hat eine LED angebracht.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Leuchtet die Diode rot, so ist noch nicht die gew\u00fcns"
                        "chte Temperatur erreicht.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Wenn das Licht auf Gr\u00fcn umschaltet, so befindet sich das Heizbad in dem Toleranzbereich der angegebenen Temperatur.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Bitte dr\u00fccken Sie erst auf WEITER, wenn alle LEDs Gr\u00fcn geschalten sind. Dies ist erforderlich, da es keine sp\u00e4tere Kontrolle der Korrektheit der Temperatur gibt.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("TempAnspruch", u"Temperaturkontrolle", None))
        self.btn_Weiter.setText(QCoreApplication.translate("TempAnspruch", u"Weiter", None))
        self.temp_lbl.setText("")
    # retranslateUi

class Frm_tempanspruch(QMainWindow, Ui_TempAnspruch):
    def __init__(self):
        super().__init__()
        self.setupUi(self)