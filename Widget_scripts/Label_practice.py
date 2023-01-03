import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

basedir = os.path.dirname(__file__)
print("Current working folder: ", os.getcwd())
print("Paths are relative to: ", basedir)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Label Practice")

        widget = QLabel("Fuck me cootie?")
        font = widget.font()
        font.setPointSize(100)
        widget.setFont(font)
        # This actually determines where the widget will be aligned on the window.
        # You can also use widget.setAlignment(Qt.AlignCenter) to get the same effect below.
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

