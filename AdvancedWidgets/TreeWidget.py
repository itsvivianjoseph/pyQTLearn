import random
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QMessageBox


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        # Create widgets
        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(3)
        self.tree_widget.setHeaderLabels(["QT Column", "Methods", "Signals"])

        # Populate the tree
        self.populate_tree()

        # Sort the tree-widget items
        self.tree_widget.sortItems(0, Qt.AscendingOrder)

        # Set the default column width
        self.tree_widget.setColumnWidth(0, 200)

        # Mention the tree-items that have to be expanded by default
        self.tree_widget.expandItem(self.widget_item)

        self.tree_widget.itemDoubleClicked.connect(self.evt_handler_double_clicked)

        # Main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.tree_widget)

        # Setup layout
        self.setLayout(self.main_layout)

    def populate_tree(self):
        # Create top-level items
        self.widget_item = QTreeWidgetItem(self.tree_widget, ["QWidget Module"])
        self.gui_item = QTreeWidgetItem(self.tree_widget, ["QGUI Module"])
        self.core_item = QTreeWidgetItem(self.tree_widget, ["QCore Module"])

        # Add sub-items to QWidget Module
        list_widget_items = ["QDialog", "QLineEdit", "QTextEdit", "QGroupBox", "QFrame"]
        for item in list_widget_items:
            self.widget_item.addChild(QTreeWidgetItem([item, str(random.randrange(25)), str(random.randrange(8))]))

        # Add sub-items to QGUI items
        list_gui_items = ["QtWidget1", "QtWidget2", "QtWidget3"]
        for item in list_gui_items:
            self.gui_item.addChild(QTreeWidgetItem([item, str(random.randrange(25)), str(random.randrange(8))]))

        # Add sub-items to QCore Module
        list_core_items = ["QThread", "QDateTime", "QPixmap", "QUrl", "QFile"]
        for item in list_core_items:
            self.core_item.addChild(QTreeWidgetItem([item, str(random.randrange(25)), str(random.randrange(8))]))

        # Find and add sub-items to the QDialog
        dialog_item = self.tree_widget.findItems("QDialog", Qt.MatchRecursive)[0]
        list_dialog_items = ["QFileDialog", "QColorDialog", "QFontDialog", "QMessageBox"]
        for item in list_dialog_items:
            dialog_item.addChild(QTreeWidgetItem([item, str(random.randrange(25)), str(random.randrange(8))]))

    # Event handlers
    def evt_handler_double_clicked(self, twi, col):
        QMessageBox.information(self, "Qt Classes", "You chose the {}".format(twi.text(col)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
