import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        self.edit = QLineEdit("Just kidding")
        self.button = QPushButton("Show Greetings")

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print("Thank you {} <3".format(self.edit.text()))

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()

    sys.exit(app.exec())

