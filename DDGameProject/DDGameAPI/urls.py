from rest_framework import routers
from .api import Char, GameMod


router = routers.DefaultRouter()
router.register('api/character',Char,'character')
router.register('api/gameModel',GameMod,'game')

urlpatterns = router.urls