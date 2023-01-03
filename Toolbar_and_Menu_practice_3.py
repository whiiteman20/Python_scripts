import sys
import os
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QWidget, QCheckBox, QStatusBar
from PySide6.QtGui import QAction, QIcon

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon(os.path.join(basedir, "Icons/fugue-icons-3.5.6/icons/animal-penguin.png")),
                                "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)

        toolbar.addAction(button_action)
        toolbar.addSeparator()

        button_action2 = QAction(QIcon(os.path.join(basedir, "Icons/fugue-icons-3.5.6/icons/animal-penguin.png")),
                                 "Your button", self)
        button_action2.setStatusTip("This is your second button")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)

        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Fuck me?"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("Click!", s)


app = QApplication()

window = MainWindow()
window.show()

app.exec()