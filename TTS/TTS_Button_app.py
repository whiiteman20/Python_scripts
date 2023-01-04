import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout
import sys
from gtts import gTTS


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TTS Commands")

        button = QPushButton("Click this to make TTS mp3")

        button2 = QPushButton("Click this to listen to TTS mp3")

        button.clicked.connect(self.make_tts_mp3)

        button2.clicked.connect(self.read_to_me)

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(button2)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def make_tts_mp3(self):
        mytext = open('/home/kendale/Desktop/Programming/TTS/readthis.txt', 'r').read().replace('\n', ' ')
        lang = 'en'

        speak = gTTS(text=mytext, lang=lang, slow=False)

        speak.save("read_textfile.mp3")

        print("Completed")

    def read_to_me(self):
        os.system('open read_textfile.mp3')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()