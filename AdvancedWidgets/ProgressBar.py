import sys, time
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        self.progress = QProgressBar()

        self.button = QPushButton("Start")
        self.button.clicked.connect(self.evt_handler)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.progress)
        self.main_layout.addWidget(self.button)

        self.setLayout(self.main_layout)

    def evt_handler(self):
        for i in range(100):
            time.sleep(0.1)
            self.progress.setValue(i)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgmain = DlgMain()
    dlgmain.show()
    sys.exit(dlgmain.exec_())