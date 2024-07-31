from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import password_validation
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            },
        ),   
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
              'class': 'form-control',
              'id': 'password-input',  
            },
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    password_strength = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type')
        
class LogInForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),   
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
              'class': 'form-control',
              'id': 'password-input',  
            },
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    class Meta:
        model = CustomUser
        fields = ('username')