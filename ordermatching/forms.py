from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=20)


    class Meta:
	    model = User
	    fields = ["username", "username", "password1", "password2"]