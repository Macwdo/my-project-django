from django.test import TestCase
from crud.models import Book


class BookTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def make_books(
        self,
        title="Book Title",
        description="Book description",
        pages=1,
        price=1,
        language="PT",
        created_at=None
        ):
        return Book.objects.create(
            title=title,
            description=description,
            pages=pages,
            price=price,
            language=language,
            created_at=created_at
            )
        
        
    def book_data(self,book):
        data = {
            "title": book.title,
            "description": book.description,
            "pages": book.pages,
            "price": book.price,
            "language": book.language,
            "created_at": book.created_at 
        }
        return data
        