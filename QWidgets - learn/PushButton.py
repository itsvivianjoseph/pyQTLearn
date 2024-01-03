import sys
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import *


class ImageDisplayGUI(QDialog):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Image Display GUI")
        self.resize(500, 500)

        # Create a button with an icon
        self.toggleButton = QPushButton("Disable", self)
        self.toggleButton.setIcon(QIcon(QPixmap('../photos/vivian.jpeg')))
        self.toggleButton.setFlat(True)
        self.toggleButton.move(200, 200)

        # Create a label for displaying text
        self.displayLabel = QLabel("Text", self)
        self.displayLabel.move(200, 250)
        self.displayLabel.resize(100, 100)

        # Set the font for the label
        font = QFont("Times New Roman", 20, 75, True)
        self.displayLabel.setFont(font)

        # Connect button click event to the event handler method
        self.toggleButton.clicked.connect(self.toggleLabelState)

    def toggleLabelState(self):
        if self.displayLabel.isEnabled():
            # Disable the label and update the button text
            self.displayLabel.setDisabled(True)
            self.displayLabel.repaint()
            self.toggleButton.setText("Enable")
            self.displayLabel.setText("Text")
        else:
            # Enable the label and update the button text
            self.displayLabel.setEnabled(True)
            self.displayLabel.repaint()
            self.toggleButton.setText("Disable")
            self.displayLabel.setText("Text")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    imageDisplayGUI = ImageDisplayGUI()
    imageDisplayGUI.show()
    sys.exit(app.exec_())