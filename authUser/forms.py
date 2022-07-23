from django import forms
from .models import Member
from django.contrib.auth.forms import UserCreationForm


class signUpForm(UserCreationForm):

    class Meta:
        model = Member
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
