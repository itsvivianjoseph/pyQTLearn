import sys
from PyQt5.QtWidgets import *


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        # Create widgets
        self.list_available_languages = QListWidget()
        self.list_available_languages.addItems(["C", "C++", "C#", "JavaScript", "Python", "PHP", "JAVA", "Ruby", "Rust", "Visual Basic", "Julia", "GO"])
        self.list_selected_languages = QListWidget()

        self.list_available_languages.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_available_languages.sortItems()

        self.button_add_language = QPushButton("-->")
        self.button_add_language.clicked.connect(self.evt_handler_add_lang)
        self.list_available_languages.itemSelectionChanged.connect(self.evt_handler_lang_select)

        self.button_remove_language = QPushButton("<--")
        self.button_remove_language.clicked.connect(self.evt_handler_remove_lang)
        self.list_available_languages.itemSelectionChanged.connect(self.evt_handler_lang_remove)

        self.list_selected_languages.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.button_do_something = QPushButton("Do Something")
        self.button_do_something.clicked.connect(self.evt_handler_do_smtg)

        self.setup_layout()

    def setup_layout(self):
        main_layout = QVBoxLayout()
        lists_layout = QHBoxLayout()
        buttons_layout = QVBoxLayout()

        # Add widgets to the buttons layout
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.button_add_language)
        buttons_layout.addWidget(self.button_remove_language)
        buttons_layout.addStretch()

        # Add widgets to the lists layout
        lists_layout.addWidget(self.list_available_languages)
        lists_layout.addLayout(buttons_layout)
        lists_layout.addWidget(self.list_selected_languages)

        # Add widgets to the main layout
        main_layout.addLayout(lists_layout)
        main_layout.addWidget(self.button_do_something)

        # Set the main layout
        self.setLayout(main_layout)


    # event handlers
    def evt_handler_add_lang(self):
        list_items = self.list_available_languages.selectedItems()
        for item in list_items:
            self.list_selected_languages.addItem(item.text())
            self.list_available_languages.takeItem(self.list_available_languages.row(item))
            # print(item.text())
        self.list_selected_languages.sortItems()

    def evt_handler_remove_lang(self):
        list_items = self.list_selected_languages.selectedItems()
        for item in list_items:
            self.list_available_languages.addItem(item.text())
            self.list_selected_languages.takeItem(self.list_selected_languages.row(item))
            # print(item.text())
        self.list_available_languages.sortItems()

    def evt_handler_lang_select(self):
        self.button_add_language.setDefault(True)
        self.repaint()

    def evt_handler_lang_remove(self):
        self.button_remove_language.setDefault(True)
        self.repaint()

    def evt_handler_do_smtg(self):
        if self.list_selected_languages.count() == 0:
            QMessageBox.information(self,"languages","0 languages known!!!")
        else:
            list_items = self.list_selected_languages.selectedItems()
            str = ""
            for item in list_items:
                str += item.text()
                str += " "
            QMessageBox.information(self,"languages","you know {} languages!!!".format(str))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec_())
