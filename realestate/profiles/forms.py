from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Enter first name")
    last_name = forms.CharField(max_length=30, required=False, help_text="Enter last name")
    email = forms.EmailField(max_length=254, help_text="Required. Enter email address")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
