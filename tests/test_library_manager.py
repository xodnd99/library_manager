import unittest
from library_manager import add_book, delete_book, search_books, update_status, load_books, save_books

class TestLibraryManager(unittest.TestCase):
    def setUp(self):
        self.test_books = [
            {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949, "status": "available"},
            {"id": 2, "title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "status": "issued"},
        ]
        save_books(self.test_books)

    def test_add_book(self):
        add_book("Fahrenheit 451", "Ray Bradbury", 1953)
        books = load_books()
        self.assertEqual(len(books), 3)
        self.assertEqual(books[-1]["title"], "Fahrenheit 451")

    def test_delete_book(self):
        delete_book(1)
        books = load_books()
        self.assertEqual(len(books), 1)

    def test_search_books(self):
        results = search_books("1984")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "1984")

    def test_update_status(self):
        update_status(1, "issued")
        books = load_books()
        self.assertEqual(books[0]["status"], "issued")

    def tearDown(self):
        save_books([])

if __name__ == "__main__":
    unittest.main()
