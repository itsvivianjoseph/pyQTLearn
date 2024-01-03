import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500,500)

        self.btn = QPushButton("choose colors",self)
        self.btn.move(200,200)
        self.btn.clicked.connect(self.evt_handler)

    def evt_handler(self):
        color = QColorDialog.getColor(QColor(0,255,0),self,"choose color")
        print(color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(dlgMain.exec_())