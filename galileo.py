from time import sleep

from util import Dictionary, Assistant


class Galileo:
    def __init__(self, lang='en'):
        self.assistant = Assistant(lang=lang)
        self.dictionary = Dictionary()

    def start_service(self):
        while True:
            self.assistant.speak('Galileo ist einsatzbereit!')
            sleep(1)
