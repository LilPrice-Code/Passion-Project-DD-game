from rest_framework import routers
from .api import Char, GameMod, UserMod, MobMod, CityMod


router = routers.DefaultRouter()
router.register('api/character',Char,'character')
router.register('api/gameModel',GameMod,'game')
router.register('api/user',UserMod,'user')
router.register('api/monster', MobMod,'Mob')
router.register('api/city', CityMod,'city')

urlpatterns = router.urls