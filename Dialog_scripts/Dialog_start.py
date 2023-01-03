import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QDialog, QDialogButtonBox, QVBoxLayout,
                               QLabel, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog practice")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        button.setCheckable(True)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("Click", s)

        # setting CustomDialog to self helps make the dialog appear over parent window
        dlg = CustomDialog(self)

        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

class CustomDialog(QDialog):
    # Set a default of None so we can omit the parent if we wish
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("HELLO")

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


app = QApplication()

window = MainWindow()
window.show()

app.exec()