import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        # Create a QLineEdit for entering a new dialog title
        self.ledTitle = QLineEdit(self.windowTitle(), self)
        self.ledTitle.setPlaceholderText("Enter a new dialog title")
        self.ledTitle.setEchoMode(QLineEdit.Password)
        self.ledTitle.setAlignment(Qt.AlignCenter)
        self.ledTitle.move(50, 50)

        # Create a QPushButton to trigger title update
        self.btnChange = QPushButton("Update Title", self)
        self.btnChange.move(50, 80)
        self.btnChange.clicked.connect(self.evt_btnChanged_clicked)

        # Connect the textChanged signal to the appropriate slot
        self.ledTitle.textChanged.connect(self.evt_ledTitle_textChanged)

    def evt_ledTitle_textChanged(self, title):
        # Do nothing here, as the title update is handled in evt_btnChanged_clicked
        pass

    def evt_btnChanged_clicked(self):
        # Ask for confirmation before updating the window title
        res = QMessageBox.question(self, "Line Edit", "Are you sure you want to change the window title to '" + self.ledTitle.text() + "'")
        if res == QMessageBox.Yes:
            self.setWindowTitle(self.ledTitle.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
