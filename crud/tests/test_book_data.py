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
    