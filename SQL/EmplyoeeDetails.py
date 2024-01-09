import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from AddEmployeeDetails import AddEmployeeDialog
from UpdateEmployeeDetails import UpdateEmployeeDialog


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
        self.button_delete_emp.clicked.connect(self.evt_handler_button_delete_emp)

        self.button_layout.addWidget(self.button_add_emp)
        self.button_layout.addWidget(self.button_update_emp)
        self.button_layout.addWidget(self.button_delete_emp)

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
        # Clear the list widget
        self.list_widget.clear()

        # create table
        self.table_emp_details.setColumnCount(7)
        self.table_emp_details.setHorizontalHeaderLabels(
            ["ID", "Fname", "Lname", "Email", "Phone", "Position", "Supervisor"])
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

                # Clear the current table
                self.table_emp_details.setRowCount(0)

                # Repopulate the table
                self.populate_table()

            else:
                QMessageBox.critical(self, "Database error", "Failed to insert data into the employee table!")

    def evt_handler_button_update_emp(self):
        emp_id, ok = QInputDialog.getInt(self, 'Update Employee', 'Enter Employee ID:')
        if ok:
            update_dialog = UpdateEmployeeDialog(self, emp_id)

            if update_dialog.exec_() == QDialog.Accepted:
                user_input = update_dialog.get_user_input()

                print("User Input:", user_input)

                query = QSqlQuery()

                sql = """
                            UPDATE employee
                            SET fname = '{fname}',
                                lname = '{lname}',
                                email = '{email}',
                                phone = '{phone}',
                                position = '{position}',
                                supervisor = '{supervisor}'
                            WHERE emp_id = {emp_id}
                        """.format(
                    fname=user_input["fname"],
                    lname=user_input["lname"],
                    email=user_input["email"],
                    phone=user_input["phone"],
                    position=user_input["position"],
                    supervisor=user_input["supervisor"],
                    emp_id=user_input["emp_id"]
                )

                if query.exec_(sql):
                    print("Employee updated successfully!")

                    # Clear the current table
                    self.table_emp_details.setRowCount(0)

                    # Repopulate the table
                    self.populate_table()

                else:
                    print("Error updating employee:", query.lastError().text())
        else:
            return None

    def evt_handler_button_delete_emp(self):
        emp_id, ok = QInputDialog.getInt(self, 'Delete Employee', 'Enter Employee ID:')
        if ok:
            # Delete the employee record
            query_delete = QSqlQuery()
            sql_delete = "DELETE FROM employee WHERE emp_id = :emp_id"
            query_delete.prepare(sql_delete)
            query_delete.bindValue(":emp_id", emp_id)

            if not query_delete.exec_():
                QMessageBox.critical(self, "Database error","Query wasn't successful \n{}".format(query_delete.lastError()))
                return

            print("{} Employee's record has been deleted!!!".format(emp_id))

            # Clear the current table
            self.table_emp_details.setRowCount(0)

            # Repopulate the table
            self.populate_table()
        else:
            QMessageBox.information(self,"Error occurred","Some error has occurred retry!!!")

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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgmain = DlgMain()
    dlgmain.show()
    sys.exit(app.exec_())
