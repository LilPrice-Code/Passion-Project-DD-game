from django.contrib import admin
from .models import  GameModel, Character


admin.site.register(GameModel)
# admin.site.register(Monster)
admin.site.register(Character)
