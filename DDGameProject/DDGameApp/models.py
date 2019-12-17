from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length = 25)
    pictureURL = models.CharField(max_length = 200, default = "https://cdn.pixabay.com/photo/2014/04/03/00/38/shield-308943_960_720.png")
    player = models.ForeignKey(User, on_delete= models.CASCADE)
    classname = models.CharField(max_length = 25, default="none")
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    health = models.IntegerField(default=100)
    baseHealth = models.IntegerField(default=100)
    defense = models.IntegerField(default=10)
    attack = models.IntegerField(default=10)
    critical = models.IntegerField(default=15)
    dodge = models.IntegerField(default=10)
    coins = models.IntegerField(default = 100)
    def __str__(self):
            return self.name

from .models import Character

class GameModel(models.Model):
    worldName = models.CharField(max_length = 100)
    body = models.TextField(max_length = 10000)
    pub_date = models.DateTimeField(default = timezone.now)
    overload = models.ForeignKey(User, on_delete= models.CASCADE)
    active = models.CharField(max_length = 4, default = "no")
    player1 = models.ForeignKey(Character, on_delete=True, related_name="player1",  default=1)
    player2 = models.ForeignKey(Character, on_delete=True, related_name="player2",  default=1)
    player3 = models.ForeignKey(Character, on_delete=True, related_name="player3",  default=1)
    player4 = models.ForeignKey(Character, on_delete=True, related_name="player4",  default=1)
    player5 = models.ForeignKey(Character, on_delete=True, related_name="player5",  default=1)
    def __str__(self):
        return self.worldName

class Monster(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length =2000, default ="https://cdn.pixabay.com/photo/2013/07/12/15/05/dragon-149393_960_720.png")
    health = models.IntegerField(default=10)
    baseHealth = models.IntegerField(default=10)
    defense = models.IntegerField(default=10)
    attack = models.IntegerField(default=10)
    dodge = models.IntegerField(default=100)
    critical = models.IntegerField(default=15)
    coins = models.IntegerField(default = 10)
    experience = models.IntegerField(default=500)
    def __str__(self):
        return self.name


