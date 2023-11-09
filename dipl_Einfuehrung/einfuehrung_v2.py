# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'einfuehrung_v2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(489, 733)
        font = QFont()
        font.setFamilies([u"Arial Narrow"])
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowTitle(u"eduPCR")
        MainWindow.setAnimated(False)
        self.actionHistory = QAction(MainWindow)
        self.actionHistory.setObjectName(u"actionHistory")
        self.actionLog_In = QAction(MainWindow)
        self.actionLog_In.setObjectName(u"actionLog_In")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_Start = QPushButton(self.centralwidget)
        self.btn_Start.setObjectName(u"btn_Start")
        self.btn_Start.setGeometry(QRect(140, 610, 200, 50))
        font1 = QFont()
        font1.setFamilies([u"Arial Narrow"])
        font1.setPointSize(20)
        font1.setBold(False)
        self.btn_Start.setFont(font1)
        self.txt_Einfuehrung = QTextEdit(self.centralwidget)
        self.txt_Einfuehrung.setObjectName(u"txt_Einfuehrung")
        self.txt_Einfuehrung.setEnabled(True)
        self.txt_Einfuehrung.setGeometry(QRect(30, 100, 421, 481))
        font2 = QFont()
        font2.setFamilies([u"Arial Narrow"])
        font2.setPointSize(20)
        font2.setKerning(False)
        self.txt_Einfuehrung.setFont(font2)
        self.txt_Einfuehrung.setAcceptDrops(False)
        self.txt_Einfuehrung.setReadOnly(True)
        self.txt_Einfuehrung.setAcceptRichText(True)
        self.lbl_Einfuehrung = QLabel(self.centralwidget)
        self.lbl_Einfuehrung.setObjectName(u"lbl_Einfuehrung")
        self.lbl_Einfuehrung.setGeometry(QRect(0, 30, 481, 50))
        font3 = QFont()
        font3.setFamilies([u"Tw Cen MT"])
        font3.setPointSize(40)
        font3.setBold(False)
        self.lbl_Einfuehrung.setFont(font3)
        self.lbl_Einfuehrung.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 20))
        self.menuProzessstart = QMenu(self.menubar)
        self.menuProzessstart.setObjectName(u"menuProzessstart")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuProzessstart.menuAction())
        self.menuProzessstart.addAction(self.actionHistory)
        self.menuProzessstart.addAction(self.actionLog_In)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.actionHistory.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.actionLog_In.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.btn_Start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.txt_Einfuehrung.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial Narrow'; font-size:20pt; font-weight:400; font-style:normal;\" bgcolor=\"#9cd4d6\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">WILLKOMMEN bei eduPCR </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">Eine Entwicklung von F\u00fcrhacker, Hinterstoisser, Karrer und Rogi </span></p>\n"
"<p style=\"-qt-paragraph-type:emp"
                        "ty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">PCR (Polymerase-Chain-Reaction) ist ein Verfahren, um bestimmte Teile-der DNA zu vermehren.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Hierbei dienen die Sequenzen als Vorlage f\u00fcr weitere DNA-Str\u00e4nge. Daeurch kommt es zu einem Anstieg von den gesuchten Sequenzen. Durch dieses Verfahren k\u00f6nnen Erbkrankheiten oder Virusinfektionen festgestellt werden, doch k\u00f6nnen nur kurze DNA-Str\u00e4nge verwendet werden.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Um den PCR-Ablauf zu starten, m\u00fcssen Sie den Start-Knopf bet\u00e4tigen.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Nach dem Dr\u00fccken, durchl\u00e4uft die entnommene Probe die 3 Phasen des PCR Grundprinzips.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Wir w\u00fcnschen Ihnen im Namen der Gruppe viel Spa\u00df und ein gutes Lernverst\u00e4ndnis. </span></p></body></html>", None))
        self.lbl_Einfuehrung.setText(QCoreApplication.translate("MainWindow", u"Prozessstart", None))
        self.menuProzessstart.setTitle(QCoreApplication.translate("MainWindow", u"Prozessstart", None))
        pass
    # retranslateUi

