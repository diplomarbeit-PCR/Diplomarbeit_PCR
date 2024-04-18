# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EinfuehrungAnspruchWindow_v1.ui'
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

class Ui_TempAnspruch(object):
    def setupUi(self, TempAnspruch):
        if not TempAnspruch.objectName():
            TempAnspruch.setObjectName(u"TempAnspruch")
        TempAnspruch.resize(489, 733)
        self.centralwidget = QWidget(TempAnspruch)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(60, 120, 371, 421))
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
        self.Dauer_line = QLineEdit(self.centralwidget)
        self.Dauer_line.setObjectName(u"Dauer_line")
        self.Dauer_line.setGeometry(QRect(70, 460, 151, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial Narrow"])
        font2.setPointSize(15)
        self.Dauer_line.setFont(font2)
        self.Dauer_line.setAlignment(Qt.AlignCenter)
        self.Dauer_line.setReadOnly(True)
        self.wasserTemp_aneal = QSpinBox(self.centralwidget)
        self.wasserTemp_aneal.setObjectName(u"wasserTemp_aneal")
        self.wasserTemp_aneal.setGeometry(QRect(260, 390, 161, 51))
        self.wasserTemp_aneal.setAlignment(Qt.AlignCenter)
        self.wasserTemp_aneal.setReadOnly(False)
        self.wasserTemp_denat = QSpinBox(self.centralwidget)
        self.wasserTemp_denat.setObjectName(u"wasserTemp_denat")
        self.wasserTemp_denat.setGeometry(QRect(260, 330, 161, 51))
        self.wasserTemp_denat.setAlignment(Qt.AlignCenter)
        self.wasserTemp_denat.setReadOnly(False)
        self.Dauer_line_2 = QLineEdit(self.centralwidget)
        self.Dauer_line_2.setObjectName(u"Dauer_line_2")
        self.Dauer_line_2.setGeometry(QRect(70, 400, 151, 31))
        self.Dauer_line_2.setFont(font2)
        self.Dauer_line_2.setAlignment(Qt.AlignCenter)
        self.Dauer_line_2.setReadOnly(True)
        self.wasserTemp_elong = QSpinBox(self.centralwidget)
        self.wasserTemp_elong.setObjectName(u"wasserTemp_elong")
        self.wasserTemp_elong.setGeometry(QRect(260, 450, 161, 51))
        self.wasserTemp_elong.setAlignment(Qt.AlignCenter)
        self.wasserTemp_elong.setReadOnly(False)
        self.Dauer_line_3 = QLineEdit(self.centralwidget)
        self.Dauer_line_3.setObjectName(u"Dauer_line_3")
        self.Dauer_line_3.setGeometry(QRect(70, 340, 151, 31))
        self.Dauer_line_3.setFont(font2)
        self.Dauer_line_3.setAlignment(Qt.AlignCenter)
        self.Dauer_line_3.setReadOnly(True)
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
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Bitte dr\u00fccken Sie erst auf WEITER, wenn alle LCD-Anzeigen Gr\u00fcn geschalten sind. Dies bedeutet, dass sich die Temperaturen im gew\u00fcnschten Toleranzenbereich befinden. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-ind"
                        "ent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Dies ist erforderlich, da es keine sp\u00e4tere Kontrolle der Korrektheit der Temperatur gibt.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("TempAnspruch", u"Temperaturkontrolle", None))
        self.btn_Weiter.setText(QCoreApplication.translate("TempAnspruch", u"Weiter", None))
        self.Dauer_line.setText(QCoreApplication.translate("TempAnspruch", u"Elongation:", None))
        self.Dauer_line_2.setText(QCoreApplication.translate("TempAnspruch", u"Annealing:", None))
        self.Dauer_line_3.setText(QCoreApplication.translate("TempAnspruch", u"Denaturierung:", None))
    # retranslateUi


class Frm_tempanspruch(QMainWindow, Ui_TempAnspruch):
    def __init__(self):
        super().__init__()
        self.setupUi(self)