from rest_framework import routers
from .api import Char, GameMod, UserMod, MobMod, CityMod, PointMod


router = routers.DefaultRouter()
router.register('api/character',Char,'character')
router.register('api/gameModel',GameMod,'game')
router.register('api/user',UserMod,'user')
router.register('api/monster', MobMod,'Mob')
router.register('api/city', CityMod,'city')
router.register('api/point', PointMod,'point')

urlpatterns = router.urls