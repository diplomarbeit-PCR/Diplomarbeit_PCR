from PySide6.QtCore import QTimer, Qt, QRect
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PySide6.QtGui import QPainter, QColor, QBrush
import sys
import colorsys
from dipl_Einfuehrung.WarteWindow_v1 import Ui_WarteWindow

class AnimatedLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.colors = []
        self.angle = 0
        self.radius = 100
        self.increasing = True
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)
        self.timer.start(30)  # 30ms Timer für die Aktualisierung

    def updateAnimation(self):
        if self.increasing:
            self.radius -= 1
        else:
            self.radius += 1

        if self.radius <= 10:
            self.increasing = False
        elif self.radius >= 100:
            self.increasing = True

        self.angle += 1
        if self.angle >= 360:
            self.angle = 0

        color = QColor.fromHsv(self.angle, 255, 255)
        self.colors.append((color, self.radius))
        if len(self.colors) > 200:
            self.colors.pop(0)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white)
        painter.setRenderHint(QPainter.Antialiasing)

        # Mittelpunkt des Widgets
        center_x = self.width() // 2
        center_y = self.height() // 2

        for color, radius in self.colors:
            brush = QBrush(color)
            painter.setBrush(brush)
            painter.drawEllipse(center_x - radius, center_y - radius, radius * 2, radius * 2)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WarteWindow()
        self.ui.setupUi(self)

        self.label = AnimatedLabel(self.ui.centralwidget)
        self.label.setGeometry(QRect(90, 410, 311, 231))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setGeometry(100, 100, 400, 400)
    mainWindow.show()
    sys.exit(app.exec())
