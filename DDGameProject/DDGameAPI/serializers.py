from rest_framework import serializers
from DDGameApp.models import Character, GameModel, User, Monster

class CharacterSer(serializers.ModelSerializer):
    class Meta():
        model = Character
        fields = "__all__"


class GameSer(serializers.ModelSerializer):
    class Meta():
        model = GameModel
        fields = "__all__"


class UserSer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = "__all__"


class MobSer(serializers.ModelSerializer):
    class Meta():
        model = Monster
        fields = "__all__"