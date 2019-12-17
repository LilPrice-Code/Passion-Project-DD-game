from django import forms
# from .models import WikiModel, WikiRelated
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'password']
