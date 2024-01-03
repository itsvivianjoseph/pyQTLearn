import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBox Example")
        self.resize(500, 500)

        # Create a checkbox labeled "Enabled"
        self.checkbox_enabled = QCheckBox("Enabled", self)
        self.checkbox_enabled.move(200, 200)
        # Initially, the checkbox is enabled
        self.checkbox_enabled.setChecked(True)
        self.checkbox_enabled.toggled.connect(self.evt_handler_enabled)

        # Create a checkbox with three states
        self.checkbox_three_state = QCheckBox("Three State", self)
        self.checkbox_three_state.move(200, 100)
        self.checkbox_three_state.setTristate(True)

        # Label to display the state of the three-state checkbox
        self.label_tristate = QLabel("State - value", self)
        self.label_tristate.move(200, 140)

        # event handler for tri-state checkbox
        self.checkbox_three_state.stateChanged.connect(self.evt_handler_tristate)

        # Create a label
        self.label_text = QLabel("Text", self)
        self.label_text.move(200, 250)
        self.label_text.resize(150, 150)
        font = QFont("Times New Roman", 20, 75, True)
        self.label_text.setFont(font)

    def evt_handler_enabled(self, checked):
        # Event handler for the "Enabled" checkbox
        if checked:
            self.label_text.setEnabled(True)
        else:
            self.label_text.setDisabled(True)

    def evt_handler_tristate(self, state):
        # state value
        print(state)

        # Event handler for the three-state checkbox
        if state == Qt.Unchecked:
            self.label_tristate.setText("State: Unchecked")
            QMessageBox.information(self, "State", "Unchecked")
        elif state == Qt.Checked:
            self.label_tristate.setText("State: Checked")
            QMessageBox.information(self, "State", "Checked")
        elif state == Qt.PartiallyChecked:
            self.label_tristate.setText("State: Partially Checked")
            QMessageBox.information(self, "State", "Partially Checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg_main = DlgMain()
    dlg_main.show()
    sys.exit(app.exec_())