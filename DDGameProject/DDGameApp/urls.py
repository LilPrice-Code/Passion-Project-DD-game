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
    path('createworld/', views.create, name = 'create'),
    path('createwarrior/', views.newwar, name = 'newwar'),
    path('view/', views.viewset, name = 'view'),
    path('mygames/', views.mygame, name = 'games'),
    path('mywarriors/', views.mywar, name = 'mywar'),
    path('preview/<int:gmID>/', views.preview, name = 'preview'),
    path('editgame/<int:gmID>/', views.editgame, name = 'editgame'),
    path('delgame/<int:gmID>/', views.delgame, name = 'delgame'),
    path('editwarrior/<int:gmID>/', views.editwar, name = 'editwar'),
    path('viewwarrior/<int:gmID>/', views.viewwar, name = 'viewwar'),
    path('delwar/<int:gmID>/', views.delwar, name = 'delwar'),
    path('addcity/<int:gmID>/', views.addcity, name = 'addcity'),
    path('addpoint/<int:gmID>/', views.addpoint, name = 'addpoint'),
    path('editcity/<int:gmID>/<int:cityID>', views.editcity, name = 'editcity'),
    path('delcity/<int:gmID>/<int:cityID>', views.delcity, name = 'delcity'),
    path('editpoint/<int:gmID>/<int:pointID>', views.editpoint, name = 'editpoint'),
    path('delpoint/<int:gmID>/<int:pointID>', views.delpoint, name = 'delpoint'),
#     path('addmonster/<int:gmID>/<int:pointID>', views.addmob, name = 'addmob'),

    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
