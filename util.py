from json import loads, dump
from os import remove

from gtts import gTTS
from playsound import playsound
from speech_recognition import Recognizer, Microphone


class Assistant:
    def __init__(self, lang='en'):
        self.lang = lang

    def speak(self, text, filename='sound.mp3'):
        gTTS(text=text, lang=self.lang).save(filename)
        playsound(filename)
        remove(filename)

    def listen(self):
        recognizer = Recognizer()
        with Microphone() as source:
            return recognizer.recognize_google(recognizer.listen(source), language=self.lang)


class Dictionary:
    def __init__(self, dictionary_path='dictionary.json'):
        self.dictionary_path = dictionary_path

    def get_dict(self):
        with open(self.dictionary_path, 'r') as file:
            return loads(file.read())

    def save_dict(self, dictionary):
        with open(self.dictionary_path, 'w') as file:
            dump(dictionary, file)

    def add_value(self, key, value):
        dictionary = self.get_dict()
        dictionary[key] = value
        self.save_dict(dictionary)

    def remove_value(self, key):
        dictionary = self.get_dict()
        dictionary.pop(key, None)
        self.save_dict(dictionary)
