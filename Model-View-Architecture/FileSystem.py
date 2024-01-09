import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        # create layouts
        self.upper_layout = QHBoxLayout()
        self.lower_layout = QVBoxLayout()
        self.main_layout = QVBoxLayout()
        self.list_layout = QHBoxLayout()
        self.tree_layout = QHBoxLayout()

        # setup layouts
        self.setup_layouts()

        # File system model setup
        self.setup_file_sys()

    def setup_layouts(self):
        self.list_widget = QListWidget()
        self.tree_widget = QTreeWidget()
        self.table_widget = QTableWidget()

        self.list_layout.addWidget(self.list_widget)
        self.tree_layout.addWidget(self.tree_widget)

        self.upper_layout.addLayout(self.list_layout, 25)
        self.upper_layout.addLayout(self.tree_layout, 75)

        self.lower_layout.addWidget(self.table_widget)

        self.main_layout.addLayout(self.upper_layout, 60)
        self.main_layout.addLayout(self.lower_layout, 40)

    def setup_file_sys(self):
        self.model = QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.currentPath())

        # Set the model for the QTreeWidget
        self.tree_widget.setHeaderLabels(["Name", "Size", "Kind", "Date-modified"])
        self.tree_widget.setColumnWidth(0, 300)
        self.tree_widget.setColumnWidth(1, 100)
        self.tree_widget.setColumnWidth(2, 150)
        self.tree_widget.setColumnWidth(3, 200)
        self.tree_widget.setModel(self.model)
        self.tree_widget.setRootIndex(self.model.index(QtCore.QDir.currentPath()))

        # Connect selection change signal of the QTreeWidget to the slot
        self.tree_widget.selectionModel().selectionChanged.connect(self.tree_selection_changed)

        # Set the model for the QListWidget
        self.list_widget.setModel(self.model)
        self.list_widget.setRootIndex(self.model.index(QtCore.QDir.currentPath()))

        # Set the model for the QTableWidget
        self.table_widget.setHorizontalHeaderLabels(["Name", "Size", "Kind", "Date-modified"])
        self.table_widget.setColumnWidth(0, 300)
        self.table_widget.setColumnWidth(1, 100)
        self.table_widget.setColumnWidth(2, 150)
        self.table_widget.setColumnWidth(3, 200)
        self.table_widget.setModel(self.model)
        self.table_widget.setRootIndex(self.model.index(QtCore.QDir.currentPath()))

        # Connect the model signals to update the table when the directory changes
        self.model.directoryLoaded.connect(self.populate_table)
        self.model.fileRenamed.connect(self.populate_table)

    def tree_selection_changed(self):
        # Get the current index from the tree widget's selection model
        current_index = self.tree_widget.selectionModel().currentIndex()

        # Set the root index for both the list widget and table widget
        self.list_widget.setRootIndex(current_index)
        self.table_widget.setRootIndex(current_index)

    def populate_table(self):
        # Clear the existing rows
        self.table_widget.setRowCount(0)

        # Iterate through the items in the current directory and populate the table
        for row in range(self.model.rowCount()):
            item_index = self.model.index(row, 0, self.model.rootIndex())
            name = self.model.fileName(item_index)
            size = self.model.size(item_index)
            kind = "Folder" if self.model.isDir(item_index) else "File"
            date_modified = self.model.lastModified(item_index).toString("yyyy-MM-dd hh:mm:ss")

            # Insert a new row
            self.table_widget.insertRow(row)

            # Populate each column in the row
            self.table_widget.setItem(row, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(size)))
            self.table_widget.setItem(row, 2, QTableWidgetItem(kind))
            self.table_widget.setItem(row, 3, QTableWidgetItem(date_modified))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgmain = DlgMain()
    dlgmain.show()
    sys.exit(app.exec_())
