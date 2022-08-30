from django import forms
from .models import Book
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

def strong_password(password):
    regex = re.compile(r'^.{8,}$')
    if not regex.match(password):
        raise ValidationError(("Your pass need greater than 8 characters"), code='Invalid')

class BooksForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput())
    
    class Meta:
        model = Book
        fields = "__all__"
        
        
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),
        required=True,
        validators=[strong_password])
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={'required': 'this field not be empty'},
        help_text='This field must be equal password field')

    class Meta:        
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]
        
    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exist = User.objects.filter(email=email).exists()
        if exist:
            raise ValidationError(
                'This email already exist',
                code='invalid'
            )
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise ValidationError(
            {'password2': 'password fields not be equal'})
            
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    
        
        
        
        