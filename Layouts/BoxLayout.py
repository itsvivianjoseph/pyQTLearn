import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        # create widgets
        self.label = QLabel("First Label")
        self.button = QPushButton("Second Button")
        self.lineedit = QLineEdit("Third Line Edit")
        self.combobox = QComboBox()
        self.combobox.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])

        # setup layouts
        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.label, alignment=Qt.AlignCenter)  # Set alignment to center
        self.mainlayout.addWidget(self.button)
        self.mainlayout.addWidget(self.lineedit)
        self.mainlayout.addWidget(self.combobox)

        self.setLayout(self.mainlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgmain = DlgMain()
    dlgmain.show()
    sys.exit(app.exec_())
