import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFormLayout, QLineEdit, QDateTimeEdit, QSpinBox, QPushButton
from PyQt5.QtCore import Qt


class MainForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        # Create widgets
        self.line_edit_first_name = QLineEdit("Joe")
        self.line_edit_last_name = QLineEdit("Smith")
        self.datetime_started = QDateTimeEdit()
        self.spin_box_age = QSpinBox()
        self.button_submit = QPushButton("Submit")

        # Setup layout
        self.main_layout = QFormLayout()
        self.main_layout.setLabelAlignment(Qt.AlignLeft)
        self.main_layout.addRow("First Name:", self.line_edit_first_name)
        self.main_layout.addRow("Last Name:", self.line_edit_last_name)
        self.main_layout.addRow("Date Started:", self.datetime_started)
        self.main_layout.addRow("Age:", self.spin_box_age)
        self.main_layout.addRow("", self.button_submit)

        self.setLayout(self.main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())
