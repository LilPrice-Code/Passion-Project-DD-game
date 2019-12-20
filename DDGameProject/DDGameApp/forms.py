from django import forms
from .models import Character, GameModel
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'password']

class CharacterForm(forms.ModelForm):
    class Meta():
        model = Character
        fields = ['name']

class GameForm(forms.ModelForm):
    class Meta():
        model = GameModel
        fields = ['worldName','body','picture']
