from rest_framework import viewsets, permissions
from DDGameApp.models import Character, GameModel, User, Monster
from .serializers import CharacterSer, GameSer, UserSer, MobSer

class Char(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = CharacterSer

class GameMod(viewsets.ModelViewSet):
    queryset = GameModel.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = GameSer


class UserMod(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = UserSer

class MobMod(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = MobSer