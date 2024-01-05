import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QCheckBox, QLineEdit, QVBoxLayout, QListWidget, QMessageBox, QStyleFactory


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Style Selection Dialog")

        # Widgets
        self.button_one = QPushButton("Button 1")
        self.button_two = QPushButton("Button 2")
        self.button_three = QPushButton("Button 3")

        self.check_box = QCheckBox("Check box 1")

        self.line_edit_one = QLineEdit("Editable")
        self.line_edit_two = QLineEdit("Read Only")
        self.line_edit_two.setReadOnly(True)

        self.style_list = QListWidget()
        # Populate the list with available styles
        self.style_list.addItems(QStyleFactory.keys())
        # Connect itemDoubleClicked signal to the handler method
        self.style_list.itemDoubleClicked.connect(self.evt_handler_style_selection)

        # Main Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.button_one)
        self.main_layout.addWidget(self.button_two)
        self.main_layout.addWidget(self.button_three)
        self.main_layout.addWidget(self.check_box)
        self.main_layout.addWidget(self.line_edit_one)
        self.main_layout.addWidget(self.line_edit_two)
        self.main_layout.addWidget(self.style_list)

        self.setLayout(self.main_layout)

    def evt_handler_style_selection(self, item):
        # Set the application style based on the selected item from the list
        app.setStyle(QStyleFactory.create(item.text()))
        # Show an information dialog about the selected style
        QMessageBox.information(self, "Style Set", "You selected the '{}' style".format(item.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg_main = MyDialog()
    dlg_main.show()
    sys.exit(app.exec_())
