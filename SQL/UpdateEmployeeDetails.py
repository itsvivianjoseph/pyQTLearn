from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


class UpdateEmployeeDialog(QDialog):
    def __init__(self, parent=None, emp_id=None):
        try:
            super().__init__(parent)
            self.setWindowTitle("Update Employee")
            self.resize(300, 200)

            self.main_layout = QVBoxLayout()

            # Get selected employee ID
            self.emp_id = int(emp_id)

            # Create widgets
            self.create_widgets()

            # Check if the employee ID is valid
            if self.emp_id is not None:
                # Retrieve employee data from the database
                emp_data = self.retrieve_emp_data_from_database(self.emp_id)
                print(emp_data)

                # Add widgets to the layout
                self.add_widgets(emp_data)

            # Connect signals to slots
            self.fname_edit.textChanged.connect(self.validate_first_name)
            self.lname_edit.textChanged.connect(self.validate_last_name)
            self.email_edit.textChanged.connect(self.validate_email)
            self.phone_edit.textChanged.connect(self.validate_phone)

            # validate and accept the updated data
            self.submit_button.clicked.connect(self.validate_and_accept)

            # Set the layout
            self.setLayout(self.main_layout)

        except Exception as e:
            print("Exception:", e)
            import traceback
            traceback.print_exc()

    def create_widgets(self):
        # Create widgets for all fields
        self.fname_label = QLabel("First Name:")
        self.fname_edit = QLineEdit()

        self.lname_label = QLabel("Last Name:")
        self.lname_edit = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_edit = QLineEdit()

        self.phone_label = QLabel("Phone Number:")
        self.phone_edit = QLineEdit()

        self.position_label = QLabel("Position:")
        self.position_edit = QLineEdit()

        self.supervisor_label = QLabel("Supervisor:")
        self.supervisor_edit = QLineEdit()

        self.submit_button = QPushButton("Submit")

    def add_widgets(self,emp_data):
        # Set employee data to the fields
        self.set_emp_data_to_fields(emp_data)

        # Add widgets to the layout
        self.main_layout.addWidget(self.fname_label)
        self.main_layout.addWidget(self.fname_edit)

        self.main_layout.addWidget(self.lname_label)
        self.main_layout.addWidget(self.lname_edit)

        self.main_layout.addWidget(self.email_label)
        self.main_layout.addWidget(self.email_edit)

        self.main_layout.addWidget(self.phone_label)
        self.main_layout.addWidget(self.phone_edit)

        self.main_layout.addWidget(self.position_label)
        self.main_layout.addWidget(self.position_edit)

        self.main_layout.addWidget(self.supervisor_label)
        self.main_layout.addWidget(self.supervisor_edit)

        self.main_layout.addWidget(self.submit_button)

    def retrieve_emp_data_from_database(self, emp_id):
        query = QSqlQuery()
        sql = "SELECT * FROM employee WHERE emp_id = {}".format(emp_id)
        res = query.exec(sql)

        if res:
            query.next()
            if query.isValid():
                emp_data = {
                    "fname": query.value("fname"),
                    "lname": query.value("lname"),
                    "email": query.value("email"),
                    "phone_number": query.value("phone"),
                    "position": query.value("position"),
                    "supervisor": int(query.value("supervisor"))
                }
                return emp_data
            else:
                print("Invalid record position")
        else:
            print("Database error: {}".format(query.lastError().text()))
            QMessageBox.critical(self, "Database error", "Database error\n\n{}".format(query.lastError().text()))

        return None

    def set_emp_data_to_fields(self, emp_data):
        if emp_data:
            print("hello")
            self.fname_edit.setText(emp_data.get("fname", ""))
            self.lname_edit.setText(emp_data.get("lname", ""))
            self.email_edit.setText(emp_data.get("email", ""))
            self.phone_edit.setText(emp_data.get("phone_number", ""))
            self.position_edit.setText(emp_data.get("position", ""))

            # Convert the supervisor value to string before setting it
            supervisor_value = str(emp_data.get("supervisor", ""))
            self.supervisor_edit.setText(supervisor_value)

        else:
            print("No data retrieved for the employee.")

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

    def validate_phone(self):
        self.phone_edit.setStyleSheet("")
        if not self.phone_edit.text():
            self.phone_edit.setStyleSheet(style_line_edit_error())
        else:
            self.phone_edit.setStyleSheet(style_line_edit_correct())

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
            errors = "Please correct the below errors:" + errors
            return errors

        # Return None if there are no errors
        return None

    def get_user_input(self):
        return {
            "emp_id": self.emp_id,
            "fname": self.fname_edit.text(),
            "lname": self.lname_edit.text(),
            "email": self.email_edit.text(),
            "phone": self.phone_edit.text(),
            "position": self.position_edit.text(),
            "supervisor": self.supervisor_edit.text()
        }


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
