from django import forms
from .models import Character, GameModel, City, Points, Item, ShopItem, Quest
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'password']

class CharacterForm(forms.ModelForm):
    class Meta():
        model = Character
        fields = ['name', "pictureURL"]

class GameForm(forms.ModelForm):
    class Meta():
        model = GameModel
        fields = ['worldName','body','picture']

class CityForm(forms.ModelForm):
    class Meta():
        model = City
        fields = ['cityName','xcord','ycord']

class PointForm(forms.ModelForm):
    class Meta():
        model = Points
        fields = ['pointName','xcord','ycord']

# class MobForm(forms.ModelForm):
#     class Meta():
#         model = Monster
#         fields = ['name']


class ItemForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = ['name']


class ShopForm(forms.ModelForm):
    class Meta():
        model = ShopItem
        fields = ['name', 'coins']

class QuestForm(forms.ModelForm):
    class Meta():
        model = Quest
        fields = ['name' , 'coins', 'experience']