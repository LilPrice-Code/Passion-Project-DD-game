from django.contrib import admin
from .models import Monster, GameModel, Character


admin.site.register(GameModel)
admin.site.register(Monster)
admin.site.register(Character)
