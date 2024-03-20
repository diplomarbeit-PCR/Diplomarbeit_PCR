# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tempDefVoraus_v1.ui'
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

class Ui_tempDef_Voraus(object):
    def setupUi(self, tempDef_Voraus):
        if not tempDef_Voraus.objectName():
            tempDef_Voraus.setObjectName(u"tempDef_Voraus")
        tempDef_Voraus.resize(489, 733)
        self.centralwidget = QWidget(tempDef_Voraus)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 130, 431, 471))
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
        self.Dauer_line.setGeometry(QRect(70, 550, 151, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial Narrow"])
        font2.setPointSize(15)
        self.Dauer_line.setFont(font2)
        self.Dauer_line.setAlignment(Qt.AlignCenter)
        self.Dauer_line.setReadOnly(True)
        self.wasserTemp_elong = QSpinBox(self.centralwidget)
        self.wasserTemp_elong.setObjectName(u"wasserTemp_elong")
        self.wasserTemp_elong.setGeometry(QRect(260, 540, 161, 51))
        self.wasserTemp_elong.setAlignment(Qt.AlignCenter)
        self.wasserTemp_elong.setReadOnly(False)
        self.Dauer_line_2 = QLineEdit(self.centralwidget)
        self.Dauer_line_2.setObjectName(u"Dauer_line_2")
        self.Dauer_line_2.setGeometry(QRect(70, 490, 151, 31))
        self.Dauer_line_2.setFont(font2)
        self.Dauer_line_2.setAlignment(Qt.AlignCenter)
        self.Dauer_line_2.setReadOnly(True)
        self.wasserTemp_aneal = QSpinBox(self.centralwidget)
        self.wasserTemp_aneal.setObjectName(u"wasserTemp_aneal")
        self.wasserTemp_aneal.setGeometry(QRect(260, 480, 161, 51))
        self.wasserTemp_aneal.setAlignment(Qt.AlignCenter)
        self.wasserTemp_aneal.setReadOnly(False)
        self.Dauer_line_3 = QLineEdit(self.centralwidget)
        self.Dauer_line_3.setObjectName(u"Dauer_line_3")
        self.Dauer_line_3.setGeometry(QRect(70, 430, 151, 31))
        self.Dauer_line_3.setFont(font2)
        self.Dauer_line_3.setAlignment(Qt.AlignCenter)
        self.Dauer_line_3.setReadOnly(True)
        self.wasserTemp_denat = QSpinBox(self.centralwidget)
        self.wasserTemp_denat.setObjectName(u"wasserTemp_denat")
        self.wasserTemp_denat.setGeometry(QRect(260, 420, 161, 51))
        self.wasserTemp_denat.setAlignment(Qt.AlignCenter)
        self.wasserTemp_denat.setReadOnly(False)
        tempDef_Voraus.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(tempDef_Voraus)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        tempDef_Voraus.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(tempDef_Voraus)
        self.statusbar.setObjectName(u"statusbar")
        tempDef_Voraus.setStatusBar(self.statusbar)

        self.retranslateUi(tempDef_Voraus)

        QMetaObject.connectSlotsByName(tempDef_Voraus)
    # setupUi

    def retranslateUi(self, tempDef_Voraus):
        tempDef_Voraus.setWindowTitle(QCoreApplication.translate("tempDef_Voraus", u"Voraussetzungen", None))
        self.textEdit.setHtml(QCoreApplication.translate("tempDef_Voraus", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#9cd4d6\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Bitte definieren Sie je nach verwendetem Primer, welche Temperaturen in den einzelnen Phasen realisiert sein sollen.<br />Bitte beachten SIe, dass Toleranzen von +/- 2\u00b0C gegeben sind.<br />Nachdem Sie fertig sind, bet\u00e4tigen Sie bitte den WEITER Button. </span></p>\n"
"<p style=\" margin-top:12px; margin-"
                        "bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Denaturierungsdauer: 94\u00b0C - 98\u00b0C</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Annealingsdauer: 50\u00b0C - 65\u00b0C</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Elongationsdauer: 68\u00b0C - 72\u00b0C</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("tempDef_Voraus", u"Temperaturbestimmung", None))
        self.btn_Weiter.setText(QCoreApplication.translate("tempDef_Voraus", u"Weiter", None))
        self.Dauer_line.setText(QCoreApplication.translate("tempDef_Voraus", u"Elongation:", None))
        self.Dauer_line_2.setText(QCoreApplication.translate("tempDef_Voraus", u"Annealing:", None))
        self.Dauer_line_3.setText(QCoreApplication.translate("tempDef_Voraus", u"Denaturierung:", None))
    # retranslateUi

