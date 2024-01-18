# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KontrollWindow_v1.ui'
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_Kontrolle(object):
    def setupUi(self, Kontrolle):
        if not Kontrolle.objectName():
            Kontrolle.setObjectName(u"Kontrolle")
        Kontrolle.resize(489, 733)
        self.centralwidget = QWidget(Kontrolle)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(70, 120, 351, 331))
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
        self.btn_Beenden = QPushButton(self.centralwidget)
        self.btn_Beenden.setObjectName(u"btn_Beenden")
        self.btn_Beenden.setGeometry(QRect(290, 610, 151, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial Narrow"])
        font1.setPointSize(20)
        self.btn_Beenden.setFont(font1)
        self.btn_Fortfuehren = QPushButton(self.centralwidget)
        self.btn_Fortfuehren.setObjectName(u"btn_Fortfuehren")
        self.btn_Fortfuehren.setGeometry(QRect(40, 610, 151, 51))
        self.btn_Fortfuehren.setFont(font1)
        self.Spg_line = QLineEdit(self.centralwidget)
        self.Spg_line.setObjectName(u"Spg_line")
        self.Spg_line.setGeometry(QRect(260, 490, 111, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial Narrow"])
        font2.setPointSize(15)
        self.Spg_line.setFont(font2)
        self.Spg_line.setAlignment(Qt.AlignCenter)
        self.Spg_line.setReadOnly(True)
        self.Spg_detekt = QLCDNumber(self.centralwidget)
        self.Spg_detekt.setObjectName(u"Spg_detekt")
        self.Spg_detekt.setGeometry(QRect(260, 530, 111, 51))
        self.Licht_detekt = QLCDNumber(self.centralwidget)
        self.Licht_detekt.setObjectName(u"Licht_detekt")
        self.Licht_detekt.setGeometry(QRect(90, 530, 121, 51))
        self.Licht_line = QLineEdit(self.centralwidget)
        self.Licht_line.setObjectName(u"Licht_line")
        self.Licht_line.setGeometry(QRect(90, 490, 121, 31))
        self.Licht_line.setFont(font2)
        self.Licht_line.setAlignment(Qt.AlignCenter)
        self.Licht_line.setReadOnly(True)
        Kontrolle.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Kontrolle)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        Kontrolle.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Kontrolle)
        self.statusbar.setObjectName(u"statusbar")
        Kontrolle.setStatusBar(self.statusbar)

        self.retranslateUi(Kontrolle)

        QMetaObject.connectSlotsByName(Kontrolle)
    # setupUi

    def retranslateUi(self, Kontrolle):
        Kontrolle.setWindowTitle(QCoreApplication.translate("Kontrolle", u"Kontrolle", None))
        self.textEdit.setHtml(QCoreApplication.translate("Kontrolle", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#9cd4d6\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Mit einer blauen LED und einer Sammellinse entsteht ein Brennpunkt auf der Probe, was zu einer Anregung f\u00fchrt. Es kommt zu einer Emittierung von gr\u00fcnem Licht. Dieses durchdringt einen Streufilter, welches den kurzwelligen Anteil filtert.<br />Das \u00fcbrigbleibende gr\u00fcne Licht trifft auf die"
                        " im Deckel enthaltene Fotodiode, welche bei dem kontakt mit Licht Strom erzeugt. <br />Ein Transimpetanzwandler verst\u00e4rkt diesen und erzeugt Spannung im mV Bereich. <br />Der Arduino liest diese ein und misst daraus die Lichtintensit\u00e4t in Millilumen.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Kontrolle", u"Kontrolle", None))
        self.btn_Beenden.setText(QCoreApplication.translate("Kontrolle", u"Beenden", None))
        self.btn_Fortfuehren.setText(QCoreApplication.translate("Kontrolle", u"Fortf\u00fchren", None))
        self.Spg_line.setText(QCoreApplication.translate("Kontrolle", u"Spannung:", None))
        self.Licht_line.setText(QCoreApplication.translate("Kontrolle", u"Lichtintensit\u00e4t:", None))
    # retranslateUi

