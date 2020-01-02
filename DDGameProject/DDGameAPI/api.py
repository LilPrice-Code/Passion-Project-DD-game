from rest_framework import viewsets, permissions
from DDGameApp.models import Character, GameModel, User, Monster, City, Points
from .serializers import CharacterSer, GameSer, UserSer, MobSer, CitySer, PointSer

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

class CityMod(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = CitySer

class PointMod(viewsets.ModelViewSet):
    queryset = Points.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = PointSer