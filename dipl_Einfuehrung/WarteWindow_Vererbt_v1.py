from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QMainWindow
from PySide6.QtCore import QTimer, QRect
from PySide6.QtGui import QColor
import colorsys
import math
import sys

from WarteWindow_v1 import Ui_WarteWindow

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

class Frm_WarteWindow(QMainWindow, Ui_WarteWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WarteWindow()
        self.ui.setupUi(self)

        self.lbl_loading = Animation(self.ui.centralwidget)
        self.lbl_loading.setObjectName(u"lbl_loading")
        self.lbl_loading.setGeometry(QRect(40, 380, 411, 291))


