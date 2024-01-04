import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        
        self.ted = QPlainTextEdit("hello world!!!")
        
        self.layout_main = QVBoxLayout()
        self.layout_main.addWidget(self.ted)

        self.setLayout(self.layout_main)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgmain = DlgMain()
    dlgmain.show()
    sys.exit(dlgmain.exec_())