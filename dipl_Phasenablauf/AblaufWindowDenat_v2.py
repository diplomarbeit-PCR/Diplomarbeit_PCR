# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AblaufWindowDenat_v2.ui'
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
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_AblaufWindowDenat(object):
    def setupUi(self, AblaufWindowDenat):
        if not AblaufWindowDenat.objectName():
            AblaufWindowDenat.setObjectName(u"AblaufWindowDenat")
        AblaufWindowDenat.resize(489, 733)
        self.centralwidget = QWidget(AblaufWindowDenat)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(70, 140, 351, 301))
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
        self.btn_Kontrolle = QPushButton(self.centralwidget)
        self.btn_Kontrolle.setObjectName(u"btn_Kontrolle")
        self.btn_Kontrolle.setGeometry(QRect(170, 610, 151, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial Narrow"])
        font1.setPointSize(20)
        self.btn_Kontrolle.setFont(font1)
        self.DL_zaehler = QLCDNumber(self.centralwidget)
        self.DL_zaehler.setObjectName(u"DL_zaehler")
        self.DL_zaehler.setGeometry(QRect(370, 500, 101, 51))
        self.DL_line = QLineEdit(self.centralwidget)
        self.DL_line.setObjectName(u"DL_line")
        self.DL_line.setGeometry(QRect(370, 460, 101, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial Narrow"])
        font2.setPointSize(15)
        self.DL_line.setFont(font2)
        self.DL_line.setAlignment(Qt.AlignCenter)
        self.DL_line.setReadOnly(True)
        self.Timer_zaehler = QLCDNumber(self.centralwidget)
        self.Timer_zaehler.setObjectName(u"Timer_zaehler")
        self.Timer_zaehler.setGeometry(QRect(40, 500, 121, 51))
        self.Dauer_line = QLineEdit(self.centralwidget)
        self.Dauer_line.setObjectName(u"Dauer_line")
        self.Dauer_line.setGeometry(QRect(40, 460, 121, 31))
        self.Dauer_line.setFont(font2)
        self.Dauer_line.setAlignment(Qt.AlignCenter)
        self.Dauer_line.setReadOnly(True)
        self.temp_sensD = QLCDNumber(self.centralwidget)
        self.temp_sensD.setObjectName(u"temp_sensD")
        self.temp_sensD.setGeometry(QRect(210, 500, 111, 51))
        self.Temp_line = QLineEdit(self.centralwidget)
        self.Temp_line.setObjectName(u"Temp_line")
        self.Temp_line.setGeometry(QRect(210, 460, 111, 31))
        self.Temp_line.setFont(font2)
        self.Temp_line.setAlignment(Qt.AlignCenter)
        self.Temp_line.setReadOnly(True)
        self.progressBar_denat = QProgressBar(self.centralwidget)
        self.progressBar_denat.setObjectName(u"progressBar_denat")
        self.progressBar_denat.setGeometry(QRect(40, 570, 421, 23))
        self.progressBar_denat.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: #20B2AA\n"
"}")
        self.progressBar_denat.setValue(24)
        AblaufWindowDenat.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AblaufWindowDenat)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        AblaufWindowDenat.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AblaufWindowDenat)
        self.statusbar.setObjectName(u"statusbar")
        AblaufWindowDenat.setStatusBar(self.statusbar)

        self.retranslateUi(AblaufWindowDenat)

        QMetaObject.connectSlotsByName(AblaufWindowDenat)
    # setupUi

    def retranslateUi(self, AblaufWindowDenat):
        AblaufWindowDenat.setWindowTitle(QCoreApplication.translate("AblaufWindowDenat", u"Denaturierung", None))
        self.textEdit.setHtml(QCoreApplication.translate("AblaufWindowDenat", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#9cd4d6\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Denaturierung beschriebt grunds\u00e4tzlich die strukturelle Ver\u00e4nderung von Biopolymeren.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">"
                        "Es wird das Wasser im ersten Becken auf 95\u00b0C erhitzt. <br />Dies dient dazu das sich die Wasserstoffbr\u00fccken und somit Doppelhelix der DNA aufl\u00f6st dabei entstehen zwei Einzelstr\u00e4nge. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Die Temperatur muss 10 Sekunden bis 1 Minute gehalten werden, um sicherzustelle das jede Doppelhelix zerst\u00f6rt wurde.</span><span style=\" font-family:'Arial Narrow'; font-size:16pt;\"> </span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("AblaufWindowDenat", u"Denaturierung", None))
        self.btn_Kontrolle.setText(QCoreApplication.translate("AblaufWindowDenat", u"Kontrolle", None))
        self.DL_line.setText(QCoreApplication.translate("AblaufWindowDenat", u"Durchlauf:", None))
        self.Dauer_line.setText(QCoreApplication.translate("AblaufWindowDenat", u"Dauer:", None))
        self.Temp_line.setText(QCoreApplication.translate("AblaufWindowDenat", u"Temperatur:", None))
#if QT_CONFIG(tooltip)
        self.progressBar_denat.setToolTip(QCoreApplication.translate("AblaufWindowDenat", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

