from PySide6.QtWidgets import QApplication, QMainWindow, QMenu
from PySide6.QtGui import QAction

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        
        # Aktion erstellen
        action = QAction('Open', self)
        action.triggered.connect(self.open_file)  # Verbinde mit der Methode, die ausgeführt werden soll
        file_menu.addAction(action)
        
    def open_file(self):
        # Hier kann die Logik für das Öffnen einer Datei stehen
        print("Opening file...")

app = QApplication([])
window = MyWindow()
window.show()
app.exec()
