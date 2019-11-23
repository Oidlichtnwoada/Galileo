from util import Dictionary, Assistant


class Galileo:
    OPENING_QUESTION = 'Möchtest du eine Erklärung erhalten oder eine Erklärung eingeben?'
    INPUT_SEQ = 'eingeben'
    OUTPUT_SEQ = 'erhalten'
    APOLOGIZE_ANSWER = 'Tut mir leid, das kann ich noch nicht!'
    SUBJECT_QUESTION_OUTPUT = 'Bitte nenne das Thema, zu dem du eine Erklärung wünschst!'
    SUBJECT_QUESTION_INPUT = 'Bitte nenne das Thema, zu dem du eine Erklärung eingeben möchtest!'
    EXPLANATION_INPUT = 'Bitte sprich die Erklärung zu dem gewünschten Thema!'
    MISSING_SUBJECT = 'Für dieses Thema habe ich im Moment noch keinen Eintrag gespeichert!'
    THANK_YOU = 'Danke für deine Hilfe!'

    def __init__(self, lang='en'):
        self.assistant = Assistant(lang=lang)
        self.dictionary = Dictionary()

    def start_service(self):
        while True:
            if self.__class__.__name__.lower() in self.assistant.listen():
                self.assistant.speak(self.OPENING_QUESTION)
                answer = self.assistant.listen()
                if self.OUTPUT_SEQ in answer:
                    self.process_explanation()
                elif self.INPUT_SEQ in answer:
                    self.get_explanation()
                else:
                    self.assistant.speak(self.APOLOGIZE_ANSWER)

    def process_explanation(self):
        self.assistant.speak(self.SUBJECT_QUESTION_OUTPUT)
        answer = self.assistant.listen()
        for key in self.dictionary.get_dict():
            if key in answer:
                self.assistant.speak(self.dictionary.get_dict()[key])
                return
        self.assistant.speak(self.MISSING_SUBJECT)

    def get_explanation(self):
        self.assistant.speak(self.SUBJECT_QUESTION_INPUT)
        answer = self.assistant.listen()
        self.assistant.speak(self.EXPLANATION_INPUT)
        self.dictionary.add_value(answer, self.assistant.listen())
        self.assistant.speak(self.THANK_YOU)
