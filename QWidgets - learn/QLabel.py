import sys
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import *


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set up the main dialog window
        self.setWindowTitle("Image Display GUI")
        self.resize(500, 500)

        # Create a label to display the image
        self.image_label = QLabel("old text", self)
        self.image_label.move(150, 200)
        self.image_label.resize(250, 250)

        # Set font for the label
        label_font = QFont("Times New Roman", 20, 75, True)
        self.image_label.setFont(label_font)

        # Create a button to change the image
        self.change_image_button = QPushButton("Change Image", self)
        self.change_image_button.move(200, 200)
        self.change_image_button.clicked.connect(self.change_image_handler)

    def change_image_handler(self):
        # HTML content for the label (commented out in the modified code)
        # text = """
        #     <h1>Hello world!</h1>
        #     <ul>
        #         <li>red</li>
        #         <li>blue</li>
        #         <li>green</li>
        #     </ul>
        # """

        # self.image_label.setText(text)
        # self.image_label.repaint()

        # Load and scale the image from file
        image_path = "Photos/vivian.jpeg"
        scaled_image = QPixmap(image_path).scaled(100, 100)

        # Set the scaled image as the pixmap for the label
        self.image_label.setPixmap(scaled_image)

        # Repaint the label to reflect the changes
        self.image_label.repaint()


if __name__ == "__main__":
    # Set up the application and run the main dialog
    app = QApplication(sys.argv)
    main_dialog = MyDialog()
    main_dialog.show()
    sys.exit(app.exec_())