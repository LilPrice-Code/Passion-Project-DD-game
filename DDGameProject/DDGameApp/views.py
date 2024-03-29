from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm, GameForm, CityForm, PointForm, ItemForm, CharacterForm
from .models import GameModel, City, Points, Item, Character


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
            return redirect('games')
    return render(request, 'DDGameApp/create.html', {'form': GameForm()})

def newwar(request):
    if request.method == 'POST':
        new = CharacterForm(request.POST)
        if new.is_valid:
            form =  Character.objects.create(name=request.POST['name'],  pictureURL=request.POST['pictureURL'], player = request.user)
            form.save()
            return redirect('mywar')
    return render(request, 'DDGameApp/createwarrior.html', {'form': CharacterForm()})

def viewset(request):
     return render(request, 'DDGameApp/viewsetup.html')

def mygame(request):
    long = GameModel.objects.filter(foreign_user = request.user)
    length = len(long)
    return render(request, 'DDGameApp/mygames.html',{'game': GameModel.objects.filter(foreign_user = request.user), 'length':length})

def mywar(request):
    long = Character.objects.filter(player = request.user)
    length = len(long)
    return render(request, 'DDGameApp/mywarrior.html',{'war': Character.objects.filter(player = request.user), 'length':length})

def delgame(request, gmID):
    games = GameModel.objects.get(pk = gmID)
    games.delete()
    return redirect('games')

def delwar(request, gmID):
    games = Character.objects.get(pk = gmID)
    games.delete()
    return redirect('mywar')

def preview(request, gmID):
    games = GameModel.objects.get(pk = gmID)
    city = City.objects.filter(foreign_Game=games)
    point = Points.objects.filter(foreign_Game=games)
    return render(request, 'DDGameApp/preview.html',{'game': games, 'city': city, 'point': point})

def editgame(request, gmID):
    games = GameModel.objects.get(pk = gmID)
    city = City.objects.filter(foreign_Game=games)
    point = Points.objects.filter(foreign_Game=games)
    if request.method == "POST":
        newgame = GameForm(request.POST or None , request.FILES, instance = games)
        if newgame.is_valid:
            newgame.save()
            return redirect('editgame', gmID)
#     if request.method == 'POST':
#            new = CityForm(request.POST)
#            if new.is_valid():
#                form = City.objects.create(cityName=request.POST['cityName'], xcord=request.POST['xcord'],  ycord=request.POST['ycord'], foreign_Game = games)
#                form.save()
#                return redirect('editgame', gmID)
#     if request.method == 'POST':
#               newpoint = PointForm(request.POST)
#               if newpoint.is_valid():
#                   formpoint = Points.objects.create(pointName=request.POST['pointName'], xcord=request.POST['xcord'],  ycord=request.POST['ycord'], foreign_Game = games)
#                   formpoint.save()
#                   return redirect('editgame', gmID)
    return render(request, 'DDGameApp/editgame.html',{'gmID': gmID, 'point': point, 'game': games, 'city': city , 'pointform': PointForm(), 'cityform': CityForm(), 'gameform': GameForm(instance=games)})

def editwar(request, gmID):
    war = Character.objects.get(pk=gmID)
    if request.method == "POST":
        newwar = CharacterForm(request.POST or None , request.FILES, instance = war)
        if newwar.is_valid:
            newwar.save()
            return redirect('editwar', gmID)
    return render(request, 'DDGameApp/editwarrior.html',{'gmID': gmID, 'war':war ,'warform': CharacterForm(instance=war)})

def viewwar(request, gmID):
    war = Character.objects.get(pk=gmID)
    return render(request, 'DDGameApp/viewwarrior.html',{'war':war})


def addcity(request, gmID):
    games = GameModel.objects.get(pk = gmID)
    city = City.objects.filter(foreign_Game=games)
    citylength= len(city)
    point = Points.objects.filter(foreign_Game=games)
    if request.method == 'POST':
        new = CityForm(request.POST)
        if new.is_valid():
            form = City.objects.create(cityName=request.POST['cityName'], xcord=request.POST['xcord'],  ycord=request.POST['ycord'], foreign_Game = games)
            form.save()
            return redirect('addcity', gmID)
    return render(request, 'DDGameApp/addcity.html',{'gmID': gmID, 'point': point, 'game': games, 'city': city, 'citylength': citylength, 'pointform': PointForm(), 'cityform': CityForm(), 'gameform': GameForm(instance=games)})

def addpoint(request, gmID):
    games = GameModel.objects.get(pk = gmID)
    city = City.objects.filter(foreign_Game=games)
    point = Points.objects.filter(foreign_Game=games)
    pointlength= len(point)
    if request.method == 'POST':
        newpoint = PointForm(request.POST)
        if newpoint.is_valid():
            formpoint = Points.objects.create(pointName=request.POST['pointName'], xcord=request.POST['xcord'],  ycord=request.POST['ycord'], foreign_Game = games)
            formpoint.save()
            return redirect('addpoint', gmID)
    return render(request, 'DDGameApp/addpoint.html',{'gmID': gmID, 'point': point, 'game': games, 'city': city , 'pointlength': pointlength, 'pointform': PointForm(), 'cityform': CityForm(), 'gameform': GameForm(instance=games)})


def editcity(request, gmID, cityID):
    games = GameModel.objects.get(pk = gmID)
    city = City.objects.filter(foreign_Game=games)
    cit = City.objects.get(pk=cityID)
    if request.method == "POST":
        newcity = CityForm(request.POST or None , request.FILES, instance = cit)
        if newcity.is_valid:
            newcity.save()
            return redirect('editcity', gmID, cityID)
#     if request.method == 'POST':
#                new = MobForm(request.POST)
#                if new.is_valid:
#                    form = Monster.objects.create(name=request.POST['name'], foreign_point = games)
#                    form.save()
#                    return redirect('editcity', gmID, cityID)
    return render(request, 'DDGameApp/editcity.html',{'game': games, 'gmID': gmID, 'cityID':cityID, 'city': city ,'cityform': CityForm(instance=cit)})


def editpoint(request, gmID, pointID):
    games = GameModel.objects.get(pk = gmID)
    city = City.objects.filter(foreign_Game=games)
    point = Points.objects.filter(foreign_Game=games)
    pnt = Points.objects.get(pk=pointID)
#     mob = Monster.objects.filter(foreign_point=point)
    if request.method == "POST":
        newpoint = PointForm(request.POST or None , request.FILES, instance = pnt)
        if newpoint.is_valid:
            newpoint.save()
            return redirect('editpoint', gmID, pointID)
#     if request.method == 'POST':
#                new = MobForm(request.POST)
#                if new.is_valid:
#                    form = Monster.objects.create(name=request.POST['name'], foreign_point = games)
#                    form.save()
#                    return redirect('editcity', gmID, cityID)
    return render(request, 'DDGameApp/editpoint.html',{'game': games, 'gmID': gmID, 'pointID': pointID , 'city': city , 'point': point, 'pointform': PointForm(instance=pnt)})

def delcity(request, gmID, cityID):
    city = City.objects.get(pk = cityID)
    city.delete()
    return redirect('addcity', gmID)

def delpoint(request, gmID, pointID):
    point = Points.objects.get(pk = pointID)
    point.delete()
    return redirect('addpoint', gmID)

# def addmob(request, gmID, pointID):
#     games = GameModel.objects.get(pk = gmID)
#     city = City.objects.filter(foreign_Game=games)
#     point = Points.objects.filter(foreign_Game=games)
#     pnt = Points.objects.get(pk=pointID)
#     mob = Monster.objects.filter(foreign_point=pnt)
#     if request.method == 'POST':
#         new = MobForm(request.POST)
#         if new.is_valid:
#             form = Monster.objects.create(name=request.POST['name'], foreign_point = pnt)
#             form.save()
#             return redirect('addmob', gmID, pointID)
#     return render(request, 'DDGameApp/addmonster.html',{'game': games, 'gmID': gmID, 'pointID': pointID , 'city': city , 'point': point, 'mobform': MobForm()})
