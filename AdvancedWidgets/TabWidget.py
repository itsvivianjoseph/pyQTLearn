import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class NestInfoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nest Information")

        # Create Widgets
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.on_tab_closed)

        self.generalWidget = QWidget()
        self.speciesWidget = QWidget()
        self.locationWidget = QWidget()
        self.surveysWidget = QWidget()

        # General Widgets
        self.nestIDLabel = QLabel("34")
        self.foundDateEdit = QDateTimeEdit(QDate(2016, 5, 13))
        self.lastSurveyDateEdit = QDateTimeEdit(QDate(2020, 4, 14))
        self.activeCheckBox = QCheckBox()

        # Species Widgets
        self.speciesComboBox = QComboBox()
        self.speciesComboBox.addItem("Red-tailed Hawk", 800)
        self.speciesComboBox.addItem("Swainson's Hawk", 400)
        self.speciesComboBox.addItem("Other", 1600)

        self.customSpeciesLineEdit = QLineEdit()
        self.bufferSpinBox = QSpinBox()
        self.bufferSpinBox.setValue(800)

        # Location Widgets
        self.latitudeSpinBox = QDoubleSpinBox()
        self.longitudeSpinBox = QDoubleSpinBox()

        # Surveys Widgets
        self.surveysListWidget = QListWidget()
        self.surveysListWidget.addItems([
            "03/24/2020 - MSM - INACTIVE",
            "03/30/2020 - MSM - INACTIVE",
            "04/07/2020 - MSM - INACTIVE",
            "04/14/2020 - MSM - ACTIVE!!"
        ])
        self.addSurveyButton = QPushButton("Add Survey")

        self.setup_layout()

    def setup_layout(self):
        self.main_layout = QHBoxLayout()

        self.main_layout.addWidget(self.tabWidget)

        # Add Tabs to tab widget
        self.tabWidget.addTab(self.generalWidget, "General")
        self.tabWidget.addTab(self.speciesWidget, "Species")
        self.tabWidget.addTab(self.locationWidget, "Location")
        self.tabWidget.addTab(self.surveysWidget, "Surveys")

        # Setup General Widget
        self.general_layout = QFormLayout()
        self.general_layout.addRow("Nest ID:", self.nestIDLabel)
        self.general_layout.addRow("Date Found:", self.foundDateEdit)
        self.general_layout.addRow("Date Last Surveyed:", self.lastSurveyDateEdit)
        self.general_layout.addRow("Currently Active", self.activeCheckBox)
        self.generalWidget.setLayout(self.general_layout)

        # Setup Species Widget
        self.species_layout = QFormLayout()
        self.species_layout.addRow("Species:", self.speciesComboBox)
        self.species_layout.addRow("Custom Species:", self.customSpeciesLineEdit)
        self.species_layout.addRow("Buffer:", self.bufferSpinBox)
        self.bufferSpinBox.setSuffix(" m")
        self.speciesWidget.setLayout(self.species_layout)

        # Setup Location Widget
        self.location_layout = QFormLayout()
        self.location_layout.addRow("Latitude:", self.latitudeSpinBox)
        self.location_layout.addRow("Longitude:", self.longitudeSpinBox)
        self.locationWidget.setLayout(self.location_layout)

        # Setup Surveys Widget
        self.surveys_layout = QVBoxLayout()
        self.surveys_layout.addWidget(self.surveysListWidget)
        self.surveys_layout.addWidget(self.addSurveyButton)
        self.surveysWidget.setLayout(self.surveys_layout)

        self.setLayout(self.main_layout)

    def on_tab_closed(self, idx):
        ans = QMessageBox.question(self, "Close", "Are you sure that you want to remove the '{}' tab?".format(self.tabWidget.tabText(idx)))
        if ans == QMessageBox.Yes:
            self.tabWidget.removeTab(idx)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    nest_info_dialog = NestInfoDialog()
    nest_info_dialog.show()
    sys.exit(app.exec_())
