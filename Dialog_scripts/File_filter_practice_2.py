import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QLineEdit, QVBoxLayout, QWidget, QPushButton)

FILE_FILTERS = [
    'Portable Network Graphics files (*.png)',
    'Text files (*.txt)',
    'Comma Separated files (*.csv)',
    'All files (*)',
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File filter practice 2")

        layout = QVBoxLayout()

        button1 = QPushButton("Open File")
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)

        button2 = QPushButton("Open Files")
        button2.clicked.connect(self.get_filenames)
        layout.addWidget(button2)

        button3 = QPushButton("Save file")
        button3.clicked.connect(self.get_save_filename)
        layout.addWidget(button3)

        button4 = QPushButton("Select folder")
        button4.clicked.connect(self.get_folder)
        layout.addWidget(button4)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_filename(self):
        caption = "Open File"
        initial_dir = ""
        initial_filter = FILE_FILTERS[3]

        dialog = QFileDialog()
        dialog.setWindowTitle(caption)
        dialog.setDirectory(initial_dir)
        dialog.setNameFilters(FILE_FILTERS)
        dialog.selectNameFilter(initial_filter)
        dialog.setFileMode(QFileDialog.ExistingFile)

        ok = dialog.exec()
        print("Result:", ok, dialog.selectedFiles(), dialog.selectedNameFilter(),)

    def get_filenames(self):
        caption = "Open Files"
        initial_dir = ""
        initial_filter = FILE_FILTERS[1]

        dialog = QFileDialog()
        dialog.setWindowTitle(caption)
        dialog.setDirectory(initial_dir)
        dialog.setNameFilters(FILE_FILTERS)
        dialog.selectNameFilter(initial_filter)
        dialog.setFileMode(QFileDialog.ExistingFiles)

        ok = dialog.exec()
        print("Result:", ok, dialog.selectedFiles(), dialog.selectedNameFilter(), )

    def get_save_filename(self):
        caption = "Save File"
        initial_dir = ""
        initial_filter = FILE_FILTERS[1]

        dialog = QFileDialog()
        dialog.setWindowTitle(caption)
        dialog.setDirectory(initial_dir)
        dialog.setNameFilters(FILE_FILTERS)
        dialog.selectNameFilter(initial_filter)
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)

        ok = dialog.exec()
        print("Result:", ok, dialog.selectedFiles(), dialog.selectedNameFilter(), )

    def get_folder(self):
        caption = "Select Folder"
        initial_dir = ""
        initial_filter = FILE_FILTERS[1]

        dialog = QFileDialog()
        dialog.setWindowTitle(caption)
        dialog.setDirectory(initial_dir)
        dialog.setNameFilters(FILE_FILTERS)
        dialog.selectNameFilter(initial_filter)
        dialog.setFileMode(QFileDialog.FileMode.Directory)

        ok = dialog.exec()
        print("Result:", ok, dialog.selectedFiles(), dialog.selectedNameFilter(), )


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
