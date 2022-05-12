import random
import re
import textwrap
from dataclasses import dataclass

from hodgeys_kjv_db import KJV


class Text:
    def __init__(self):
        self.kjv = KJV()
        self.books = self.kjv.fetch_books()

    def get_passage(self, testament:int, book:int, chapter:int, verse:int):
        '''
        Gets a passage per the inputs; or, from smallest to largest, the inputs can be 0,
        in which case the value is selected at random.  The randomness is not uniform;
        first the book, from which the chapter, from which the verse, is chosen uniformly.
        '''

        if verse:
            return self._get_verse(testament, book, chapter, verse)
        
        if chapter:
            return self._get_random_verse_in_chapter(testament, book, chapter)

        if book:
            return self._get_random_verse_in_book(testament, book)

        if testament:
            return self._get_random_verse_in_testament(testament)

        return self._get_random_verse()

    def _get_verse(self, testament, book, chapter, verse):
        p = self.kjv.fetch_passage(testament, book, chapter, verse)
        return Passage([b.ShortName for b in self.books if b.Book == book and b.Testament == testament][0], p.Attribution, p.Passage1, p.Passage2)

    def _get_random_verse_in_chapter(self, testament, book, chapter):
        chapter_length = self.kjv.fetch_chapters(testament, book)[chapter]
        random_verse = random.randint(1, chapter_length)

        return self._get_verse(testament, book, chapter, random_verse)

    def _get_random_verse_in_book(self, testament, book):
        chapters = self.kjv.fetch_chapters(testament, book)
        random_chapter_index, chapter_length = random.choice(list(chapters.items()))
        random_verse = random.randint(1, chapter_length)

        return self._get_verse(testament, book, random_chapter_index, random_verse)

    def _get_random_verse_in_testament(self, testament):
        book = self._get_random_book(testament)[1]
        chapters = self.kjv.fetch_chapters(testament, book)
        random_chapter_index, chapter_length = random.choice(list(chapters.items()))
        random_verse = random.randint(1, chapter_length)

        return self._get_verse(testament, book, random_chapter_index, random_verse)

    def _get_random_verse(self):
        testament, book = self._get_random_book(None)
        chapters = self.kjv.fetch_chapters(testament, book)
        random_chapter_index, chapter_length = random.choice(list(chapters.items()))
        random_verse = random.randint(1, chapter_length)

        return self._get_verse(testament, book, random_chapter_index, random_verse)

    def _get_random_book(self, testament):
        if testament:
            random_book = random.choice([book for book in self.books if book.Testament == testament])
        else:
            random_book = random.choice(self.books)
            
        return random_book.Testament, random_book.Book

@dataclass
class Passage:
    Book: str
    _Attribution: str
    _Passage1: str
    _Passage2: str

    def Attribution(self):
        return self.Book + ' ' + self._Attribution

    def Passage(self, width=50):
        newline = '\n'
        clean1 = re.sub('[0-9]{1,3}:[0-9]{1,3} ?', '', self._Passage1)
        joined1 = ''.join(x + newline for x in textwrap.wrap(clean1, width))

        if len(self._Passage2) > 0:
            clean2 = re.sub('[0-9]{1,3}:[0-9]{1,3} ?', '', self._Passage2)
            joined2 = ''.join(x + newline for x in textwrap.wrap(clean2, width))

            return (joined1 + newline + joined2).rstrip(newline)
        else:
            return joined1.rstrip(newline)
