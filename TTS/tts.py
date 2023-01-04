from gtts import gTTS
import os
mytext = open('/home/kendale/Desktop/Programming/TTS/readthis.txt','r').read().replace('\n',' ')
lang = 'en'

speak = gTTS(text=mytext, lang=lang, slow=False)

speak.save("read_textfile.mp3")

