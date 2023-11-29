# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vorraussetzung_v1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_Vorraussetzung(object):
    def setupUi(self, Vorraussetzung):
        if not Vorraussetzung.objectName():
            Vorraussetzung.setObjectName(u"Vorraussetzung")
        Vorraussetzung.resize(489, 733)
        self.centralwidget = QWidget(Vorraussetzung)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 130, 431, 231))
        self.textEdit.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-2, 50, 491, 61))
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(40)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.Vorraus_lbl = QLabel(self.centralwidget)
        self.Vorraus_lbl.setObjectName(u"Vorraus_lbl")
        self.Vorraus_lbl.setGeometry(QRect(20, 370, 451, 301))
        self.Vorraus_lbl.setPixmap(QPixmap(r"C:\Daten_Amelie\DA\App\GitHub\Diplomarbeit_PCR\dipl_Einfuehrung\pcrGrundprinzip.png"))
        self.Vorraus_lbl.setScaledContents(True)
        Vorraussetzung.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Vorraussetzung)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        Vorraussetzung.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Vorraussetzung)
        self.statusbar.setObjectName(u"statusbar")
        Vorraussetzung.setStatusBar(self.statusbar)

        self.retranslateUi(Vorraussetzung)

        QMetaObject.connectSlotsByName(Vorraussetzung)
    # setupUi

    def retranslateUi(self, Vorraussetzung):
        Vorraussetzung.setWindowTitle(QCoreApplication.translate("Vorraussetzung", u"Vorraussetzungen", None))
        self.textEdit.setHtml(QCoreApplication.translate("Vorraussetzung", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#9cd4d6\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Es muss die DNA-Sequenz des suchenden Strangs wie die Probe vorliegen. Um mit dem Prozess zu beginnen werden sogenannte Primer und Enzyme ben\u00f6tigt. <br />Ein Primer gibt den Beginn der Polymerase an. Durch diesen werden unterschiedliche DNA-Abschnitte repliziert. <br />Enzyme induzieren die Reaktionen und red"
                        "uzieren die Aktivierungsenergie. </span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Vorraussetzung", u"Vorraussetzungen", None))
        self.Vorraus_lbl.setText("")
    # retranslateUi

