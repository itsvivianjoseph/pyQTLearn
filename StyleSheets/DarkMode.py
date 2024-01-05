import sys
from PyQt5.QtWidgets import *
import qdarkstyle


class DarkStyleDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dark Style Demo")

        # Group box to contain dark style options
        self.gbxDarkStyle = QGroupBox("Dark style")
        self.gbxDarkStyle.setCheckable(True)

        # Radio buttons for style selection
        self.optNormal = QRadioButton("Normal")
        self.optNormal.setChecked(True)
        self.optNormal.toggled.connect(self.toggle_dark_style)
        self.optNormal.setStyleSheet(style_radio_button(dark=False))  # Apply initial style

        self.optDark = QRadioButton("Dark style")
        self.optDark.setStyleSheet(style_radio_button(dark=False))  # Apply initial style

        # Plain text edit to display style information
        self.txtStyle = QPlainTextEdit()

        # Layouts for organizing widgets
        self.lytBtns = QVBoxLayout()
        self.lytBtns.addWidget(self.optNormal)
        self.lytBtns.addWidget(self.optDark)

        self.lytGBox = QHBoxLayout()
        self.lytGBox.addLayout(self.lytBtns)
        self.lytGBox.addWidget(self.txtStyle)

        self.gbxDarkStyle.setLayout(self.lytGBox)

        self.lytMain = QHBoxLayout()
        self.lytMain.addWidget(self.gbxDarkStyle)

        self.setLayout(self.lytMain)

    def toggle_dark_style(self, check):
        if check:
            app.setStyleSheet("")  # Apply normal style
            self.dark = False
        else:
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())  # Apply dark style
            self.dark = True

        self.txtStyle.setPlainText(app.styleSheet())
        self.optNormal.setStyleSheet(style_radio_button(self.dark))  # Update radio button style
        self.optDark.setStyleSheet(style_radio_button(self.dark))  # Update radio button style

def style_radio_button(dark=False):
    if dark:
        sStyle = """
            QRadioButton {
                background-color: #323232;
                color: #b8b8b8;
                border: 1px solid #555555;
                border-radius: 2px;
                padding: 5px;
            }
            QRadioButton::indicator {
               background-color: #323232;
               color: #b8b8b8; 
               border: 1px solid #555555;
               border-radius: 6px;
            }
        """
    else:
        sStyle = """
            QRadioButton {
                background-color: #ffffff;
                color: #333333;
                border: 1px solid #cccccc;
                border-radius: 2px;
                padding: 5px;
            }
            QRadioButton::indicator {
               background-color: #ffffff;
               color: #333333; 
               border: 1px solid #cccccc;
               border-radius: 6px;
            }
        """

    return sStyle


if __name__ == "__main__":
    app = QApplication(sys.argv)
    darkStyleDialog = DarkStyleDialog()
    darkStyleDialog.show()
    sys.exit(app.exec_())
