import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()

        # Set up the main dialog window
        self.setWindowTitle("Learn Input Dialog Box")
        self.resize(500, 500)

        # Create three buttons to trigger different input dialogs
        self.btnGetInt = QPushButton("Get Integer", self)
        self.btnGetInt.move(50, 50)
        self.btnGetInt.clicked.connect(self.evt_handler_get_int)

        self.btnGetDouble = QPushButton("Get Double", self)
        self.btnGetDouble.move(200, 50)
        self.btnGetDouble.clicked.connect(self.evt_handler_get_double)

        self.btnGetText = QPushButton("Get Text", self)
        self.btnGetText.move(350, 50)
        self.btnGetText.clicked.connect(self.evt_handler_get_text)

        self.btnGetColors = QPushButton("Get Colors", self)
        self.btnGetColors.move(50, 100)
        self.btnGetColors.clicked.connect(self.evt_handler_get_color)

    # Event handler for the "Get Integer" button
    def evt_handler_get_int(self):
        # (default , min , max , step)
        iValue, bOk = QInputDialog.getInt(self, "Get Integer", "Enter an integer", 0, -100, 100, 1)
        if bOk:
            QMessageBox.information(self, "Integer Value", "You entered: {}".format(iValue))
        else:
            QMessageBox.warning(self, "Canceled", "User canceled input")

    # Event handler for the "Get Double" button
    def evt_handler_get_double(self):
        # (default , min , max , step)
        dValue, bOk = QInputDialog.getDouble(self, "Get Double", "Enter a double", 0.0, -100.0, 100.0, 2)
        if bOk:
            QMessageBox.information(self, "Double Value", "You entered: {}".format(dValue))
        else:
            QMessageBox.warning(self, "Canceled", "User canceled input")

    # Event handler for the "Get Text" button
    def evt_handler_get_text(self):
        # (default , min , max , step)
        sText, bOk = QInputDialog.getText(self, "Get Text", "Enter some text")
        if bOk:
            QMessageBox.information(self, "Text", "You entered: {}".format(sText))
        else:
            QMessageBox.warning(self, "Canceled", "User canceled input")

    # Event handler for the "Get colors" button
    def evt_handler_get_color(self):
        lstColor = ["red", "green", "blue"]
        sColor, bOk = QInputDialog.getItem(self, "Get Colors", "Enter your favorite color", lstColor,editable=False)
        if bOk:
            QMessageBox.information(self, "Color", "Your favorite color is {}".format(sColor))
        else:
            QMessageBox.critical(self, "Canceled", "User canceled")


if __name__ == "__main__":
    # Set up the application and run the main dialog
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())