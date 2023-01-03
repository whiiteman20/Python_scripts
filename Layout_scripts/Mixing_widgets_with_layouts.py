import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QVBoxLayout, QLabel,
                               QMainWindow, QPushButton, QWidget, QStackedLayout)
from Color_class import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Mixing it up")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        button = QPushButton('Red')
        button.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(button)
        self.stacklayout.addWidget((Color('red')))

        button = QPushButton('Green')
        button.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(button)
        self.stacklayout.addWidget((Color('green')))

        button = QPushButton('Yellow')
        button.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(button)
        self.stacklayout.addWidget((Color('yellow')))

        button = QPushButton('Blue')
        button.pressed.connect(self.activate_tab_4)
        button_layout.addWidget(button)
        self.stacklayout.addWidget((Color('blue')))

        button = QPushButton('Purple')
        button.pressed.connect(self.activate_tab_5)
        button_layout.addWidget(button)
        self.stacklayout.addWidget((Color('purple')))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)

    def activate_tab_4(self):
        self.stacklayout.setCurrentIndex(3)

    def activate_tab_5(self):
        self.stacklayout.setCurrentIndex(4)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
