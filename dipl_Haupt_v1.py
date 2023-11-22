from PySide6.QtWidgets import QApplication, QMainWindow

from dipl_Einfuehrung.einfuehrung_v3 import Ui_StartWindow
from dipl_ import Ui_AblaufWindowDenat

class Frm_denat(QMainWindow, Ui_AblaufWindowDenat):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Frm_main(QMainWindow, Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_Start.clicked.connect(self.denat_Ablauf)

    def denat_Ablauf(self):
        frm_main.hide()
        frm_denat.show()


app = QApplication()
frm_main = Frm_main()
frm_main.show()
frm_denat = Frm_denat()
app.exec()
