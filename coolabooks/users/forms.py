from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# adds the email field to the default registration form

class RegisterForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']