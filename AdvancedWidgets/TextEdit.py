import sys
from PyQt5.QtGui import QTextCursor, QColor
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QTextEdit, QPushButton, QColorDialog


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        self.main_layout = QVBoxLayout(self)

        self.text_edit = QTextEdit()
        self.text_edit.setText("01234567890123456789012345678901234567890123456789012345678901234567890123456789")
        self.main_layout.addWidget(self.text_edit)

        self.button_bg = QPushButton("Set Background Color")
        self.main_layout.addWidget(self.button_bg)
        self.button_bg.clicked.connect(self.evt_handler)

        self.button_html = QPushButton("Add HTML")
        self.main_layout.addWidget(self.button_html)
        self.button_html.clicked.connect(self.evt_html_handler)

        self.set_text_color()

    def evt_handler(self):
        color = QColorDialog.getColor(QColor("black"))
        self.text_edit.setTextBackgroundColor(color)

    def evt_html_handler(self):
        html = """
            <h1>
                <ul>
                    <li>A</li>
                    <li>B</li>
                    <li>C</li>
                </ul>
            </h1>
        """
        self.text_edit.setHtml(html)

    def set_text_color(self):
        cursor = self.text_edit.textCursor()
        cursor.setPosition(15, QTextCursor.MoveAnchor)
        cursor.setPosition(25, QTextCursor.KeepAnchor)
        self.text_edit.setTextCursor(cursor)

        # Set text color (uncomment the line below to set the text color)
        # self.text_edit.setTextColor(QColor("red"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg_main = DlgMain()
    dlg_main.show()
    sys.exit(app.exec_())