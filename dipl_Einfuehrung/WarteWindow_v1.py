# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WarteWindow_v1.ui'
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
    QSizePolicy, QStatusBar, QTextEdit, QWidget)
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QMainWindow
from PySide6.QtCore import QTimer, QRect
from PySide6.QtGui import QColor
import colorsys
import math
import sys



class Animation(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Loading Animation Example")

        # Set up the scene
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        # Rand            links, oben, rechts, unten
        self.setSceneRect(-150, -140, 300, 280)


        # Initialize parameters
        self.angle = 0
        self.circle_radius = 100
        self.pen_width = 50
        self.hue = 0

        # Create timer for animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)
        self.timer.start(10)  # Update every 10 milliseconds

    def updateAnimation(self):
        # Calculate the next position of the circle
        self.angle += 1
        if self.angle >= 360:
            self.angle = 0
        rad_angle = math.radians(self.angle)
        x = self.circle_radius * math.cos(rad_angle)
        y = self.circle_radius * math.sin(rad_angle)

        # Update hue for color
        self.hue += 1
        if self.hue >= 360:
            self.hue = 0

        # Draw the circle at the current position
        brush_color = QColor.fromHsv(self.hue, 255, 255)
        pen_color = QColor.fromHsv(self.hue, 255, 255)
        pen = self.scene.addEllipse(x - self.pen_width / 2, y - self.pen_width / 2, self.pen_width, self.pen_width, pen_color, brush_color)
        pen.setTransformOriginPoint(x, y)
        pen.setRotation(self.angle)

class Ui_WarteWindow(object):
    def setupUi(self, WarteWindow):
        if not WarteWindow.objectName():
            WarteWindow.setObjectName(u"WarteWindow")
        WarteWindow.resize(489, 733)
        self.centralwidget = QWidget(WarteWindow)
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
        self.lbl_loading = QLabel(self.centralwidget)
        self.lbl_loading.setObjectName(u"lbl_loading")
        self.lbl_loading.setGeometry(QRect(40, 380, 411, 291))
        WarteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(WarteWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        WarteWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(WarteWindow)
        self.statusbar.setObjectName(u"statusbar")
        WarteWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WarteWindow)

        QMetaObject.connectSlotsByName(WarteWindow)
    # setupUi

    def retranslateUi(self, WarteWindow):
        WarteWindow.setWindowTitle(QCoreApplication.translate("WarteWindow", u"WarteWindow", None))
        self.textEdit.setHtml(QCoreApplication.translate("WarteWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#9cd4d6\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Es muss die DNA-Sequenz des suchenden Strangs Wir bitten um Ihre Geduld.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Es werden die personalisierten Daten "
                        "verarbeitet und \u00fcbermittelt.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; font-size:16pt;\">Bitte gehen Sie w\u00e4hrenddessen sicher, dass die Probe eingef\u00fchrt ist und, dass sich der Bewegmechanismus in seiner zgewiesenen Nullposition befindet.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("WarteWindow", u"Warte Window", None))
        self.lbl_loading.setText("")
    # retranslateUi

