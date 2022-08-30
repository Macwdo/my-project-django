from .test_book_data import BookTestCase
from crud.models import Book


class BookModelsTest(BookTestCase):    
    def setUp(self):
        self.book = self.make_books()
        return super().setUp()
    
    def test_str_show_return(self):
        book = self.book
        title = 'Book Title'
        self.assertEqual(book.__str__(), title)
