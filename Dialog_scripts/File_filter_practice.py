import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QFileDialog,
                               QVBoxLayout, QWidget, QMessageBox)

FILE_FILTERS = [
    'Portable Network Graphics files (*.png)',
    'Text files (*.txt)',
    'Comma Separated Values (*.csv)',
    'All files (*)',
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Filter Practice")

        layout = QVBoxLayout()

        button1 = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)

        button2 = QPushButton("Open files")
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

    # Open one file, read the contents, print the contents in terminal
    def get_filename(self):
        initial_filter = FILE_FILTERS[3]
        filters = ';;'.join(FILE_FILTERS)
        print('Filters are: ', filters)
        print("Initial filter: ", initial_filter)

        filename, selected_filter = QFileDialog.getOpenFileName(self, filter=filters, )
        print("Result: ", filename, selected_filter)

        if filename:
            with open(filename, 'r') as file:
                file_contents = file.read()
                print(file_contents)

    # Open multiple files, read the contents, print the contents in terminal
    def get_filenames(self):
        caption = ''
        initial_dir = ''
        initial_filter = FILE_FILTERS[1]
        filters = ';;'.join(FILE_FILTERS)

        print("Filters are:", filters)
        print("Initial fitler:", initial_filter)

        filenames, selected_filter = QFileDialog.getOpenFileNames(self, caption=caption, dir=initial_dir,
                                                                  filter=filters,)
        print("Result:", filenames, selected_filter)

        for filename in filenames:
            with open(filename, 'r') as file:
                file_contents = file.read()
                print(file_contents)

    def get_save_filename(self):
        caption = ''
        initial_dir = ''
        initial_filter = FILE_FILTERS[2]
        filters = ';;'.join(FILE_FILTERS)

        print("Filters are:", filters)
        print("Initial filter:", initial_filter)

        filename, selected_filter = (QFileDialog.getSaveFileName(self, caption=caption, dir=initial_dir,
                                                                 filter=filters))
        print("Result:", filename, selected_filter)

        if filename:
            if os.path.exists(filename):
                # Existing file, ask the user for confirmation.
                write_confirmed = QMessageBox.question(self, "Overwrite file?", f"The file {filename} exists. Are you "
                                                                                f"want to overwrite it?",)
            else:
                # File does not exist, always-confirmed
                write_confirmed = True

            if write_confirmed:
                with open(filename, 'w') as file:
                    file_content = "Fuck yeah"
                    file.write(file_content)

    def get_folder(self):
        caption = "Select folder"
        initial_dir = ""

        dialog = QFileDialog()
        dialog.setWindowTitle(caption)
        dialog.setDirectory(initial_dir)
        dialog.setFileMode(QFileDialog.FileMode.Directory)

        ok = dialog.exec()
        print("Result:", ok, dialog.selectedFiles(), dialog.selectNameFilter(), )


app = QApplication()

window = MainWindow()
window.show()

app.exec()