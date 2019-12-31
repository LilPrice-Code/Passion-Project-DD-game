from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm, GameForm, CityForm, MobForm, PointForm
from .models import GameModel, City, Monster, Points


# Create your views here.
def index(request):
    users = request.user
    return render(request, 'DDGameApp/index.html', {'user': users })


def DDlogin(request):
    if request.method == "POST":
        person = UserForm(request.POST)
        if person.is_valid:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
    return render(request, 'DDGameApp/login.html', {'form': UserForm()})


def DDlogout(request):
    logout(request)
    return redirect('index')

def newplayer(request):
    people = User.objects.all()
    useray = []
    for x in people:
        useray.append(x.username)
    if request.method == 'POST':
        new = UserForm(request.POST)
        if new.is_valid:
            for x in useray:
                if x == request.POST['username']:
                    return render(request, 'DDGameApp/newuser.html', {'form': UserForm()})
            form = User.objects.create_user(username=request.POST['username'], email='', password=request.POST['password'])
            form.save()
            login(request, form)
            return redirect('index')
    return render(request, 'DDGameApp/newuser.html', {'form': UserForm()})

def overlord(request):
    return render(request, 'DDGameApp/overlord.html')

def player(request):
    return render(request, 'DDGameApp/player.html')

def board(request):
    return render(request, 'DDGameApp/board.html')

def create(request):
    if request.method == 'POST':
        new = GameForm(request.POST)
        if new.is_valid:
            form = GameModel.objects.create(worldName=request.POST['worldName'], body=request.POST['body'],  picture=request.POST['picture'], foreign_user = request.user)
            form.save()
            return redirect('view')
    return render(request, 'DDGameApp/create.html', {'form': GameForm()})

def viewset(request):
     return render(request, 'DDGameApp/viewsetup.html')

def mygame(request):
    long = GameModel.objects.filter(foreign_user = request.user)
    length = len(long)
    return render(request, 'DDGameApp/mygames.html',{'game': GameModel.objects.filter(foreign_user = request.user), 'length':length})

def preview(request, gmID):
    games = GameModel.objects.get(pk = gmID)
    city = City.objects.filter(foreign_Game=games)
    return render(request, 'DDGameApp/preview.html',{'game': games, 'city': city})

def editgame(request, gmID):
    games = GameModel.objects.get(pk = gmID)
    city = City.objects.filter(foreign_Game=games)
    point = Points.objects.filter(foreign_Game=games)
    if request.method == "POST":
        newgame = GameForm(request.POST or None , request.FILES, instance = games)
        if newgame.is_valid:
            newgame.save()
            return redirect('editgame', gmID)
    if request.method == 'POST':
           new = CityForm(request.POST)
           if new.is_valid:
               form = City.objects.create(cityName=request.POST['cityName'], xcord=request.POST['xcord'],  ycord=request.POST['ycord'], foreign_Game = games)
               form.save()
               return redirect('editgame', gmID)
#     if request.method == 'POST':
#               newpoint = PointForm(request.POST)
#               if newpoint.is_valid:
#                   formpoint = Points.objects.create(pointName=request.POST['pointName'], xcord=request.POST['xcord'],  ycord=request.POST['ycord'], foreign_Game = games)
#                   formpoint.save()
#                   return redirect('editgame', gmID)
    return render(request, 'DDGameApp/editgame.html',{'gmID': gmID, 'game': games, 'city': city , 'pointform': PointForm(), 'cityform': CityForm(), 'gameform': GameForm(instance=games)})

def editcity(request, gmID, cityID):
    games = GameModel.objects.get(pk = gmID)
    city = City.objects.filter(foreign_Game=games)
    cit = City.objects.get(pk=cityID)
    mobs = Mon
    if request.method == "POST":
        newcity = CityForm(request.POST or None , request.FILES, instance = cit)
        if newcity.is_valid:
            newcity.save()
            return redirect('editcity', gmID, cityID)
    if request.method == 'POST':
               new = MobForm(request.POST)
               if new.is_valid:
                   form = Monster.objects.create(name=request.POST['name'], foreign_point = games)
                   form.save()
                   return redirect('editcity', gmID, cityID)
    return render(request, 'DDGameApp/editcity.html',{'game': games, 'gmID': gmID, 'city': city ,'cityform': CityForm(instance=cit)})
