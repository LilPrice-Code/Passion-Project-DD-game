from rest_framework import routers
from .api import Char, GameMod, UserMod, MobMod


router = routers.DefaultRouter()
router.register('api/character',Char,'character')
router.register('api/gameModel',GameMod,'game')
router.register('api/user',UserMod,'user')
router.register('api/monster', MobMod,'Mob')

urlpatterns = router.urls