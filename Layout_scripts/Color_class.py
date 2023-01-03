import sys
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
from PySide6.QtCore import Qt


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        # This tells to set the background to the color provided
        self.setAutoFillBackground(True)

        palette = self.palette()

        # This changes the widget's QPalette.
        # QColor is provided by the value given by user
        palette.setColor(QPalette.Window, QColor(color))

        # This is then applied to the palette
        self.setPalette(palette)