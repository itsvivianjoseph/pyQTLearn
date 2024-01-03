import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        self.btn = QPushButton("dates",self)
        self.btn.move(200, 200)
        self.btn.clicked.connect(self.evt_handler)

    def evt_handler(self):
        date = QDate.currentDate()
        print(date.toString())
        print(date.toJulianDay())
        print(date.dayOfYear())
        print(date.dayOfWeek())
        print(date.addDays(23).toString())

        TimeZ = QTimeZone(14,30,15)
        print(TimeZ.toString())
        TimeZ2 = TimeZ.addSecs(140)
        print(TimeZ2.tostring())

        dtm = QDateTime.currentDateTime()
        print(dtm.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(dlgMain.exec_())