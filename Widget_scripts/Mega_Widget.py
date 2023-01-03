from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, 
                               QVBoxLayout, QWidget, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit, QDial, 
                               QDoubleSpinBox, QFontComboBox, QLCDNumber, QProgressBar, QPushButton, QRadioButton,
                               QSlider, QSpinBox, QTimeEdit)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.checkbox = QCheckBox()
        self.combobox = QComboBox()
        self.dateedit = QDateEdit()
        self.datetimeedit = QDateTimeEdit()
        self.dial = QDial()
        self.doublespinbox = QDoubleSpinBox()
        self.fontcombobox = QFontComboBox()
        self.lcdnumber = QLCDNumber()
        self.progbar = QProgressBar()
        self.pushbutton = QPushButton()
        self.radiobutton = QRadioButton()
        self.slider = QSlider()
        self.spinbox = QSpinBox()
        self.timeedit = QTimeEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.combobox)
        layout.addWidget(self.dateedit)
        layout.addWidget(self.datetimeedit)
        layout.addWidget(self.dial)
        layout.addWidget(self.doublespinbox)
        layout.addWidget(self.fontcombobox)
        layout.addWidget(self.lcdnumber)
        layout.addWidget(self.progbar)
        layout.addWidget(self.pushbutton)
        layout.addWidget(self.radiobutton)
        layout.addWidget(self.slider)
        layout.addWidget(self.spinbox)
        layout.addWidget(self.timeedit)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()