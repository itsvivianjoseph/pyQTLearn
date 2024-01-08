import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *


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
        validation_result = self.validate_input_fields()

        if validation_result:
            self.accept()
        else:
            QMessageBox.information(self, "Invalid details", "Invalid employee details:\n{}".format(validation_result))

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


# update employee details
class UpdateEmployeeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Update Employee")
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
        validation_result = self.validate_input_fields()

        if validation_result:
            self.accept()
        else:
            QMessageBox.information(self, "Invalid details", "Invalid employee details:\n{}".format(validation_result))

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


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employee Database")
        self.resize(1000, 800)

        print(QSqlDatabase.drivers())

        # create layout
        self.main_layout = QVBoxLayout()
        self.inner_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.button_layout = QVBoxLayout()

        # DB connection
        self.db_connection()

        # setup layout
        self.setup_button_layout()
        self.setup_left_layout()
        self.setup_right_layout()
        self.setup_inner_layout()
        self.setup_main_layout()

        # set up the application layout as the main layout
        self.setLayout(self.main_layout)

    def setup_button_layout(self):
        self.button_add_emp = QPushButton("Add Employee")
        self.button_add_emp.clicked.connect(self.evt_handler_button_add_emp)

        self.button_update_emp = QPushButton("Update Employee")
        self.button_update_emp.clicked.connect(self.evt_handler_button_update_emp)

        self.button_delete_emp = QPushButton("Delete Employee")

        self.button_layout.addWidget(self.button_add_emp)
        self.button_layout.addWidget(self.button_update_emp)
        self.button_layout.addWidget(self.button_delete_emp)

    def evt_handler_button_update_emp(self):
        pass

    def setup_left_layout(self):
        self.list_widget = QListWidget()
        self.left_layout.addWidget(self.list_widget)
        self.left_layout.addLayout(self.button_layout)

    def setup_right_layout(self):
        self.table_emp_details = QTableWidget()
        self.populate_table()
        # Add the QTableWidget to the right_layout
        self.right_layout.addWidget(self.table_emp_details)

    def setup_inner_layout(self):
        self.inner_layout.addLayout(self.left_layout, 20)
        self.inner_layout.addLayout(self.right_layout, 80)

    def setup_main_layout(self):
        self.main_layout.addLayout(self.inner_layout)

    def populate_table(self):
        # create table
        self.table_emp_details.setColumnCount(7)
        self.table_emp_details.setHorizontalHeaderLabels(["ID", "Fname", "Lname", "Email", "Phone", "Position", "Supervisor"])
        self.table_emp_details.setColumnWidth(0, 50)
        self.table_emp_details.setColumnWidth(1, 80)
        self.table_emp_details.setColumnWidth(2, 80)
        self.table_emp_details.setColumnWidth(3, 150)
        self.table_emp_details.setColumnWidth(4, 60)
        self.table_emp_details.setColumnWidth(5, 130)
        self.table_emp_details.setColumnWidth(6, 200)

        # populating the table
        query = QSqlQuery()
        res = query.exec("SELECT * FROM employee")
        if res:
            while query.next():
                row = self.table_emp_details.rowCount()
                self.table_emp_details.insertRow(row)

                for col in range(6):
                    twi = QTableWidgetItem(str(query.value(col)))
                    twi.setTextAlignment(Qt.AlignCenter)
                    self.table_emp_details.setItem(row, col, twi)
                twi = QTableWidgetItem(self.return_emp_name(query.value("emp_id")))
                self.table_emp_details.setItem(row, 6, twi)

                self.list_widget.addItem(self.return_emp_name(query.value("emp_id")))
        else:
            QMessageBox.critical(self, "Database error", "Database error\n\n{}".format(query.lastError().text()))

    def return_emp_name(self, id):
        query = QSqlQuery()
        sql = "SELECT fname,lname,position FROM employee WHERE emp_id = {}".format(int(id))
        res = query.exec(sql)

        if res:
            query.next()
            if query.isValid():
                fname, lname, position = query.value("fname"), query.value("lname"), query.value("position")
                return "{}, {}, {}".format(fname, lname, position)
            else:
                print("Invalid record position")
        else:
            print("Database error: {}".format(query.lastError().text()))
            QMessageBox.critical(self, "Database error", "Database error\n\n{}".format(query.lastError().text()))

        return ""

    def db_connection(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("../data/Employees.db")
        if db.open():
            print("table name:", db.tables())
            if "employee" not in db.tables():
                self.create_table()
        else:
            QMessageBox.critical(self, "Database error", "Couldn't open the Database!!!")

    def create_table(self):
        # Create the employee table if not exists
        sql_create_table = """
            CREATE TABLE IF NOT EXISTS employee (
                emp_id INTEGER PRIMARY KEY,
                fname TEXT NOT NULL,
                lname TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE,
                position TEXT,
                supervisor INTEGER
            )
        """

        # Insert sample data into the employee table
        sql_insert_data = """
            INSERT INTO employee VALUES 
            (101, 'MIKE', 'Smith', 'mike@gmail.com', 'x542', 'CEO', 9999),
            (102, 'JANE', 'Doe', 'jane@gmail.com', 'x543', 'Manager', 101),
            (103, 'JOHN', 'Johnson', 'john@gmail.com', 'x544', 'Developer', 102),
            (104, 'SARA', 'Connor', 'sara@gmail.com', 'x545', 'Engineer', 101),
            (105, 'DAVID', 'Brown', 'david@gmail.com', 'x546', 'Analyst', 102),
            (106, 'ALICE', 'Jones', 'alice@gmail.com', 'x547', 'HR Specialist', 103),
            (107, 'BOB', 'Williams', 'bob@gmail.com', 'x548', 'Marketing Coordinator', 105),
            (108, 'EMMA', 'Davis', 'emma@gmail.com', 'x549', 'Sales Representative', 101),
            (109, 'ERIC', 'Miller', 'eric@gmail.com', 'x550', 'IT Specialist', 103),
            (110, 'OLIVIA', 'Taylor', 'olivia@gmail.com', 'x551', 'Financial Analyst', 105),
            (111, 'LUCAS', 'Anderson', 'lucas@gmail.com', 'x552', 'Project Manager', 102)
        """

        query = QSqlQuery()

        # Execute the CREATE TABLE statement
        if not query.exec(sql_create_table):
            QMessageBox.critical(self, "Database error", "Failed to create the employee table!")

        # Execute the INSERT INTO statement
        if not query.exec(sql_insert_data):
            QMessageBox.critical(self, "Database error", "Failed to insert data into the employee table!")

    def evt_handler_button_add_emp(self):
        add_employee_dialog = AddEmployeeDialog(self)
        result = add_employee_dialog.exec_()

        if result == QDialog.Accepted:
            emp_input_data = add_employee_dialog.get_user_input()

            # Proceed with database insertion
            query = QSqlQuery()

            sql_insert_data = """
                INSERT INTO employee (fname, lname, email, phone, position, supervisor)
                VALUES ('{}', '{}', '{}', '{}', '{}', {})
            """.format(
                emp_input_data['fname'],
                emp_input_data['lname'],
                emp_input_data['email'],
                emp_input_data['phone'],
                emp_input_data['position'],
                emp_input_data['supervisor']
            )

            if query.exec(sql_insert_data):
                QMessageBox.information(self, "Employee added", "Employee details added to the table")
            else:
                QMessageBox.critical(self, "Database error", "Failed to insert data into the employee table!")


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
            border : 1px solid greeen;
        }
    """
    return styles


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgmain = DlgMain()
    dlgmain.show()
    sys.exit(app.exec_())
