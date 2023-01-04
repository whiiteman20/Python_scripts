import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QWidgetAction


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Practice with Toolbars and Menus")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("Main toolbar")
        self.addToolBar(toolbar)

        button_action = QWidgetAction(self)
        button_action.setStatusTip("This is your button")

        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication()

window = MainWindow()
window.show()

app.exec()