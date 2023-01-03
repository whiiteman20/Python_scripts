import os
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QStatusBar, QToolBar, QCheckBox

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Practice with Icons")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("The Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon(os.path.join(basedir, 'Icons/fugue-icons-3.5.6/icons/animal-monkey.png')),
                                "Your Button", self)
        button_action.setStatusTip("This is your button")

        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        button_action_2 = QAction(QIcon(os.path.join(basedir, 'Icons/fugue-icons-3.5.6/icons/android.png')),
                                  "Your Button", self)
        button_action_2.setStatusTip("This is your button")

        button_action_2.triggered.connect(self.onMyToolBarButtonClick)
        button_action_2.setCheckable(True)
        toolbar.addAction(button_action_2)

        toolbar.addWidget(QLabel("Fuck me?"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print('click', s)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
