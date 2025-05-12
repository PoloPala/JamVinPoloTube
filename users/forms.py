from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'age', 'password1', 'password2']
