import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome GUI")
        self.resize(500, 500)

        self.button_one = QPushButton("Button 1")
        self.button_two = QPushButton("Button 2")
        self.button_three = QPushButton("Button 3")

        # Apply awesome styling to buttons
        self.apply_styling()

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.button_one)
        self.main_layout.addWidget(self.button_two)
        self.main_layout.addWidget(self.button_three)

        self.setLayout(self.main_layout)

    def apply_styling(self):
        # Styling for button_one
        self.button_one.setStyleSheet(
            """
            background-color: #3498db;
            border: 2px solid #2980b9;
            color: white;
            border-radius: 5px;
            padding: 5px;
            """
        )

        # Styling for button_two
        self.button_two.setStyleSheet(
            """
            background-color: #2ecc71;
            border: 2px solid #27ae60;
            color: white;
            border-radius: 5px;
            padding: 5px;
            """
        )

        # Styling for button_three
        self.button_three.setStyleSheet(
            """
            background-color: #e74c3c;
            border: 2px solid #c0392b;
            color: white;
            border-radius: 5px;
            padding: 5px;
            """
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgmain = DlgMain()
    dlgmain.show()
    sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
#
# class DlgMain(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My Awesome GUI")
#         self.resize(500, 500)
#
#         self.button_one = QPushButton("Button 1")
#         self.button_two = QPushButton("Button 2")
#         self.button_three = QPushButton("Button 3")
#
#         # Apply awesome styling and effects to buttons
#         self.apply_styling()
#
#         self.main_layout = QVBoxLayout()
#         self.main_layout.addWidget(self.button_one)
#         self.main_layout.addWidget(self.button_two)
#         self.main_layout.addWidget(self.button_three)
#
#         self.setLayout(self.main_layout)
#
#     def apply_styling(self):
#         # Styling for buttons
#         style = """
#             QPushButton {
#                 background-color: #3498db;
#                 border: 2px solid #2980b9;
#                 color: white;
#                 border-radius: 5px;
#                 padding: 5px;
#             }
#
#             QPushButton:hover {
#                 background-color: #2c3e50;
#             }
#
#             QPushButton:pressed {
#                 background-color: #34495e;
#             }
#         """
#
#         # Apply style to all buttons
#         self.button_one.setStyleSheet(style)
#         self.button_two.setStyleSheet(style)
#         self.button_three.setStyleSheet(style)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dlgmain = DlgMain()
#     dlgmain.show()
#     sys.exit(app.exec_())