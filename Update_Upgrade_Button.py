#!/usr/bin/env python3
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys
import subprocess

window_titles = ["My App", "Booty Head", "Still my App", "What is going on?"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")

        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        cmd = input("Enter the command you want to use: ")
        cmd_split = cmd.split()
        subprocess.run(cmd_split, capture_output=True, shell=True, check=True)
            

app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()
