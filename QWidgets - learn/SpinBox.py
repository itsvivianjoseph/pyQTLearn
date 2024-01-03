import sys
from PyQt5.QtWidgets import *


class NumberInputDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set up the main dialog window
        self.setWindowTitle("Number Input Dialog")
        self.setGeometry(100, 100, 300, 150)

        # Create a spin box for integer input
        self.intSpinBox = QSpinBox(self)
        self.intSpinBox.move(50, 20)
        self.intSpinBox.setRange(0, 10000)
        self.intSpinBox.setSingleStep(200)
        self.intSpinBox.setValue(1000)
        self.intSpinBox.valueChanged.connect(self.handleIntSpinBoxValueChanged)
        self.intSpinBox.editingFinished.connect(self.handleIntSpinBoxEditingFinished)

        # Create a spin box for double input (latitude)
        self.doubleSpinBox = QDoubleSpinBox(self)
        self.doubleSpinBox.move(50, 60)
        self.doubleSpinBox.setDecimals(5)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setPrefix("Latitude: ")
        self.doubleSpinBox.setSuffix(chr(176))
        self.doubleSpinBox.setRange(-90, 90)
        self.doubleSpinBox.editingFinished.connect(self.handleDoubleSpinBoxEditingFinished)

    def handleIntSpinBoxValueChanged(self, value):
        print("Integer value changed:", value, value % 200)
        if value % 200:
            self.intSpinBox.setStyleSheet("color:red")
        else:
            self.intSpinBox.setStyleSheet("color:black")

    def handleIntSpinBoxEditingFinished(self):
        print("Editing finished for integer spin box")
        if self.intSpinBox.value() % 200:
            QMessageBox.warning(self, "Invalid Value", "Invalid value entered. \nMust be divisible by 200")
            self.intSpinBox.setFocus()

    def handleDoubleSpinBoxEditingFinished(self):
        message = "Latitude Information:\nText: '{}'\nValue: {}".format(self.doubleSpinBox.text(),
                                                                        self.doubleSpinBox.value())
        QMessageBox.information(self, "Latitude", message)
        self.setWindowTitle(self.doubleSpinBox.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    numberInputDialog = NumberInputDialog()
    numberInputDialog.show()
    sys.exit(app.exec_())






# import sys
# from PyQt5.QtWidgets import *
#
#
# class DlgMain(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My GUI")
#         self.resize(500,500)
#
#         # spinbox type int
#         self.spinboxint = QSpinBox(self)
#         self.spinboxint.move(200, 100)
#         self.spinboxint.setWrapping(True)
#         self.spinboxint.setRange(0, 10000)
#         self.spinboxint.setSingleStep(200)
#         self.spinboxint.setValue(1000) #default value
#         self.spinboxint.setStyleSheet("color:green")
#         self.spinboxint.valueChanged.connect(self.evt_handler)
#
#         # spinbox type double
#         self.spinboxdouble = QDoubleSpinBox(self)
#         self.spinboxdouble.move(200,300)
#         self.spinboxdouble.setDecimals(5)
#         self.spinboxdouble.setSingleStep(10)
#         self.spinboxdouble.setPrefix("Latitude :")
#         self.spinboxdouble.setSuffix(chr(176))
#         self.spinboxdouble.setRange(-90,90)
#         self.spinboxdouble.valueChanged.connect(self.evt_Handler_double)
#
#     def evt_handler(self,val):
#         if val % 200 == 0:
#             self.spinboxint.setStyleSheet("color:green")
#         else:
#             self.spinboxint.setStyleSheet("color:red")
#
#     def evt_Handler_double(self):
#         print(self.spinboxdouble.text())
#         print(self.spinboxdouble.value())
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dlgmain = DlgMain()
#     dlgmain.show()
#     sys.exit(dlgmain.exec_())
