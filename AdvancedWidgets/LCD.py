import sys
from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QLCDNumber

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        self.lcd_number = QLCDNumber()
        self.lcd_number.display(120)
        self.lcd_number.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_number.setStyleSheet("background-color:black'color:green")
        # self.lcd_number.setHexMode() - display the number in hexadecimal - base 16
        # self.lcd_number.setOctMode() - display the number in octal - base 8
        # self.lcd_number.setBinMode() - display the number in binary - base 2

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.lcd_number)
        self.setLayout(self.main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec_())