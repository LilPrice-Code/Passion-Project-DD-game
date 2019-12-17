from django import forms
from .models import Character
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'password']

class CharacterForm(forms.ModelForm):
    class Meta():
        model = Character
        fields = ['name']

