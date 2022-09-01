from django.test import TestCase
from django.urls import reverse

from .test_book_data import BookTestCase


class BookViewTests(BookTestCase):
    def setUp(self, *args, **kwargs) -> None:
        return super().setUp(*args, **kwargs)

    def test_home_page_returns(self):
        book = self.make_books()
        title = "Book Title"
        self.assertEqual(book.title, title)

    def test_newbook_create_view_post(self):
        url = reverse('crud:createbook')
        response = self.client.post(url)
        self.assertRedirects(response, '/')

    def test_newbook_create_view_get(self):
        url = reverse('crud:createbook')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'crud/create_new_book.html')

    def test_bookpage_read_delete_view_get(self):
        self.make_books()
        url = reverse('crud:bookpage', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'crud/book.html')

    def test_bookpage_read_delete_view_post(self):
        self.make_books()
        url = reverse('crud:bookpage', kwargs={'id': 1})
        response = self.client.post(url)
        self.assertRedirects(response, '/')

    def test_book_update_get(self):
        self.make_books()
        url = reverse('crud:updatebook', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'crud/update_book.html')

    def test_book_update_post(self):
        book_data = self.book_data(self.make_books())

        url = reverse('crud:updatebook', kwargs={'id': 1})
        response = self.client.post(url, data=book_data)
        self.assertRedirects(response, '/')


class RegisterViewTest(TestCase):
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

    def test_register_create_get_mode(self):
        url = reverse('crud:register_create')
        response = self.client.get(url)
        self.assertRedirects(response, '/writer/register')

    def test_login_view_loads(self):
        url = reverse('crud:login')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'crud/login.html')

    def test_login_create_view_get_returns_404(self):
        url = reverse('crud:login_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_login_create_view_error_to_validate(self):
        self.form_data
        self.form_data.update({
            'password': ''
        })
        url = reverse('crud:login_create')
        msg = 'Error to validate'
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_login_create_view_Invalid_credential(self):
        self.form_data
        url = reverse('crud:login_create')
        msg = 'Invalid Credential'
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_author_created_can_login(self):
        url = reverse('crud:register_create')
        self.form_data
        self.form_data.update({
            'username': 'testuser',
            'password': 'danilo21',
            'password2': 'danilo21',
        })
        self.client.post(url, data=self.form_data, follow=True)
        send_response = self.client.post(
            reverse('crud:login_create'), data=self.form_data, follow=True)

        self.assertIn('You are logged in',
                      send_response.content.decode('utf-8'))

    def test_logout_view_get_mode(self):
        # The user need login login part /-----
        url = reverse('crud:register_create')
        self.form_data.update({
            'username': 'testuser',
            'password': 'danilo21',
            'password2': 'danilo21',
        })
        self.client.post(url, data=self.form_data, follow=True)
        self.client.post(reverse('crud:login_create'),
                         data=self.form_data, follow=True)
        self.client.login(username='testuser', password='danilo21')
        #------/
        url = reverse('crud:logout')
        response = self.client.get(url)
        self.assertRedirects(response, reverse('crud:home'))

    def test_logout_view_post_mode_user_correctly_loged(self):
        url = reverse('crud:register_create')
        self.form_data.update({
            'username': 'testuser',
            'password': 'danilo21',
            'password2': 'danilo21',
        })
        self.client.post(url, data=self.form_data, follow=True)
        self.client.post(reverse('crud:login_create'),
                         data=self.form_data, follow=True)
        self.client.login(username='testuser', password='danilo21')
        #------/
        url = reverse('crud:logout')
        response = self.client.post(url,data={'username':'testuser'})
        self.assertRedirects(response, reverse('crud:home'))
        
    def test_logout_view_get_mode(self):
        # The user need login login part /-----
        url = reverse('crud:register_create')
        self.form_data.update({
            'username': 'testuser',
            'password': 'danilo21',
            'password2': 'danilo21',
        })
        self.client.post(url, data=self.form_data, follow=True)
        self.client.post(reverse('crud:login_create'),
                         data=self.form_data, follow=True)
        self.client.login(username='testuser', password='danilo21')
        #------/
        url = reverse('crud:logout')
        response = self.client.get(url)
        self.assertRedirects(response, reverse('crud:home'))

    def test_logout_view_post_mode_wrong_user(self):
        url = reverse('crud:register_create')
        self.form_data.update({
            'username': 'testuser',
            'password': 'danilo21',
            'password2': 'danilo21',
        })
        self.client.post(url, data=self.form_data, follow=True)
        self.client.post(reverse('crud:login_create'),
                         data=self.form_data, follow=True)
        self.client.login(username='testuser', password='asdalo21')
        #------/
        url = reverse('crud:logout')
        response = self.client.post(url,data={'username':'otheruser'})
        self.assertRedirects(response, reverse('crud:home'))
