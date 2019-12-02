from wikipedia import *

from util import Dictionary, Assistant


class Galileo:

    def __init__(self):
        self.assistant = Assistant(lang='de')
        self.dictionary = Dictionary()
        set_lang('de')

    def start_service(self):
        while True:
            if "galileo" in self.assistant.listen():
                self.assistant.speak('Hallo, möchtest du eine Erklärung erhalten oder eine Erklärung eingeben?')
                answer = self.assistant.listen()
                if not self.check_answer(answer):
                    continue
                if 'erhalten' in answer:
                    self.process_explanation()
                elif 'eingeben' in answer:
                    self.get_explanation()
                else:
                    self.assistant.speak('Tut mir leid, das kann ich noch nicht!')

    def process_explanation(self):
        self.assistant.speak("Gib bitte ein Thema an!")
        answer = self.assistant.listen()
        if not self.check_answer(answer):
            return
        for topic in self.dictionary.get_dict():
            if topic in answer:
                self.assistant.speak(
                    f'Die Erklärung zu dem Thema {topic} lautet: {self.dictionary.get_dict()[topic]}!')
                return
        try:
            self.assistant.speak(page(search(answer)[0]).summary.split('\n')[0])
        except (IndexError | PageError):
            self.assistant.speak(
                f'Zu diesem Thema wurde noch keine Erklärung eingegeben, deshalb kann ich dir leider nicht helfen.')

    def get_explanation(self):
        self.assistant.speak('Wie lautet dein Thema?')
        first_answer = self.assistant.listen()
        if not self.check_answer(first_answer):
            return
        self.assistant.speak('Gib die Erklärung zum entsprechenden Thema ein!')
        second_answer = self.assistant.listen()
        if not self.check_answer(second_answer):
            return
        self.assistant.speak(
            f'Deine Erklärung für das Thema {first_answer} war {second_answer}! Ist das für dich in Ordnung?')
        third_answer = self.assistant.listen()
        if not self.check_answer(third_answer):
            return
        if 'ja' in third_answer:
            self.dictionary.add_value(first_answer, second_answer)
            self.assistant.speak('Danke, die anderen Kinder werden sich freuen!')
        else:
            self.assistant.speak('Ok, dann breche ich den aktuellen Vorgang ab!')

    def check_answer(self, answer):
        if answer == '':
            self.assistant.speak('Da du nicht mehr mit mir geredet hast, breche ich den aktuellen Vorgang ab!')
            return False
        else:
            return True
