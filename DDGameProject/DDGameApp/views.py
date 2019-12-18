from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm
# from .models import


# Create your views here.
def index(request):
#     oldwiki = WikiModel.objects.all()
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
                    return render(request, 'DDGameApp/newuser.html', {'form': UserForm(), 'hi': 'That username is taken. Please use another one.'})
            form = User.objects.create_user(username=request.POST['username'], email='', password=request.POST['password'])
            form.save()
            login(request, form)
            return redirect('index')
    return render(request, 'DDGameApp/newuser.html', {'form': UserForm(), 'hi': 'Please enter a username and password.'})

def overlord(request):
    return render(request, 'DDGameApp/overlord.html')
def player(request):
    return render(request, 'DDGameApp/player.html')

def board(request):
    return render(request, 'DDGameApp/board.html')