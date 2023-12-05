from abc import ABC, abstractmethod
import wikipedia
from wikipedia.exceptions import PageError


class ContentPage(ABC):
    """Abstract class for retrieving content for chatbot."""

    @abstractmethod
    def set_wiki_content(self, topic: str = None):
        pass


class WikiContentPage(ContentPage):
    """Content from wikipedia pages."""

    _content = None

    def __init__(self, topic: str = None):
        if topic is not None:
            self.set_wiki_content(topic)

    @property
    def content(self):
        if self._content is None:
            raise AttributeError(
                "Content hasn't been set yet. Use .set_wiki_content() method."
            )
        return self._content

    @content.setter
    def content(self, text: str):
        if not isinstance(text, str) and text is not None:
            self._content = text
        else:
            raise ValueError(f'Content must be a string, not a {type(text)}')

    def set_wiki_content(self, topic: str = None):
        """Assign value to _content attribute."""

        if not isinstance(topic, str):
            raise ValueError(f'Content must be a string, '
                             f'not a {type(topic)} type.')

        try:
            self._content = wikipedia.page(topic).content
            return True
        except PageError:
            return False
