"""
Answer Extractor class.
"""

import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class AnswerExtractor:
    """Extract the most similar sentence as an answer of chatbot."""

    ltz = nltk.stem.WordNetLemmatizer()
    pos_tags = ('n', 'v', 'a', 'r', 's')
    _context = None
    _tokens = None

    def __init__(self, context: str = None):
        self.context = context

    @property
    def context(self):
        if self._context is None:
            raise AttributeError(
                "Context hasn't been set yet. Assign value to the context."
            )
        return self._context

    @context.setter
    def context(self, value):
        if not isinstance(value, str) and value is not None:
            raise ValueError(f'Context must be a string, not a {type(value)} '
                             f'type.')
        self._context = value
        self._tokens = None

    def lemma_me(self, sent: str) -> list:
        """Return significant lemmas of a sentence."""

        sent_tokens = nltk.word_tokenize(sent)
        tagged_tokens = nltk.pos_tag(sent_tokens)
        lemmas = list()

        for token, tag in tagged_tokens:
            tag = tag[0].lower()
            if tag in self.pos_tags:
                lemma = self.ltz.lemmatize(token, tag)
                lemmas.append(lemma)

        return lemmas

    def get_answer(self, q: str) -> str | None:
        """Return the most similar sentence from the context."""

        if self._tokens is None:
            self._tokens = nltk.sent_tokenize(self.context)

        sentence_tokens = self._tokens + [q]

        tv = TfidfVectorizer(tokenizer=self.lemma_me, token_pattern=None)
        tf = tv.fit_transform(sentence_tokens)

        values = cosine_similarity(tf[-1], tf)
        index = values.argsort()[0][-2]

        values_flat = sorted(values.flatten())
        coeff = values_flat[-2]

        if coeff > 0.3:
            return sentence_tokens[index]

        return None
