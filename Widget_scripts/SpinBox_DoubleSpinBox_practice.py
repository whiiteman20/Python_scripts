import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("SpinBox/DoubleSpinBox Practice")

        # QSpinBox = int only and QDoubleSpinBox = float only
        widget = QSpinBox()
        # OR widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or widget.setRange(-10,3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3) # Or e.g. 0.5 for QDoubleSpinBox

        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
