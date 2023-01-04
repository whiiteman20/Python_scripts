import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QWidgetAction, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Add Status Button Practice")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QWidgetAction(self)
        button_action.setText("Your button")
        button_action.setStatusTip("This is your button")

        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)
        # Below shows the button toggled when it is clicked and untoggled when clicked again
        button_action.setCheckable(True)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication()

window = MainWindow()
window.show()

app.exec()