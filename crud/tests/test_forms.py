from crud.forms import BooksForm, RegisterForm
from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class BookFormsTest(TestCase):
    
    def setUp(self, *args, **kwargs) -> None:
        self.form_data = {
            'username': 'User',
            'password': 'pass1234',
            'email': 'email@gmail.com',
            'first_name': 'Fuser',
            'last_name': 'Luser',
            'password2': 'pass1234'
        }
        return super().setUp(*args, **kwargs)
    
    def test_clean_password(self):
        self.form_data['password'] = 'pass113'
        self.form_data['password2'] = 'pass113'
        url = reverse('crud:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Your pass need greater than 8 characters'
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_password_greater_than_7_characters(self):
        self.form_data['password2'] = 'passerror'
        url = reverse('crud:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'password fields not be equal'
        self.assertIn(msg, response.content.decode('utf-8'))
        
    def test_email_not_equal(self):
        url = reverse('crud:register_create')
        self.client.post(url, data=self.form_data, follow=True)
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'This email already exist'
        self.assertIn(msg, response.content.decode('utf-8'))