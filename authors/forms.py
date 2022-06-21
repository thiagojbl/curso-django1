from cProfile import label

from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'Username',
            'last_name': 'First name',
            'username': 'Last name',
            'email': 'E-mail',
            'password': 'Passwword',
        }
