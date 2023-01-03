import sys
from random import randint
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QLabel)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget.
    If it hs no parent, it will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window {}".format(randint(0,100)))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)


    def show_new_window(self, checked):
        self.w.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()