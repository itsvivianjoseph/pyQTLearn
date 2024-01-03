import sys
from PyQt5.QtCore import QDate, QTime, QDateTime
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        # Date selection
        self.dateEdit = QDateTimeEdit(QDate.currentDate(), self)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.move(200, 100)

        # Time selection
        self.timeEdit = QDateTimeEdit(QTime.currentTime(), self)
        self.timeEdit.move(200, 150)

        # Date and time selection
        self.dateTimeEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.dateTimeEdit.move(200, 200)

        # Button to calculate elapsed time
        self.elapsedTimeButton = QPushButton("Elapsed Time", self)
        self.elapsedTimeButton.move(200, 250)
        self.elapsedTimeButton.clicked.connect(self.calculateElapsedTime)

    def calculateElapsedTime(self):
        current_date_time = QDateTime.currentDateTime()
        elapsed_seconds = current_date_time.secsTo(self.dateTimeEdit.dateTime())
        elapsed_time_string = "{} seconds have elapsed since {}".format(elapsed_seconds, self.dateTimeEdit.dateTime().toString())
        QMessageBox.information(self, "Elapsed Time", elapsed_time_string)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
