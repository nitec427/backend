from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import RoomForm
from .models import Room, Topic, Message
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn something'},
    {'id': 2, 'name': 'Lets swim'},
    {'id': 3, 'name': 'Lets play'}
]


def home(req):
    q = req.GET.get('q') if req.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q))
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {
        "rooms": rooms, "topics": topics, "room_count": room_count
    }
    return render(req, 'base/home.html', context)


def room(req, pk):
    """ 
    user = models.ForeignKey(User, on_delete=CASCADE)
    room = models.ForeignKey(Room, on_delete=CASCADE)
    body = models.TextField()
    """
    room = Room.objects.get(id=pk)
    roommessages = room.message_set.all()

    if req.method == 'POST':
        message = Message.objects.create(
            user=req.user, room=room, body=req.POST.get('body'))
        return redirect("room", pk=room.id)
    context = {"room": room, "roommessages": roommessages}
    return render(req, 'base/room.html', context)


@login_required(login_url="/login")
def create_room(req):
    form = RoomForm()
    if req.method == 'POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(req, 'base/room_form.html', context)


@login_required(login_url="/login")
def update_room(req, pk):
    room = Room.objects.get(id=int(pk))
    form = RoomForm(instance=room)

    if req.user != room.host:
        return HttpResponse("You are not allowed here!")

    if req.method == 'POST':
        form = RoomForm(req.POST, instance=room)
        print("babantikem")
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form": form}
    return render(req, "base/room_form.html", context)


@login_required(login_url="/login")
def delete_room(req, pk):
    room = Room.objects.get(id=int(pk))
    if req.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj': room}
    return render(req, "base/deleteroom.html", context)


def logout_page(request):
    logout(request)
    return redirect('home')


def login_page(req):
    page = "login"
    if req.user.is_authenticated:
        return redirect("home")
    if req.method == 'POST':
        username = req.POST.get('username').lower()
        password = req.POST.get('password')
        try:
            user = User.objects.get(username=username)  # password=password
        except:
            messages.error(req, "User not found")
        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            return redirect('home')
        else:
            messages.error(req, "Either username or password is incorrect")
    context = {"page": page}
    return render(req, "base/login_register.html", context)


def register_page(req):
    page = "register"
    form = UserCreationForm()
    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(req, user)
        return redirect('home')
    else:
        messages.error(req, "Something went wrong during registration.")
    context = {"page": page, "form": form}
    return render(req, "base/login_register.html", context)
