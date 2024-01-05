import sys
from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import QTimer
import random

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Changing App")

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.color_label = QLabel()
        self.pixmap = QPixmap(50, 50)
        self.color_list = ["red", "green", "blue", "yellow", "violet", "black", "white"]
        self.pixmap.fill(QColor(random.choice(self.color_list)))
        self.color_label.setPixmap(self.pixmap)
        self.main_layout.addWidget(self.color_label)

        self.start_button = QPushButton("Start")
        self.main_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop")
        self.main_layout.addWidget(self.stop_button)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_timeout_handler)

        self.start_button.clicked.connect(self.start_timer_handler)
        self.stop_button.clicked.connect(self.stop_timer_handler)

    def start_timer_handler(self):
        self.timer.start(500)

    def stop_timer_handler(self):
        self.timer.stop()

    def timer_timeout_handler(self):
        color = random.choice(self.color_list)
        self.pixmap.fill(QColor(color))
        self.color_label.setPixmap(self.pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_dialog = MyDialog()
    my_dialog.show()
    sys.exit(app.exec_())
