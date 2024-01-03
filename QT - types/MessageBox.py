import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        # Create a button
        self.btn = QPushButton("Show Message", self)
        self.btn.move(200, 200)

        # Connect the button's click event to the event handler
        self.btn.clicked.connect(self.evt_handler)

    def evt_handler(self):
        # Show a message box when the button is clicked

        # type 1 - static methods
        # res = QMessageBox.information(self, "Disk Full", "Your disk drive is almost full!")
        # # res = QMessageBox.warning(self, "Disk Full", "Your disk drive is almost full!")
        # # res = QMessageBox.critical(self, "Disk Full", "Your disk drive is almost full!")
        # # res = QMessageBox.question(self, "Disk Full", "Your disk drive is almost full!")
        #
        # if QMessageBox.Yes:
        #     QMessageBox.information(self,"chosen option","Yes")
        # else:
        #     res = QMessageBox.information(self,"chosen option","No")
        # print(res)

        # type 2
        msg_disk_full = QMessageBox()
        msg_disk_full.setText("your hard drive is almost full")
        msg_disk_full.setDetailedText("Please make space available else system perfomace will be degraded")
        msg_disk_full.setIcon(QMessageBox.Information)
        msg_disk_full.setWindowTitle("Drive Full")
        msg_disk_full.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg_disk_full.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()

    # Show the main dialog
    dlgMain.show()

    # Execute the application
    sys.exit(app.exec_())