import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QRadioButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        # Main layout
        self.main_layout = QHBoxLayout()

        # Checkable group box
        self.checkable_group_box = QGroupBox("Checkable")
        self.rbt_check_true = QRadioButton("True")
        self.rbt_check_false = QRadioButton("False")
        self.checkable_layout = QVBoxLayout()
        self.checkable_layout.addWidget(self.rbt_check_true)
        self.checkable_layout.addWidget(self.rbt_check_false)
        self.checkable_group_box.setLayout(self.checkable_layout)
        self.main_layout.addWidget(self.checkable_group_box)
        self.rbt_check_true.toggled.connect(self.evt_rbt_check_toggled)

        # Flat group box
        self.flat_group_box = QGroupBox("Flat")
        self.rbt_flat_true = QRadioButton("True")
        self.rbt_flat_false = QRadioButton("False")
        self.flat_layout = QVBoxLayout()
        self.flat_layout.addWidget(self.rbt_flat_true)
        self.flat_layout.addWidget(self.rbt_flat_false)
        self.flat_group_box.setLayout(self.flat_layout)
        self.rbt_flat_true.toggled.connect(self.evt_rbt_flat_toggled)
        self.main_layout.addWidget(self.flat_group_box)

        # Alignment group box
        self.align_group_box = QGroupBox("Alignment")
        self.rbt_align_left = QRadioButton("Alignment Left")
        self.rbt_align_center = QRadioButton("Alignment Center")
        self.rbt_align_right = QRadioButton("Alignment Right")
        self.align_layout = QVBoxLayout()
        self.align_layout.addWidget(self.rbt_align_left)
        self.align_layout.addWidget(self.rbt_align_center)
        self.align_layout.addWidget(self.rbt_align_right)
        self.align_group_box.setLayout(self.align_layout)
        self.rbt_align_left.toggled.connect(self.evt_rbt_align_left_toggled)
        self.rbt_align_center.toggled.connect(self.evt_rbt_align_center_toggled)
        self.rbt_align_right.toggled.connect(self.evt_rbt_align_right_toggled)
        self.main_layout.addWidget(self.align_group_box)

        # Set main layout
        self.setLayout(self.main_layout)

    def evt_rbt_check_toggled(self, checked):
        self.checkable_group_box.setCheckable(checked)

    def evt_rbt_flat_toggled(self, checked):
        self.flat_group_box.setFlat(checked)

    def evt_rbt_align_left_toggled(self, checked):
        if checked:
            self.align_group_box.setAlignment(Qt.AlignLeft)
            self.align_group_box.setTitle("Left Alignment")

    def evt_rbt_align_right_toggled(self, checked):
        if checked:
            self.align_group_box.setAlignment(Qt.AlignRight)
            self.align_group_box.setTitle("Right Alignment")

    def evt_rbt_align_center_toggled(self, checked):
        if checked:
            self.align_group_box.setAlignment(Qt.AlignCenter)
            self.align_group_box.setTitle("Center Alignment")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec_())
