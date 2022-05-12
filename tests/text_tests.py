import unittest
import sys

from Twitterbot.src import text


class TextTestCase(unittest.TestCase):

    def setUp(self):
        self.target = text.Text()

        #TODO: rewrite these to get books and chapter info in the setup, then make a large number of random calls from there
        # need to check weird stuff like that every legit chapter is hit (no off by one errors making 1:31 inaccessible or whatever)

    def test_get_passage_at_verse_level(self):
        result = self.target.get_passage(1, 1, 31, 48)
        self.assertTrue(result.Attribution() == 'Genesis 31:48-49')
        self.assertTrue('And Laban said, ' in result.Passage())

    def test_get_passage_at_chapter_level(self):
        result = self.target.get_passage(1, 8, 2, None)
        self.assertTrue('Ruth 2:' in result.Attribution())

    def test_get_passage_at_book_level(self):
        result = self.target.get_passage(2, 4, None, None)
        self.assertTrue(result.Book == 'John')

    def test_get_passage_at_testament_level(self):
        pass

    def test_get_passage_at_top_level(self):
        pass


if __name__ == '__main__':
    unittest.main()