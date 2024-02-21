
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QMainWindow
from PySide6.QtCore import QTimer, QRect
from PySide6.QtGui import QColor
import colorsys
import math
import sys

from WarteWindow_v1 import Ui_WarteWindow, Animation

class Frm_WarteWindow(QMainWindow, Ui_WarteWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WarteWindow()
        self.ui.setupUi(self)

        self.lbl_loading = Animation(self.ui.centralwidget)
        self.lbl_loading.setObjectName(u"lbl_loading")
        self.lbl_loading.setGeometry(QRect(40, 380, 411, 291))




