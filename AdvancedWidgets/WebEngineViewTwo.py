import random
import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QMessageBox, QComboBox, \
    QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(1000, 700)

        # Create widgets
        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(1)  # Set column count to 1
        self.tree_widget.setHeaderLabels(["QT Column"])

        # Populate the tree
        self.populate_tree()

        # Sort the tree-widget items
        self.tree_widget.sortItems(0, Qt.AscendingOrder)

        # Set the default column width
        self.tree_widget.setColumnWidth(0, 200)

        # Mention the tree-items that have to be expanded by default
        self.tree_widget.expandItem(self.widget_item)

        self.tree_widget.itemDoubleClicked.connect(self.evt_handler_double_clicked)

        # combo-box
        self.combo_box = QComboBox()
        list_classes = get_all_items(self.tree_widget)
        list_classes.sort()
        for clas in list_classes:
            self.combo_box.addItem(clas.text(0))

        # line-edit for entering a new class to the hierarchy
        self.line_edit = QLineEdit("Q")

        # button for adding class to hierarchy
        self.button_add_class = QPushButton("Add the class to the hierarchy")
        self.button_add_class.clicked.connect(self.evt_handler_add_class)

        # web-engine view
        self.web_engine_view = QWebEngineView()

        # button for forward
        self.button_forward = QPushButton(">>")
        self.button_backward = QPushButton("<<")
        self.button_home = QPushButton("Home")

        # set web-engine-views url
        self.web_engine_view.setUrl(QUrl.fromUserInput("https://doc.qt.io/qt-5/qtmodules.html"))

        # button connections
        self.button_forward.clicked.connect(self.web_engine_view.forward)
        self.button_backward.clicked.connect(self.web_engine_view.back)
        self.button_home.clicked.connect(self.evt_handler_go_home)

        # layouts
        self.main_layout = QHBoxLayout()
        self.tree_layout = QVBoxLayout()
        self.web_engine_view_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()

        # add widgets to button-layout
        self.button_layout.addWidget(self.button_backward)
        self.button_layout.addWidget(self.button_forward)
        self.button_layout.addWidget(self.button_home)

        # add widgets to tree-layout
        self.tree_layout.addWidget(self.tree_widget)
        self.tree_layout.addWidget(self.combo_box)
        self.tree_layout.addWidget(self.line_edit)
        self.tree_layout.addWidget(self.button_add_class)

        # add widgets to the web-engine view layout
        self.web_engine_view_layout.addWidget(self.web_engine_view)
        self.web_engine_view_layout.addLayout(self.button_layout)  # Add button_layout to web_engine_view_layout

        # add sub-layouts to the main-layout
        self.main_layout.addLayout(self.tree_layout, 30)
        self.main_layout.addLayout(self.web_engine_view_layout, 70)

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
            self.widget_item.addChild(QTreeWidgetItem([item]))

        # Add sub-items to QGUI items
        list_gui_items = ["QtWidget1", "QtWidget2", "QtWidget3"]
        for item in list_gui_items:
            self.gui_item.addChild(QTreeWidgetItem([item]))

        # Add sub-items to QCore Module
        list_core_items = ["QThread", "QDateTime", "QPixmap", "QUrl", "QFile"]
        for item in list_core_items:
            self.core_item.addChild(QTreeWidgetItem([item]))

        # Find and add sub-items to the QDialog
        dialog_item = self.tree_widget.findItems("QDialog", Qt.MatchRecursive)[0]
        list_dialog_items = ["QFileDialog", "QColorDialog", "QFontDialog", "QMessageBox"]
        for item in list_dialog_items:
            dialog_item.addChild(QTreeWidgetItem([item]))

    # Event handlers
    def evt_handler_double_clicked(self, twi, col):
        # QMessageBox.information(self, "Qt Classes", "You chose the {}".format(twi.text(col)))
        url = "https://doc.qt.io/qt-5/{}.html".format(twi.text(0)).lower()
        self.web_engine_view.setUrl(QUrl.fromUserInput(url))

    def evt_handler_add_class(self):
        ans = QMessageBox.question(self, "Add Class", "Are you sure that you want to add {} to {}".format(self.line_edit.text(), self.combo_box.currentText()))
        if ans == QMessageBox.Yes:
            tree_widget_item = self.tree_widget.findItems(self.combo_box.currentText(), Qt.MatchRecursive)[0]
            tree_widget_item.addChild(QTreeWidgetItem([self.line_edit.text()]))

    def evt_handler_go_home(self):
        self.web_engine_view.setUrl(QUrl.fromUserInput("https://doc.qt.io/qt-5/qtmodules.html"))


def get_all_items(tree_widget):
    all_items = []

    # Loop over top-level items
    for i in range(tree_widget.topLevelItemCount()):
        top_item = tree_widget.topLevelItem(i)
        stack = [top_item]

        # Process items in a depth-first manner
        while stack:
            current_item = stack.pop()
            all_items.append(current_item)

            # Separate for-loop for extending the stack with child items
            for j in range(current_item.childCount()):
                stack.append(current_item.child(j))

    return all_items


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
