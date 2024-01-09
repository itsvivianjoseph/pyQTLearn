import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class EmployeeCRUD(QMainWindow):
    def __init__(self):
        super(EmployeeCRUD, self).__init__()

        self.setWindowTitle("Employee CRUD")
        self.setGeometry(100, 100, 800, 600)

        self.setup_database()
        self.setup_model()
        self.setup_ui()

    def setup_database(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("employees.db")

        if not db.open():
            QMessageBox.critical(None, "Cannot open database",
                                 "Unable to establish a database connection.\n"
                                 "This example needs SQLite support. Please read "
                                 "the Qt SQL driver documentation for information "
                                 "how to build it.\n\n"
                                 "Click Cancel to exit.", QMessageBox.Cancel)
            sys.exit(1)

        query = db.exec_("""
            CREATE TABLE IF NOT EXISTS employee (
                emp_id INTEGER PRIMARY KEY,
                fname TEXT NOT NULL,
                lname TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE,
                position TEXT,
                supervisor INTEGER
            )
        """)

        if not query.isActive():
            print("Database creation failed")
            sys.exit(1)

    def setup_model(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("employee")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()

    def setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.table_view = QTableView(self)
        self.table_view.setModel(self.model)

        add_button = QPushButton("Add Employee")
        add_button.clicked.connect(self.add_employee)

        delete_button = QPushButton("Delete Employee")
        delete_button.clicked.connect(self.delete_employee)

        layout.addWidget(self.table_view)
        layout.addWidget(add_button)
        layout.addWidget(delete_button)

    def add_employee(self):
        record = self.model.record()
        record.setValue("fname", "")
        record.setValue("lname", "")
        record.setValue("email", "")
        record.setValue("phone", "")
        record.setValue("supervisor", 9999)

        if self.model.insertRecord(-1, record):
            print("Employee added successfully!")
        else:
            print("Error adding employee:", self.model.lastError().text())

    def delete_employee(self):
        current_row = self.table_view.selectionModel().currentIndex().row()
        if current_row >= 0:
            response = QMessageBox.question(self, "Delete Employee", "Are you sure you want to delete this employee?",
                                            QMessageBox.Yes | QMessageBox.No)

            if response == QMessageBox.Yes:
                if self.model.removeRow(current_row):
                    print("Employee deleted successfully!")
                else:
                    print("Error deleting employee:", self.model.lastError().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmployeeCRUD()
    window.show()
    sys.exit(app.exec_())
