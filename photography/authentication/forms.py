from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from django import forms # type: ignore

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'password1', 'placeholder': 'Enter password here'}))
    password2 = forms.CharField(
        label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class': 'password2', 'placeholder': 'Enter confirm password here'}))
    
    class Meta:
        model= User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'usename':'Username', 'first_name': 'First Name', 'last_name':'Last Name', 'email':'Email Address'}

        widgets = {
            'username': forms.TextInput(attrs={'class': 'username', 'placeholder': 'Enter username here'}),
            'first_name': forms.TextInput(attrs={'class': 'first_name', 'placeholder': 'Enter first name here'}),
            'last_name': forms.TextInput(attrs={'class': 'last_name', 'placeholder': 'Enter last name here'}),
            'email': forms.EmailInput(attrs={'class': 'email', 'placeholder': 'Enter email here'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'username', 'placeholder': 'Enter username here'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Enter password here'})
    )