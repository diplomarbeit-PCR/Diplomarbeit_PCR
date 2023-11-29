from PySide6.QtWidgets import QApplication, QLabel, QSpinBox, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SpinBox Beispiel")
        self.setGeometry(100, 100, 300, 200)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Wert:")
        spinbox = QSpinBox()
        
        # Setze die Mindest- und Höchstwerte
        spinbox.setRange(10, 60)
        # Setze den Startwert
        spinbox.setValue(10)

        # Verbinde den Wert geändert-Slot
        spinbox.valueChanged.connect(self.onValueChanged)

        layout.addWidget(label)
        layout.addWidget(spinbox)

        self.setLayout(layout)

    def onValueChanged(self, value):
        print(f"Neuer Wert: {value}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
