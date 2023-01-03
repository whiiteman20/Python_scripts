import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        # This allows you to add objects to the list
        widget.setEditable(True)

        # Below allows you to limit the number of items allowed in the box
        widget.setMaxCount(10)

        # This is how you can create an insert policy.
        # There are NoInsert, InsertAtTop, InsertAtCurrent, InsertAtBottom, InsertAfterCurrent
        # InsertBeforeCurrent, and InsertAlphabetically
        widget.setInsertPolicy(QComboBox.InsertAlphabetically)

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()