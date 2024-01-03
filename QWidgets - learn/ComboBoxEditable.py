import sys
from PyQt5.QtWidgets import QApplication, QDialog, QComboBox, QLabel, QMessageBox, QInputDialog


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("State and Plant Info")

        # ComboBox for states
        self.cmbStates = QComboBox(self)
        self.cmbStates.move(50, 50)
        self.populate_states_combobox()

        # Label for displaying population
        self.lblPop = QLabel("Population: 4000000", self)
        self.lblPop.move(180, 55)

        # ComboBox for plants
        self.cmbPlants = QComboBox(self)
        self.cmbPlants.move(50, 80)
        self.cmbPlants.resize(200, 20)
        self.cmbPlants.setEditable(True)
        self.cmbPlants.setDuplicatesEnabled(False)
        self.populate_plants_combobox()
        self.cmbPlants.currentIndexChanged.connect(self.evt_cmbPlants_changed)

    def populate_states_combobox(self):
        # Adding states to the ComboBox with associated data (abbreviation and population)
        state_data = [
            ("Alabama", {"ab": "AL", "pop": 4000000}),
            ("Alaska", {"ab": "AK", "pop": 500000}),
            ("Arizona", {"ab": "AZ", "pop": 7000000}),
            ("Arkansas", {"ab": "AR", "pop": 3000000}),
            ("Mississippi", {"ab": "MS", "pop": 5000000}),
            ("Missouri", {"ab": "MO", "pop": 5000000}),
            ("Minnesota", {"ab": "MN", "pop": 6000000}),
            ("Michigan", {"ab": "MI", "pop": 10000000})
        ]

        for state_name, state_info in state_data:
            self.cmbStates.addItem(state_name, state_info)

        # Connect signals to event handlers
        self.cmbStates.currentIndexChanged.connect(self.evt_cmbStates_changed)
        self.cmbStates.highlighted.connect(self.evt_cmbStates_highlighted)

    def populate_plants_combobox(self):
        # Adding plant names and species codes to the ComboBox
        plant_data = [
            ("Thalictrum occidentalis", "THOC"),
            ("Bouteloua gracilis", "BOGR"),
            ("Bromus tectus", "BRTE"),
            ("Picea engelmannii", "PIEN")
        ]

        for plant_name, species_code in plant_data:
            self.cmbPlants.addItem(plant_name, species_code)

    def evt_cmbStates_changed(self, idx):
        # Handle the event when the state ComboBox selection changes
        data = self.cmbStates.itemData(idx)
        QMessageBox.information(self, "State Info", "You selected {}\nwhich has a population of: {}".format(data["ab"], data["pop"]))

    def evt_cmbStates_highlighted(self, idx):
        # Handle the event when a state in the ComboBox is highlighted
        self.lblPop.setText("Population: {}".format(self.cmbStates.itemData(idx)["pop"]))

    def evt_cmbPlants_changed(self, idx):
        # Handle the event when the plant ComboBox selection changes
        if not self.cmbPlants.itemData(idx):
            # If no species code is set, prompt the user to add one
            species_code, bOk = QInputDialog.getText(self, "Add Species Code", f"Add a species code for '{self.cmbPlants.itemText(idx)}'")
            if bOk:
                self.cmbPlants.setItemData(idx, species_code)
        QMessageBox.information(self, "Plant Info", "You selected '{}' with species code: {}".format(self.cmbPlants.itemText(idx), self.cmbPlants.itemData(idx)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
