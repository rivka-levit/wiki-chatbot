from abc import ABC, abstractmethod
import wikipedia


class ContentPage(ABC):
    """Abstract class for retrieving content for chatbot."""

    @abstractmethod
    def set_content(self, topic: str = None):
        pass


class WikiContentPage(ContentPage):
    """Content from wikipedia pages."""

    _content = None

    def __init__(self, topic: str = None):
        if topic is not None:
            self.set_content(topic)

    @property
    def content(self):
        if self._content is None:
            raise AttributeError(
                "Content hasn't been set yet. Use .set_content() method."
            )
        return self._content

    @content.setter
    def content(self, text: str):
        if isinstance(text, str):
            self._content = text
        else:
            raise ValueError(f'Content must be a string, not a {type(text)}')

    def set_content(self, topic: str = None):
        """Assign value to _content attribute."""

        if not isinstance(topic, str):
            raise ValueError(f'Content must be a string, '
                             f'not a {type(topic)} type.')

        self._content = wikipedia.page(topic).content
