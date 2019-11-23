from json import loads, dump, JSONDecodeError
from os import remove

from gtts import gTTS, gTTSError
from playsound import playsound
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError


class Assistant:
    def __init__(self, lang='en'):
        self.lang = lang

    def speak(self, text, filename='sound.mp3'):
        try:
            gTTS(text=text, lang=self.lang).save(filename)
            playsound(filename)
            remove(filename)
        except gTTSError:
            pass

    def listen(self):
        try:
            with Microphone() as source:
                recognizer = Recognizer()
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                return recognizer.recognize_google(audio, language=self.lang)
        except (UnknownValueError, RequestError):
            return ''


class Dictionary:
    def __init__(self, dictionary_path='dictionary.json'):
        self.dictionary_path = dictionary_path
        try:
            self.get_dict()
        except JSONDecodeError:
            self.save_dict({})

    def get_dict(self):
        with open(self.dictionary_path, 'r+') as file:
            return loads(file.read())

    def save_dict(self, dictionary):
        with open(self.dictionary_path, 'w+') as file:
            dump(dictionary, file)

    def add_value(self, key, value):
        dictionary = self.get_dict()
        dictionary[key] = value
        self.save_dict(dictionary)

    def remove_value(self, key):
        dictionary = self.get_dict()
        dictionary.pop(key, None)
        self.save_dict(dictionary)
