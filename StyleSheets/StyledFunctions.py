import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QCheckBox, QLineEdit, QVBoxLayout, QListWidget, QMessageBox, QStyleFactory


def set_styles():
    # Define the styles for QPushButton
    button_style = """
        QPushButton {
            background-color: #4CAF50;  /* Green */
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }

        QPushButton:hover {
            background-color: #45a049;  /* Darker Green on Hover */
        }
    """

    return button_style


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        # Widgets
        self.button_one = QPushButton("Button 1")
        self.button_two = QPushButton("Button 2")
        self.button_three = QPushButton("Button 3")

        # styling the buttons
        self.button_one.setStyleSheet(set_styles())
        self.button_two.setStyleSheet(set_styles())
        self.button_three.setStyleSheet(set_styles())

        # Main Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.button_one)
        self.main_layout.addWidget(self.button_two)
        self.main_layout.addWidget(self.button_three)

        # set layout for the application
        self.setLayout(self.main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg_main = MyDialog()
    dlg_main.show()
    sys.exit(app.exec_())
