import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.text_browser = QTextBrowser()

        self.main_layout.addWidget(self.text_browser)

        html_content = """
            <h1>
                <ul>
                    <li>item A</li>
                    <li>item B</li>
                    <li>item C</li>
                </ul>
            </h1>
        """

        self.text_browser.setHtml(html_content)

        self.load_html_button = QPushButton("Load HTML")
        self.main_layout.addWidget(self.load_html_button)
        self.load_html_button.clicked.connect(self.load_html_handler)

    def load_html_handler(self):
        file_url = "./dummy.html"
        self.text_browser.setSource(QUrl.fromLocalFile(file_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
