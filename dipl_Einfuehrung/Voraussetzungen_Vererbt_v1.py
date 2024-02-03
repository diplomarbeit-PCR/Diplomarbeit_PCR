from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_Voraussetzung(object):
    def setupUi(self, Voraussetzung):
        if not Voraussetzung.objectName():
            Voraussetzung.setObjectName(u"Voraussetzung")
        Voraussetzung.resize(489, 733)
        self.centralwidget = QWidget(Voraussetzung)
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
        font.setPointSize(35)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.Voraus_lbl = QLabel(self.centralwidget)
        self.Voraus_lbl.setObjectName(u"Voraus_lbl")
        self.Voraus_lbl.setGeometry(QRect(20, 370, 451, 301))
        self.Voraus_lbl.setPixmap(QPixmap(r"C:\Daten_Amelie\DA\App\GitHub\Diplomarbeit_PCR\dipl_Einfuehrung\pcrGrundprinzip.png"))
        self.Voraus_lbl.setScaledContents(True)
        Voraussetzung.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Voraussetzung)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        Voraussetzung.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Voraussetzung)
        self.statusbar.setObjectName(u"statusbar")
        Voraussetzung.setStatusBar(self.statusbar)

        self.retranslateUi(Voraussetzung)

        QMetaObject.connectSlotsByName(Voraussetzung)
    # setupUi

    def retranslateUi(self, Voraussetzung):
        Voraussetzung.setWindowTitle(QCoreApplication.translate("Voraussetzung", u"Voraussetzungen", None))
        self.textEdit.setHtml(QCoreApplication.translate("Voraussetzung", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#9cd4d6\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Es muss die DNA-Sequenz des suchenden Strangs wie die Probe vorliegen. Um mit dem Prozess zu beginnen werden sogenannte Primer und Enzyme ben\u00f6tigt. <br />Ein Primer gibt den Beginn der Polymerase an. Durch diesen werden unterschiedliche DNA-Abschnitte repliziert. <br />Enzyme induzieren die Reaktionen und red"
                        "uzieren die Aktivierungsenergie. </span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Voraussetzung", u"Voraussetzungen", None))
        self.Voraus_lbl.setText("")
    # retranslateUi



# Es wird eine Klasse für die Voraussetzungen erstellt
# Hierfür wird deklariert, dass ein MainWindow verwendet wurde und es auf die Klasse Ui_Voraussetzung
class Frm_voraus(QMainWindow, Ui_Voraussetzung):
    def __init__(self):
        super().__init__()
        self.setupUi(self)