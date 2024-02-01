# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ErgebnisWindow_v1.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableView, QWidget)

class Ui_Ergebnis(object):
    def setupUi(self, Ergebnis):
        if not Ergebnis.objectName():
            Ergebnis.setObjectName(u"Ergebnis")
        Ergebnis.resize(490, 733)
        self.centralwidget = QWidget(Ergebnis)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-2, 50, 491, 61))
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(35)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_Ende = QPushButton(self.centralwidget)
        self.btn_Ende.setObjectName(u"btn_Ende")
        self.btn_Ende.setGeometry(QRect(170, 610, 151, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial Narrow"])
        font1.setPointSize(20)
        self.btn_Ende.setFont(font1)
        self.tbl_phasen = QTableWidget()
        self.tbl_phasen = QTableView(self.centralwidget)
        self.tbl_phasen.setObjectName(u"tbl_phasen")
        self.tbl_phasen.setGeometry(QRect(0, 120, 491, 261))
        self.tbl_mess = QTableWidget()
        self.tbl_mess = QTableView(self.centralwidget)
        self.tbl_mess.setObjectName(u"tbl_mess")
        self.tbl_mess.setGeometry(QRect(0, 390, 491, 211))
        Ergebnis.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Ergebnis)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 490, 22))
        Ergebnis.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Ergebnis)
        self.statusbar.setObjectName(u"statusbar")
        Ergebnis.setStatusBar(self.statusbar)

        self.retranslateUi(Ergebnis)

        QMetaObject.connectSlotsByName(Ergebnis)
    # setupUi

    def retranslateUi(self, Ergebnis):
        Ergebnis.setWindowTitle(QCoreApplication.translate("Ergebnis", u"Ergebnis", None))
        self.label.setText(QCoreApplication.translate("Ergebnis", u"Ergebnis", None))
        self.btn_Ende.setText(QCoreApplication.translate("Ergebnis", u"Beenden", None))
    # retranslateUi

