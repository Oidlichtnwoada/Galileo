from util import Dictionary, Assistant


class Galileo:
    def __init__(self, lang='en'):
        self.assistant = Assistant(lang=lang)
        self.dictionary = Dictionary()

    def start_service(self):
        while True:
            text = self.assistant.listen()
            self.assistant.speak(text)
