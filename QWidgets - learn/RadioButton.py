import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()

        # Set up the main dialog window
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        # Create a label to display radio-button selections
        self.label = QLabel("radio-buttons", self)
        self.label.setStyleSheet("color:black; font-size:10px")
        self.label.move(200, 100)

        # Radio buttons for the color group
        self.color_button_group = QButtonGroup()

        self.red_radio_button = QRadioButton("Red", self)
        self.red_radio_button.move(200, 150)
        self.red_radio_button.clicked.connect(self.evt_handler)
        self.color_button_group.addButton(self.red_radio_button)

        self.blue_radio_button = QRadioButton("Blue", self)
        self.blue_radio_button.move(200, 200)
        self.blue_radio_button.clicked.connect(self.evt_handler)
        self.color_button_group.addButton(self.blue_radio_button)

        self.green_radio_button = QRadioButton("Green", self)
        self.green_radio_button.move(200, 250)
        self.green_radio_button.clicked.connect(self.evt_handler)
        self.color_button_group.addButton(self.green_radio_button)

        # Button group for text size
        self.size_button_group = QButtonGroup()

        self.small_button = QRadioButton("Small Text", self)
        self.small_button.move(200, 300)
        self.size_button_group.addButton(self.small_button, 10)
        self.small_button.clicked.connect(self.evt_handler)

        self.medium_button = QRadioButton("Medium Text", self)
        self.medium_button.move(200, 350)
        self.size_button_group.addButton(self.medium_button, 25)
        self.medium_button.clicked.connect(self.evt_handler)

        self.large_button = QRadioButton("Large Text", self)
        self.large_button.move(200, 400)
        self.size_button_group.addButton(self.large_button, 50)
        self.large_button.clicked.connect(self.evt_handler)

    def evt_handler(self):
        # Get the selected color and size
        selected_color_button = self.color_button_group.checkedButton()
        selected_size = self.size_button_group.checkedId()

        # Create a style sheet based on the selected color and size
        style_sheet = "color:" + selected_color_button.text() + "; font-size:" + str(selected_size) + "px"
        print(style_sheet)

        # Apply the style sheet to the label
        self.label.setStyleSheet(style_sheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg_main = DlgMain()
    dlg_main.show()
    sys.exit(app.exec_())