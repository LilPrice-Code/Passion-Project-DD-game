from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from DDGameApp import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signin/', views.DDlogin, name = 'login'),
    path('signout/', views.DDlogout, name = 'logout'),
    path('signup/', views.newplayer, name = 'newuser'),
    path('overlord/', views.overlord, name = 'overlord'),
    path('player/', views.player, name = 'player'),
    path('gameboard/', views.board, name = 'board'),
    path('create/', views.create, name = 'create'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
