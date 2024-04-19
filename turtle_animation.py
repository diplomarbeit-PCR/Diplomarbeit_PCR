import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Werte anzeigen")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Hier sind einige Werte:", self)
        self.label.setGeometry(50, 50, 200, 30)

        self.value_label = QLabel("", self)  
        self.value_label.setGeometry(250, 50, 100, 30)

        self.value = 123
        self.update_value_label()

    def update_value_label(self):
        self.value_label.setText(str(self.value))
        font = QFont()
        font.setPointSize(16)  # Hier die gewünschte Schriftgröße einstellen
        self.value_label.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
