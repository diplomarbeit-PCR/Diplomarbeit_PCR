from PySide6.QtWidgets import QApplication, QMainWindow

from dipl_Einfuehrung.einfuehrung_v3 import Ui_StartWindow
from dipl_Ablauf_Denat.AblaufWindowDenat_v1 import Ui_AblaufWindowDenat

class Frm_main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication()
frm_main = Frm_main()
frm_main.show()
app.exec()
