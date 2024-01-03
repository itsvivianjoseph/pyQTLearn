import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("State Selector")
        self.resize(500, 500)

        # Example 1: Combo box for state selection
        self.combo_states = QComboBox(self)
        self.combo_states.move(200, 100)
        self.combo_states.addItem("Tamil Nadu", "TN")
        self.combo_states.addItem("Uttar Pradesh", "UP")
        self.combo_states.addItem("Kerala", "KE")
        self.combo_states.addItem("Delhi", "DE")
        self.combo_states.addItem("Andhra Pradesh", "AP")
        self.combo_states.currentIndexChanged.connect(self.evt_handler_state_selected)

        # Example 2: Combo box with a list of elements
        self.combo_elements = QComboBox(self)
        self.combo_elements.move(200, 250)
        self.combo_elements.addItems(["Al", "Au", "Xe", "Mo", "Mi"])
        self.combo_elements.currentTextChanged.connect(self.evt_handler_element_selected)

        # Example 3: Combo box with items represented as dictionaries
        self.cmb_states_with_pop = QComboBox(self)
        self.cmb_states_with_pop.move(200, 300)
        self.cmb_states_with_pop.addItem("Alaska", {"ab": "AK", "pop": 500000})
        self.cmb_states_with_pop.addItem("Arizona", {"ab": "AZ", "pop": 7000000})
        self.cmb_states_with_pop.addItem("Arkansas", {"ab": "AR", "pop": 3000000})
        self.cmb_states_with_pop.addItem("Mississippi", {"ab": "MS", "pop": 5000000})
        self.cmb_states_with_pop.addItem("California", {"ab": "CA", "pop": 39500000})
        self.cmb_states_with_pop.addItem("New York", {"ab": "NY", "pop": 19500000})
        self.cmb_states_with_pop.addItem("Texas", {"ab": "TX", "pop": 29000000})
        self.cmb_states_with_pop.addItem("Florida", {"ab": "FL", "pop": 21000000})
        self.cmb_states_with_pop.currentIndexChanged.connect(self.evt_handler_state_selected)
        self.cmb_states_with_pop.highlighted.connect(self.evt_handler_state_selected_with_pop)

        self.label = QLabel("Population: ", self)
        self.label.move(250, 350)

    def evt_handler_state_selected_with_pop(self, idx):
        """
        Event handler called when the state selection changes in the state combo box with population data.
        Updates the label with the population information.

        :param idx: Index of the selected item
        """
        self.label.setText("Population: {}".format(self.cmb_states_with_pop.itemData(idx)["pop"]))

    def evt_handler_state_selected(self, idx):
        """
        Event handler called when the state selection changes in the state combo box.
        Shows an information message box with the selected state details.

        :param idx: Index of the selected item
        """
        selected_state_name = self.combo_states.currentText()
        selected_state_abbreviation = self.combo_states.itemData(idx)
        message = "You selected state: {} (Abbreviation: {})".format(selected_state_name, selected_state_abbreviation)
        QMessageBox.information(self, "State Selection", message)

    def evt_handler_element_selected(self, text):
        """
        Event handler called when the element selection changes in the elements combo box.
        Shows an information message box with the selected element.

        :param text: Text of the selected item
        """
        message = "You selected element: {}".format(text)
        QMessageBox.information(self, "Element Selection", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg_main = DlgMain()
    dlg_main.show()
    sys.exit(app.exec_())