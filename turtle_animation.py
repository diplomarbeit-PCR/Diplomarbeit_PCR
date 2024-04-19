import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Werte anzeigen")
        self.setGeometry(100, 100, 400, 200)

        label = QLabel("Hier sind einige Werte:", self)
        label.setGeometry(50, 50, 200, 30)

        value_label = QLabel("123", self)  # Beispielwert
        value_label.setGeometry(250, 50, 100, 30)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
