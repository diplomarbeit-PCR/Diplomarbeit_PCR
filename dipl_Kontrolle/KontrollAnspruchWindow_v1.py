# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KontrollAnspruchWindow_v1.ui'
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

class Ui_KontrollAnspruch(object):
    def setupUi(self, KontrollAnspruch):
        if not KontrollAnspruch.objectName():
            KontrollAnspruch.setObjectName(u"KontrollAnspruch")
        KontrollAnspruch.resize(489, 733)
        self.centralwidget = QWidget(KontrollAnspruch)
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
        self.btn_Weiter.setGeometry(QRect(160, 580, 151, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial Narrow"])
        font1.setPointSize(20)
        self.btn_Weiter.setFont(font1)
        KontrollAnspruch.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(KontrollAnspruch)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        KontrollAnspruch.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(KontrollAnspruch)
        self.statusbar.setObjectName(u"statusbar")
        KontrollAnspruch.setStatusBar(self.statusbar)

        self.retranslateUi(KontrollAnspruch)

        QMetaObject.connectSlotsByName(KontrollAnspruch)
    # setupUi

    def retranslateUi(self, KontrollAnspruch):
        KontrollAnspruch.setWindowTitle(QCoreApplication.translate("KontrollAnspruch", u"Kontrolle", None))
        self.textEdit.setHtml(QCoreApplication.translate("KontrollAnspruch", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#9cd4d6\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Mit einer blauen LED und einer Sammellinse entsteht ein Brennpunkt auf der Probe, was zu einer Anregung f\u00fchrt. Es kommt zu einer Emittierung von gr\u00fcnem Licht. Dieses durchdringt einen Streufilter, welches den kurzwelligen Anteil filtert.<br />Das \u00fcbrigbleibende gr\u00fcne Licht trifft auf die"
                        " im Deckel enthaltene Fotodiode, welche bei dem Kontakt mit Licht Strom erzeugt. <br />Ein Transimpetanzwandler verst\u00e4rkt diesen und erzeugt Spannung im mV Bereich. <br />Der Arduino liest diese ein und misst daraus die Lichtintensit\u00e4t in Millilumen.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Bitte dr\u00fccken Sie erst auf WEITER, wenn Sie die Probe von dem Bewegmechanismus in die Detektorhalterung bef\u00f6rdert haben.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("KontrollAnspruch", u"Kontrollanspr\u00fcche", None))
        self.btn_Weiter.setText(QCoreApplication.translate("KontrollAnspruch", u"Weiter", None))
    # retranslateUi

