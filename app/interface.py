"""
Command Line Interface for chatbot.
"""

from content import WikiContentPage
from answer import AnswerExtractor


class WikiChatInterface:
    """Interface for chatbot."""

    page = WikiContentPage()
    respondent = AnswerExtractor()

    def chat(self):
        """Chat process."""

        print("Hi! I'm a wiki chatbot. A can answer your questions.")
        topic = input('What do you want to talk about?\n')

        while True:
            if topic == 'q':
                return

            if not self.page.set_wiki_content(topic):
                print("Oops! Wikipedia doesn't know anything about it.")
                topic = input("Do you want to talk about something else?\n")

            else:
                self.respondent.context = self.page.content
                break

        question = input("Ok! I'm ready to answer your questions. Ask me!\n")

        while True:
            if question == 'q':
                break

            output = self.respondent.get_answer(question)

            if not output:
                print("Oh... I don't know.")
            else:
                print(output)

            question = input("Another question?\n")
