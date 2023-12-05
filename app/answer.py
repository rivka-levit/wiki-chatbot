"""
Answer Extractor class.
"""

import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from content import WikiContentPage


class AnswerExtractor:
    """Extract the most similar sentence as an answer of chatbot."""

    ltz = nltk.stem.WordNetLemmatizer()
    pos_tags = ('n', 'v', 'a', 'r', 's')

    def lemma_me(self, sent: str) -> list:
        """Return significant lemmas of a sentence."""

        tokens = nltk.word_tokenize(sent)
        tagged_tokens = nltk.pos_tag(tokens)
        lemmas = list()

        for token, tag in tagged_tokens:
            tag = tag[0].lower()
            if tag in self.pos_tags:
                lemma = self.ltz.lemmatize(token, tag)
                lemmas.append(lemma)

        return lemmas

    def get_answer(self, q: str) -> str | None:
        pass

