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
        self.textEdit.setGeometry(QRect(60, 120, 371, 491))
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
        self.wasser_aneal = QSpinBox(self.centralwidget)
        self.wasser_aneal.setObjectName(u"wasser_aneal")
        self.wasser_aneal.setGeometry(QRect(260, 390, 161, 51))
        self.wasser_aneal.setAlignment(Qt.AlignCenter)
        self.wasser_aneal.setReadOnly(False)
        self.wasser_denat = QSpinBox(self.centralwidget)
        self.wasser_denat.setObjectName(u"wasser_denat")
        self.wasser_denat.setGeometry(QRect(260, 330, 161, 51))
        self.wasser_denat.setAlignment(Qt.AlignCenter)
        self.wasser_denat.setReadOnly(False)
        self.Dauer_line_2 = QLineEdit(self.centralwidget)
        self.Dauer_line_2.setObjectName(u"Dauer_line_2")
        self.Dauer_line_2.setGeometry(QRect(70, 400, 151, 31))
        self.Dauer_line_2.setFont(font2)
        self.Dauer_line_2.setAlignment(Qt.AlignCenter)
        self.Dauer_line_2.setReadOnly(True)
        self.wasser_elong = QSpinBox(self.centralwidget)
        self.wasser_elong.setObjectName(u"wasser_elong")
        self.wasser_elong.setGeometry(QRect(260, 450, 161, 51))
        self.wasser_elong.setAlignment(Qt.AlignCenter)
        self.wasser_elong.setReadOnly(False)
        self.Dauer_line_3 = QLineEdit(self.centralwidget)
        self.Dauer_line_3.setObjectName(u"Dauer_line_3")
        self.Dauer_line_3.setGeometry(QRect(70, 340, 151, 31))
        self.Dauer_line_3.setFont(font2)
        self.Dauer_line_3.setAlignment(Qt.AlignCenter)
        self.Dauer_line_3.setReadOnly(True)
        self.Dauer_line_4 = QLineEdit(self.centralwidget)
        self.Dauer_line_4.setObjectName(u"Dauer_line_4")
        self.Dauer_line_4.setGeometry(QRect(70, 540, 151, 31))
        self.Dauer_line_4.setFont(font2)
        self.Dauer_line_4.setAlignment(Qt.AlignCenter)
        self.Dauer_line_4.setReadOnly(True)
        self.lbl_tempdef = QLabel(self.centralwidget)
        self.lbl_tempdef.setObjectName(u"lbl_tempdef")
        self.lbl_tempdef.setGeometry(QRect(260, 530, 151, 61))
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
        self.Dauer_line_4.setText(QCoreApplication.translate("TempAnspruch", u"Ausgew\u00e4hlt:", None))
        self.lbl_tempdef.setText("")
    # retranslateUi

