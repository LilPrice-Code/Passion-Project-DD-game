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

from .models import Character

class GameModel(models.Model):
    worldName = models.CharField(max_length = 100)
    body = models.TextField(max_length = 10000)
    pub_date = models.DateTimeField(default = timezone.now)
    foreign_user = models.ForeignKey(User, on_delete= models.CASCADE)
    active = models.CharField(max_length = 4, default = "no")
    display = models.CharField(max_length = 4, default = "no")
    picture = models.CharField(max_length = 10000)

from .models import GameModel

class City(models.Model):
    cityName = models.CharField(max_length =2000)
    xcord = models.IntegerField(default=25)
    ycord = models.IntegerField(default=25)
    foreign_Game = models.ForeignKey(GameModel, on_delete= models.CASCADE)

class Points(models.Model):
    pointName = models.CharField(max_length =2000)
    xcord = models.IntegerField(default=25)
    ycord = models.IntegerField(default=25)
    foreign_Game = models.ForeignKey(GameModel, on_delete= models.CASCADE)

from .models import City, Points

class Monster(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length =2000, default ="https://cdn.pixabay.com/photo/2013/07/12/15/05/dragon-149393_960_720.png")
    foreign_point = models.ForeignKey(Points, on_delete= models.CASCADE)
    health = models.IntegerField(default=10)
    baseHealth = models.IntegerField(default=10)
    defense = models.IntegerField(default=10)
    attack = models.IntegerField(default=10)
    dodge = models.IntegerField(default=100)
    critical = models.IntegerField(default=15)
    coins = models.IntegerField(default = 10)
    experience = models.IntegerField(default=500)




