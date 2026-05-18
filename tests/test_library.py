import unittest
from models.book import Book

class TestLibrary(unittest.TestCase):

    def test_book_available(self):
        book = Book("Test", "1234567890123", "A", 2020, 1)
        self.assertTrue(book.is_available())

    def test_book_unavailable(self):
        book = Book("Test", "1234567890123", "A", 2020, 0)
        self.assertFalse(book.is_available())

if __name__ == "__main__":
    unittest.main()