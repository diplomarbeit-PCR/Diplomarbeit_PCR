from PySide6.QtWidgets import QApplication, QMainWindow, QLCDNumber, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QTimer

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.centralWidget())

        # Erstelle drei QLCDNumber-Widgets
        self.lcd_numbers = [QLCDNumber() for _ in range(3)]
        for lcd_number in self.lcd_numbers:
            lcd_number.setDigitCount(3)
            layout.addWidget(lcd_number)

        # Setze den Wert der Bedingung
        self.condition_value = 50

        # Setze den Timer für die Aktualisierung
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_lcd_colors)
        self.timer.start(1000)  # Aktualisiere alle 1000 Millisekunden (1 Sekunde)

    def update_lcd_colors(self):
        # Überprüfe die Bedingung
        condition_fulfilled = self.check_condition()

        # Aktualisiere die Farben der LCD-Widgets basierend auf der Bedingung
        for lcd_number in self.lcd_numbers:
            palette = lcd_number.palette()
            if condition_fulfilled:
                palette.setColor(palette.Text, Qt.green)
                palette.setColor(palette.Window, Qt.black)
            else:
                palette.setColor(palette.Text, Qt.red)
                palette.setColor(palette.Window, Qt.black)
            lcd_number.setPalette(palette)

    def check_condition(self):
        # Hier wird deine Bedingung überprüft
        # Beispiel: Wenn der Wert eines der LCD-Widgets größer als die Bedingung ist, gib True zurück
        for lcd_number in self.lcd_numbers:
            if lcd_number.intValue() > self.condition_value:
                return True
        return False

if __name__ == "__main__":
    app = QApplication([])
    window = MyWidget()
    window.show()
    app.exec()
