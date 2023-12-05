from unittest import TestCase

from content import WikiContentPage


class WikiContentTests(TestCase):
    """Tests for content from Wikipedia."""

    def setUp(self):
        self.page = WikiContentPage('September')

    def test_retrieve_content_from_wiki(self):
        """Test retrieving text of wikipedia article."""

        self.assertIsInstance(self.page.content, str)
        self.assertIn('September', self.page.content)

    def test_change_topic_get_content(self):
        """Test retrieving content after changing a topic."""

        self.page.set_content('Vegetables')
        self.assertIn('Vegetables', self.page.content)
