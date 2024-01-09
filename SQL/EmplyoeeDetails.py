import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from AddEmployeeDetails import AddEmployeeDialog
from UpdateEmployeeDetails import UpdateEmployeeDialog


class DlgMain(QDialog):
    # attributes
    employee_data = []

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
        self.setup_main_layout()
        self.setup_right_layout()
        self.setup_inner_layout()

        # synchronize the current item selected on table widget and list widget
        self.list_widget.currentItemChanged.connect(self.on_list_widget_item_changed)

        # set up the application layout as the main layout
        self.setLayout(self.main_layout)

    def on_list_widget_item_changed(self, current_item, previous_item):
        if current_item:
            index = self.list_widget.row(current_item)

            if 0 <= index < self.table_emp_details.rowCount():
                # Select the corresponding row in the table
                self.table_emp_details.selectRow(index)

                # Get the supervisor ID of the selected employee
                emp_data = self.employee_data[index]
                supervisor_id = emp_data["supervisor"]

                # Find the corresponding item in the tree_widget based on supervisor ID
                tree_items = self.tree_widget.findItems(str(supervisor_id), Qt.MatchRecursive, 0)
                if tree_items:
                    self.tree_widget.setCurrentItem(tree_items[0])

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
        # employee table setup
        self.table_emp_details = QTableWidget()
        # Populate the table and tree after setting them up
        self.populate_table()

        # employee supervisor tree-setup
        self.tree_widget = QTreeWidget()
        # Set the header labels for the columns
        self.tree_widget.setHeaderLabels(["ID", "Name", "Phone", "Email", "Position", "Supervisor"])
        # insert into tree
        self.populate_tree()


        # Add the QTableWidget to the right layout
        self.right_layout.addWidget(self.table_emp_details)
        # Add the QTreeWidget to the right layout
        self.right_layout.addWidget(self.tree_widget)


    def setup_inner_layout(self):
        self.inner_layout.addLayout(self.left_layout, 20)
        self.inner_layout.addLayout(self.right_layout, 80)

    def setup_main_layout(self):
        self.main_layout.addLayout(self.inner_layout)

    def table_creation(self):
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

        self.table_emp_details.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_emp_details.setAlternatingRowColors(True)
        self.list_widget.setAlternatingRowColors(True)

    def populate_table(self):
        # Clear the list widget
        self.list_widget.clear()

        # create table
        self.table_creation()

        # populating the table
        for emp_data in self.employee_data:
            row = self.table_emp_details.rowCount()
            self.table_emp_details.insertRow(row)

            for col, field in enumerate(["emp_id", "fname", "lname", "email", "phone", "position"]):
                twi = QTableWidgetItem(str(emp_data[field]))
                twi.setTextAlignment(Qt.AlignCenter)
                self.table_emp_details.setItem(row, col, twi)

            supervisor_details = self.return_emp_name(emp_data["supervisor"])
            emp_id = emp_data["emp_id"]

            twi = QTableWidgetItem(supervisor_details)
            self.table_emp_details.setItem(row, 6, twi)

            # Add user role data to the list widget items
            list_widget_item = QListWidgetItem("{} {}".format(emp_data["fname"],emp_data["lname"]))
            list_widget_item.setData(Qt.UserRole, emp_id)
            self.list_widget.addItem(list_widget_item)

    def populate_tree(self):
        # Clear existing items in the tree
        self.tree_widget.clear()

        for emp_data in self.employee_data:
            emp_id = emp_data["emp_id"]
            name = "{} {}".format(emp_data["fname"], emp_data["lname"])
            phone = emp_data["phone"]
            email = emp_data["email"]
            position = emp_data["position"]
            supervisor = emp_data["supervisor"]

            # Conversion to string
            emp_id_str = str(emp_id)
            supervisor_str = str(supervisor)

            tree_widget_item = QTreeWidgetItem([emp_id_str, name, phone, email, position, supervisor_str])

            # Find the parent (supervisor) and add the current item as a child
            parent_item = self.find_tree_item(emp_data["supervisor"])
            if parent_item:
                parent_item.addChild(tree_widget_item)
            else:
                self.tree_widget.addTopLevelItem(tree_widget_item)

    def find_tree_item(self, supervisor_id):
        for item_index in range(self.tree_widget.topLevelItemCount()):
            item = self.tree_widget.topLevelItem(item_index)
            if item.text(0) == str(supervisor_id):
                return item
            child_item = self.find_child_tree_item(item, supervisor_id)
            if child_item:
                return child_item
        return None

    def find_child_tree_item(self, parent_item, supervisor_id):
        for child_index in range(parent_item.childCount()):
            child_item = parent_item.child(child_index)
            if child_item.text(0) == str(supervisor_id):
                return child_item
            sub_child_item = self.find_child_tree_item(child_item, supervisor_id)
            if sub_child_item:
                return sub_child_item
        return None

    def db_connection(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("../data/Employees.db")
        if db.open():
            print("table name:", db.tables())
            if "employee" not in db.tables():
                self.create_table()
            self.populate_data()
        else:
            QMessageBox.critical(self, "Database error", "Couldn't open the Database!!!")

    def populate_data(self):
        self.employee_data = []
        query = QSqlQuery("SELECT * FROM employee")
        while query.next():
            emp_data = {
                "emp_id": query.value("emp_id"),
                "fname": query.value("fname"),
                "lname": query.value("lname"),
                "email": query.value("email"),
                "phone": query.value("phone"),
                "position": query.value("position"),
                "supervisor": query.value("supervisor"),
            }
            self.employee_data.append(emp_data)

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

    def return_emp_name(self, supervisor_id):
        query = QSqlQuery()
        sql = "SELECT fname,lname,position FROM employee WHERE emp_id = {}".format(int(supervisor_id))
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

                # Update the class attribute
                self.populate_data()

                # Clear the current table
                self.table_emp_details.setRowCount(0)

                # Repopulate the table
                self.populate_table()

                # Repopulate the tree
                self.populate_tree()

            else:
                QMessageBox.critical(self, "Database error", "Failed to insert data into the employee table!")

    def evt_handler_button_update_emp(self):
        # emp_id = self.list_widget.currentItem().data(Qt.userRole)
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

                    # Update the class attribute
                    self.populate_data()

                    # Clear the current table
                    self.table_emp_details.setRowCount(0)

                    # Repopulate the table
                    self.populate_table()

                    # Repopulate the tree
                    self.populate_tree()

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

            # Update the class attribute
            self.populate_data()

            # Clear the current table
            self.table_emp_details.setRowCount(0)

            # Repopulate the table
            self.populate_table()

            # Repopulate the tree
            self.populate_tree()
        else:
            QMessageBox.information(self,"Error occurred","Some error has occurred retry!!!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgmain = DlgMain()
    dlgmain.show()
    sys.exit(app.exec_())
