from PyQt5.QtWidgets import *


# add new employee class
class AddEmployeeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Employee")
        self.resize(300, 200)

        # define layout type
        self.layout = QVBoxLayout()

        # create widgets
        self.create_widgets()

        # add widgets to the layout
        self.add_widgets()

        # validation
        self.fname_edit.textChanged.connect(self.validate_first_name)
        self.lname_edit.textChanged.connect(self.validate_last_name)
        self.email_edit.textChanged.connect(self.validate_email)

        # event handlers
        self.add_button.clicked.connect(self.validate_and_accept)

        # set layout
        self.setLayout(self.layout)

    def validate_and_accept(self):
        error = self.validate_input_fields()

        if error is None:
            self.accept()
        else:
            QMessageBox.information(self, "Invalid details", "Invalid employee details:\n{}".format(error))

    def validate_first_name(self):
        self.fname_edit.setStyleSheet("")
        if len(self.fname_edit.text()) < 2:
            self.fname_edit.setStyleSheet(style_line_edit_error())
        else:
            self.fname_edit.setStyleSheet(style_line_edit_correct())

    def validate_last_name(self):
        self.lname_edit.setStyleSheet("")
        if len(self.lname_edit.text()) < 2:
            self.lname_edit.setStyleSheet(style_line_edit_error())
        else:
            self.lname_edit.setStyleSheet(style_line_edit_correct())

    def validate_email(self):
        self.email_edit.setStyleSheet("")
        if self.email_edit.text().find('@') < 1 or self.email_edit.text().find('.') < 3:
            self.email_edit.setStyleSheet(style_line_edit_error())
        else:
            self.email_edit.setStyleSheet(style_line_edit_correct())

    def validate_input_fields(self):
        errors = ""

        # Validate first name
        if len(self.fname_edit.text()) < 2:
            errors += "\n First name has to be at least two characters"

        # Validate last name
        if len(self.lname_edit.text()) < 2:
            errors += "\n Last name has to be at least two characters"

        # Validate email
        if self.email_edit.text().find('@') < 1:
            errors += "\n Invalid Email"

        if self.email_edit.text().find('.') < 3:
            errors += "\n Email ID shouldn't contain any periods"

        # Validate phone
        if not self.phone_edit.text():
            errors += "\n Phone number field not mentioned"

        # Validate position
        if not self.position_edit.text():
            errors += "\n Position field not mentioned"

        # Validate supervisor
        if not self.supervisor_edit.text():
            errors += "\n Supervisor field not mentioned"

        if errors:
            errors = "Please correct the below errors:\n" + errors
            print(errors)
            return errors

        # Return None if there are no errors
        return None

    def add_widgets(self):
        self.layout.addWidget(self.fname_label)
        self.layout.addWidget(self.fname_edit)
        self.layout.addWidget(self.lname_label)
        self.layout.addWidget(self.lname_edit)
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_edit)
        self.layout.addWidget(self.phone_label)
        self.layout.addWidget(self.phone_edit)
        self.layout.addWidget(self.position_label)
        self.layout.addWidget(self.position_edit)
        self.layout.addWidget(self.supervisor_label)
        self.layout.addWidget(self.supervisor_edit)
        self.layout.addWidget(self.add_button)

    def get_user_input(self):
        return {
            "fname": self.fname_edit.text(),
            "lname": self.lname_edit.text(),
            "email": self.email_edit.text(),
            "phone": self.phone_edit.text(),
            "position": self.position_edit.text(),
            "supervisor": self.supervisor_edit.text()
        }

    def create_widgets(self):
        # first name label
        self.fname_label = QLabel("First Name:")
        self.fname_edit = QLineEdit()

        # last name label
        self.lname_label = QLabel("Last Name:")
        self.lname_edit = QLineEdit()

        # email label
        self.email_label = QLabel("Email:")
        self.email_edit = QLineEdit()

        # phone label
        self.phone_label = QLabel("Phone:")
        self.phone_edit = QLineEdit()

        # position label
        self.position_label = QLabel("Position:")
        self.position_edit = QLineEdit()

        # supervisor label
        self.supervisor_label = QLabel("Supervisor ID:")
        self.supervisor_edit = QLineEdit()

        # submit button
        self.add_button = QPushButton("submit")


def style_line_edit_error():
    styles = """
        QLineEdit {
            border : 1px solid red;
        }
    """
    return styles

def style_line_edit_correct():
    styles = """
        QLineEdit {
            border : 1px solid green;
        }
    """
    return styles
