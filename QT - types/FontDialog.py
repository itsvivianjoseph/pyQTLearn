import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        self.btn = QPushButton("Choose Font", self)
        self.btn.move(200, 200)
        self.btn.clicked.connect(self.evt_handler)

    def evt_handler(self):
        font, bOk = QFontDialog.getFont()
        print(font, bOk)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())