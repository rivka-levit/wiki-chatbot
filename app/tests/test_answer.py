from unittest import TestCase

from answer import AnswerExtractor


class AnswerTests(TestCase):
    """Tests for Answer Extractor."""

    def setUp(self):
        self.text = ('Python is a high-level, general-purpose programming '
                     'language. Its design philosophy emphasizes code '
                     'readability with the use of significant indentation. '
                     'Python is dynamically typed and garbage-collected. It '
                     'supports multiple programming paradigms, including '
                     'structured (particularly procedural), object-oriented '
                     'and functional programming. It is often described as a '
                     '"batteries included" language due to its comprehensive '
                     'standard library.')

        self.extractor = AnswerExtractor(self.text)

    def test_get_lemmas(self):
        """Test extracting lemmas of a sentence."""

        question = 'What is Python'
        lemmas = self.extractor.lemma_me(question)

        self.assertIsInstance(lemmas, list)
        self.assertEqual(len(lemmas), 2)

    def test_get_answer(self):
        """Test extracting the most similar sentence."""

        question = 'What language is Python?'
        expected = ('Python is a high-level, general-purpose programming '
                    'language.')
        answer = self.extractor.get_answer(question)

        self.assertEqual(expected, answer)
