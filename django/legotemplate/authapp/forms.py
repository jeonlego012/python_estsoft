from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from django import forms

from .models import User

class UserLoginModelForm(ModelForm):
    class Meta:
        model = User

        fields = ['username', 'password']

        widgets = {
            'username': TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Please enter you username',
                },
            ),
            'password': PasswordInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '******',
                },
            ),
        }
        
class UserRegisterForm(forms.Form):
    email = forms.CharField(
        label = 'Email',
        max_length=150,
        required = True,
        widget = EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Please enter you valid email address',
            },
        ),
    )
    username = forms.CharField(
        label = 'Username',
        max_length=150,
        required = True,
        widget = TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Please enter your username',
            },
        ),
    )
    password = forms.CharField(
        label = 'Password',
        max_length=150,
        required = True,
        widget = PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '8~12 characters',
            },
        ),
    )
    password2 = forms.CharField(
        label = 'Repeat Password',
        max_length=150,
        required = True,
        widget = PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Please repeat your pasword',
            },
        ),
    )
    
'''
class UserRegisterModelForm(ModelForm):
    class Meta:
        model = User
        
        fields = ['email', 'username', 'password', 'password2']
        
        labels = {
            'password2': 'Repeat Password'
        }
        
        widgets = {
            'email': EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Please enter you valid email address',
                },
            ),
            'username': TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Please enter you username',
                },
            ),
            'password': PasswordInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '8~12 characters',
                },
            ),
            'password2': PasswordInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Please repeat your pasword',
                },
            ),
        }
'''

class UserChangePasswordForm(forms.Form):
    
    email = forms.CharField(
        label = 'Email',
        max_length=150,
        required = True,
        widget = EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Please enter your email address you registered',
            },
        ),
    )
    password = forms.CharField(
        label = 'Password',
        max_length=150,
        required = True,
        widget = PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '8~12 characters',
            },
        ),
    )
    password2 = forms.CharField(
        label = 'Repeat Password',
        max_length=150,
        required = True,
        widget = PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Please repeat your pasword',
            },
        ),
    )