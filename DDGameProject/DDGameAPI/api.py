from rest_framework import viewsets, permissions
from DDGameApp.models import Character, GameModel
from .serializers import CharacterSer, GameSer

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