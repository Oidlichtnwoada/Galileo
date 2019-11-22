from util import Dictionary, Assistant


class Galileo:
    def __init__(self, lang='en'):
        self.assistant = Assistant(lang=lang)
        self.dictionary = Dictionary()

    def start_service(self):
        self.assistant.speak('Galileo hat gestartet')
        self.assistant.speak(f'Du hast {self.assistant.listen()} gesagt')
