# https://commons.wikimedia.org/w/index.php?search=Loading+animations&title=Special:MediaSearch&type=image

# https://prod.liveshare.vsengsaas.visualstudio.com/join?A8A30C45399B67793C7C489967D379206946
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from dipl_Einfuehrung.WarteWindow_v1 import Ui_WarteWindow  

class WarteWindow(QMainWindow, Ui_WarteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Zentrieren des Labels
        self.lbl_loading.setAlignment(Qt.AlignCenter)

        # Größe des Labels ändern
        self.lbl_loading.setFixedSize(400, 400)  # Ändern Sie die Größe nach Bedarf


        self.movie = QMovie(r"C:\Daten_Amelie\DA\App\GitHub\Diplomarbeit_PCR\dipl_Einfuehrung\loading_cyan.gif")
        self.lbl_loading.setMovie(self.movie)

        timer = QTimer(self)
        timer.timeout.connect(self.startAnimation)
        timer.start(1000)  # Startet die Animation alle 1000 Millisekunden

    def startAnimation(self):
        self.movie.start()


if __name__ == "__main__":
    app = QApplication([])
    frm_warte = WarteWindow()  # Instanz der WarteWindow-Klasse erstellen
    frm_warte.show()  # Das Hauptfenster anzeigen
    app.exec()  # Starten der Ereignisschleife
