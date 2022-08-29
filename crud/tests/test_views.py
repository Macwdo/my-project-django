from crud.models import Book
from .test_book_data import BookTestCase


class ViewsTests(BookTestCase):
    def setUp(self) -> None:
        self.book = self.make_books()
        return super().setUp()
    
    
    def test_home_page_returns(self):
        book = self.book
        title = "Hello world"
        self.assertEqual(book.title, title)