from PySide6.QtWidgets import QApplication, QLCDNumber, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.timer_seconds = 0

        self.timer_lcd = QLCDNumber()
        self.timer_lcd.setDigitCount(8)  # 8 Ziffern für "hh:mm:ss"
        self.timer_lcd.display("00:00:00")

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.timer_lcd)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)

        self.setLayout(self.layout)

    def start_timer(self):
        self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()

    def update_timer(self):
        self.timer_seconds += 1
        hours = self.timer_seconds // 3600
        minutes = (self.timer_seconds % 3600) // 60
        seconds = self.timer_seconds % 60

        time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        self.timer_lcd.display(time_str)

if __name__ == "__main__":
    app = QApplication([])
    window = TimerApp()
    window.show()
    app.exec()
