from rest_framework import serializers
from DDGameApp.models import Character, GameModel

class CharacterSer(serializers.ModelSerializer):
    class Meta():
        model = Character
        fields = "__all__"


class GameSer(serializers.ModelSerializer):
    class Meta():
        model = GameModel
        fields = "__all__"