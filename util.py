from playsound import *
from speech_recognition import *
from gtts import *

def speak(text='', lang='en', filename='soundfile'):
    gTTS(text=text, lang=lang).save(filename)
    playsound(filename)

def listen():
    with Microphone() as source:
        recognizer = Recognizer()
        return recognizer.recognize_google(recognizer.listen(source))
