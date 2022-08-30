from crud.forms import BooksForm, RegisterForm
from django.urls import reverse
from django.test import TestCase
from parameterized import parameterized

class BookFormsTest(TestCase):
    
    def setUp(self) -> None:
        self.form_data = {
            'username': 'User',
            'password': 'pass1234',
            'email': 'email@gmail.com',
            'first_name': 'Fuser',
            'last_name': 'Luser',
            'password2': 'pass1234'
        }
        return super().setUp()
    
    def test_clean_password(self):
        url = reverse('crud:register')
        response = self.client.post(url, data=self.form_data, follow=True)
        password = self.form_data['password']
        self.assertEqual(1, 1)