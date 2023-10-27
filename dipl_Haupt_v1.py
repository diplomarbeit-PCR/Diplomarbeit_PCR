from PySide6.QtWidgets import QApplication, QMainWindow

from dipl_Einfuehrung.einfuehrung_v1 import Ui_MainWindow

class Frm_main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication()
frm_main = Frm_main()
frm_main.show()
app.exec()

