# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AblaufWindowAneal_v2.ui'
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

class Ui_AblaufWindowAneal(object):
    def setupUi(self, AblaufWindowAneal):
        if not AblaufWindowAneal.objectName():
            AblaufWindowAneal.setObjectName(u"AblaufWindowAneal")
        AblaufWindowAneal.resize(489, 733)
        self.centralwidget = QWidget(AblaufWindowAneal)
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
        self.temp_sensA = QLCDNumber(self.centralwidget)
        self.temp_sensA.setObjectName(u"temp_sensA")
        self.temp_sensA.setGeometry(QRect(210, 500, 111, 51))
        self.Temp_line = QLineEdit(self.centralwidget)
        self.Temp_line.setObjectName(u"Temp_line")
        self.Temp_line.setGeometry(QRect(210, 460, 111, 31))
        self.Temp_line.setFont(font2)
        self.Temp_line.setAlignment(Qt.AlignCenter)
        self.Temp_line.setReadOnly(True)
        self.progressBar_aneal = QProgressBar(self.centralwidget)
        self.progressBar_aneal.setObjectName(u"progressBar_aneal")
        self.progressBar_aneal.setGeometry(QRect(40, 570, 421, 23))
        self.progressBar_aneal.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: #20B2AA\n"
"}")
        self.progressBar_aneal.setValue(24)
        AblaufWindowAneal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AblaufWindowAneal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        AblaufWindowAneal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AblaufWindowAneal)
        self.statusbar.setObjectName(u"statusbar")
        AblaufWindowAneal.setStatusBar(self.statusbar)

        self.retranslateUi(AblaufWindowAneal)

        QMetaObject.connectSlotsByName(AblaufWindowAneal)
    # setupUi

    def retranslateUi(self, AblaufWindowAneal):
        AblaufWindowAneal.setWindowTitle(QCoreApplication.translate("AblaufWindowAneal", u"Annealing", None))
        self.textEdit.setHtml(QCoreApplication.translate("AblaufWindowAneal", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#9cd4d6\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:16pt;\">Nachdem nur Einzelstr\u00e4nge vorhanden sind, bindet der Primer an diese. Dabei unterscheidet man die Str\u00e4nge in+ Sense -und Anti-sense. Daf\u00fcr gibt es Reversprimer. Der Primer klammert sich an die gew\u00fcnschte Sequenz und die dazwischenliegenden Sequenzen werden Amplikon benannt. Aufgrund des "
                        "Primers betr\u00e4gt die Temperatur 60\u00b0C, da ansonsten der Primer zerst\u00f6rt werden k\u00f6nnte. Diese wird f\u00fcr 30 Sekunden bis 1 Minute gehalten. Ein Strang hat ein 3\u2018 und ein 5\u2018 Anfang. </span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("AblaufWindowAneal", u"Annealing", None))
        self.btn_Kontrolle.setText(QCoreApplication.translate("AblaufWindowAneal", u"Kontrolle", None))
        self.DL_line.setText(QCoreApplication.translate("AblaufWindowAneal", u"Durchlauf:", None))
        self.Dauer_line.setText(QCoreApplication.translate("AblaufWindowAneal", u"Dauer:", None))
        self.Temp_line.setText(QCoreApplication.translate("AblaufWindowAneal", u"Temperatur:", None))
#if QT_CONFIG(tooltip)
        self.progressBar_aneal.setToolTip(QCoreApplication.translate("AblaufWindowAneal", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

