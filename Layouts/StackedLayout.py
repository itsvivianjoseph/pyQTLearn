import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class NestInfoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nest Information")

        # Create Widgets
        self.categorySelector = QComboBox()
        self.categorySelector.addItems(["General", "Species", "Location", "Surveys"])
        self.categorySelector.currentIndexChanged.connect(self.on_category_selector_changed)

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

        self.setupLayout()

    def setupLayout(self):
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QVBoxLayout()
        self.rightLayout = QStackedLayout()

        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.rightLayout)

        # Add Widgets to leftLayout
        self.leftLayout.addWidget(self.categorySelector)
        self.leftLayout.addStretch()

        # Add Stacked Widgets to rightLayout
        self.rightLayout.addWidget(self.generalWidget)
        self.rightLayout.addWidget(self.speciesWidget)
        self.rightLayout.addWidget(self.locationWidget)
        self.rightLayout.addWidget(self.surveysWidget)

        # Setup General Widget
        self.generalLayout = QFormLayout()
        self.generalLayout.addRow("Nest ID:", self.nestIDLabel)
        self.generalLayout.addRow("Date Found:", self.foundDateEdit)
        self.generalLayout.addRow("Date Last Surveyed:", self.lastSurveyDateEdit)
        self.generalLayout.addRow("Currently Active", self.activeCheckBox)
        self.generalWidget.setLayout(self.generalLayout)

        # Setup Species Widget
        self.speciesLayout = QFormLayout()
        self.speciesLayout.addRow("Species:", self.speciesComboBox)
        self.speciesLayout.addRow("Custom Species:", self.customSpeciesLineEdit)
        self.speciesLayout.addRow("Buffer:", self.bufferSpinBox)
        self.bufferSpinBox.setSuffix(" m")
        self.speciesWidget.setLayout(self.speciesLayout)

        # Setup Location Widget
        self.locationLayout = QFormLayout()
        self.locationLayout.addRow("Latitude:", self.latitudeSpinBox)
        self.locationLayout.addRow("Longitude:", self.longitudeSpinBox)
        self.locationWidget.setLayout(self.locationLayout)

        # Setup Surveys Widget
        self.surveysLayout = QVBoxLayout()
        self.surveysLayout.addWidget(self.surveysListWidget)
        self.surveysLayout.addWidget(self.addSurveyButton)
        self.surveysWidget.setLayout(self.surveysLayout)

        self.setLayout(self.mainLayout)

    def on_category_selector_changed(self, idx):
        self.rightLayout.setCurrentIndex(idx)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    nestInfoDialog = NestInfoDialog()
    nestInfoDialog.show()
    sys.exit(app.exec_())