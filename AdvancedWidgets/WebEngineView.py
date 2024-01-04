import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import QUrl


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        # Create the main layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Create a QWebEngineView widget and add it to the main layout
        self.web_engine_view = QWebEngineView()
        self.main_layout.addWidget(self.web_engine_view)

        # Set initial HTML content for the QWebEngineView
        initial_html = """
            <h1>Hello World!!</h1>
            <ul>
                <li>ITEM A</li>
                <li>ITEM B</li>
                <li>ITEM C</li>
            </ul>
        """
        self.web_engine_view.setHtml(initial_html)

        # Adding a line-edit to the main layout
        self.line_edit = QLineEdit("Enter the URL")
        self.main_layout.addWidget(self.line_edit)

        # Create a button to load a different HTML page
        self.button_load_html = QPushButton("Load Page")
        self.main_layout.addWidget(self.button_load_html)
        # Connect the button click event to the event handler method
        self.button_load_html.clicked.connect(self.evt_handler_load_page)

        # Create a button to load a plotpy output
        self.button_plotpy = QPushButton("load plotpy output")
        self.main_layout.addWidget(self.button_plotpy)
        self.button_plotpy.clicked.connect(self.evt_handler_load_plotpy)


    def evt_handler_load_page(self):
        # Retrieve the target URL from the line edit
        target_url = self.line_edit.text()
        print(target_url)
        # Set the QWebEngineView's URL to the specified target URL
        self.web_engine_view.setUrl(QUrl.fromUserInput(target_url))

    def evt_handler_load_plotpy(self):
        target_url = "/plotly.html"
        self.web_engine_view.setUrl(QUrl.fromLocalFile(target_url))


if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)
    # Create an instance of the custom dialog
    dialog = MyDialog()
    # Show the dialog
    dialog.show()
    # Run the application event loop
    sys.exit(app.exec_())