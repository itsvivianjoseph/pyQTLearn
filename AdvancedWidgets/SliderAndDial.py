import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QSlider, QDial


class SliderDialDemo(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Slider and Dial Demo")
        self.resize(300, 200)

        self.slider = QSlider()
        self.dial = QDial()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.dial)

        self.slider.valueChanged.connect(self.update_dial_value)
        self.dial.valueChanged.connect(self.update_slider_value)

        self.setLayout(self.layout)

    def update_dial_value(self, value):
        self.dial.setValue(value)

    def update_slider_value(self, value):
        self.slider.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = SliderDialDemo()
    demo.show()
    sys.exit(app.exec_())
