import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("LineEdit Practice")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")

        # widget.setReadOnly(True) # uncomment this to make readonly

        # When the Enter key is pressed, action happens
        widget.returnPressed.connect(self.return_pressed)
        # When the selection changes, action happens (need to uncomment widget.setReadOnly(True) for this to work)
        widget.selectionChanged.connect(self.selection_changed)
        # When the text changes, action happens
        widget.textChanged.connect(self.text_changed)
        # When the text is edited, action happens
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

        # It is possible to perform input validation using an input mask to define which
        # characters are supported and where
        # widget.setInputMask('000.000.000.000;_')

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()