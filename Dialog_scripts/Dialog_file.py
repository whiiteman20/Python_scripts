import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog File Practice")

        button1 = QPushButton("Open File")
        button1.clicked.connect(self.get_filename)

        self.setCentralWidget(button1)

    def get_filename(self):
        filters = 'Portable Network Graphics files (*.png);;Comma Separated Values (*.csv);; Text files (*.txt);;' \
                  'All files (*)'
        print("Filters are: ", filters)
        filename, select_filter = QFileDialog.getOpenFileName(self, filter=filters)
        print("Result:", filename, select_filter)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()