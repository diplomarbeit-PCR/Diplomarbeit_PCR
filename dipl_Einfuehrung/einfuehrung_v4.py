# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'einfuehrung_v4.ui'
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

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.setEnabled(True)
        StartWindow.resize(489, 733)
        font = QFont()
        font.setFamilies([u"Arial Narrow"])
        StartWindow.setFont(font)
        StartWindow.setTabletTracking(False)
        StartWindow.setAcceptDrops(False)
        StartWindow.setWindowTitle(u"eduPCR")
        StartWindow.setAnimated(False)
        self.actionHistory = QAction(StartWindow)
        self.actionHistory.setObjectName(u"actionHistory")
        self.actionLog_In = QAction(StartWindow)
        self.actionLog_In.setObjectName(u"actionLog_In")
        self.actionShut_Down = QAction(StartWindow)
        self.actionShut_Down.setObjectName(u"actionShut_Down")
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_Start = QPushButton(self.centralwidget)
        self.btn_Start.setObjectName(u"btn_Start")
        self.btn_Start.setGeometry(QRect(150, 620, 191, 51))
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
        StartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(StartWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 20))
        self.menuShutDown = QMenu(self.menubar)
        self.menuShutDown.setObjectName(u"menuShutDown")
        StartWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(StartWindow)
        self.statusbar.setObjectName(u"statusbar")
        StartWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuShutDown.menuAction())
        self.menuShutDown.addAction(self.actionShut_Down)

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        self.actionHistory.setText(QCoreApplication.translate("StartWindow", u"History", None))
        self.actionLog_In.setText(QCoreApplication.translate("StartWindow", u"Log In", None))
        self.actionShut_Down.setText(QCoreApplication.translate("StartWindow", u"Shut Down", None))
        self.btn_Start.setText(QCoreApplication.translate("StartWindow", u"Start", None))
        self.txt_Einfuehrung.setHtml(QCoreApplication.translate("StartWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">PCR (Polymerase-Chain-Reaction) ist ein Verfahren, um bestimmte Teile der DNA zu vermehren.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Hierbei dienen die Sequenzen als Vorlage f\u00fcr weitere DNA-Str\u00e4nge. Dadurch kommt es zu einem Anstieg von den gesuchten Sequenzen. Durch dieses Verfahren k\u00f6nnen Erbkrankheiten oder Virusinfektionen festgestellt werden, doch k\u00f6nnen nur kurze DNA-Str\u00e4nge verwendet werden.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Um den PCR-Ablauf zu starten, m\u00fcssen Sie den Start-Knopf bet\u00e4tigen.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Danach wird die entnommene Probe die 3 Phasen des PCR Grundprinzips.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Wir w\u00fcnschen Ihnen im Namen der Gruppe viel Spa\u00df und ein gutes Lernverst\u00e4ndnis. </span></p></body></html>", None))
        self.lbl_Einfuehrung.setText(QCoreApplication.translate("StartWindow", u"Prozessstart", None))
        self.menuShutDown.setTitle(QCoreApplication.translate("StartWindow", u"Ausschalten", None))
        pass
    # retranslateUi

