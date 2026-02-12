
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse

from django.db.models import Q

from .models import *
from .serializers import *
from .forms import *


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist') 
    context = {'page':page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during register')

    return render(request, 'base/login_register.html', {'form':form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    salas = Sala.objects.filter(
        Q(topico__nome__icontains=q) |
        Q(nome__icontains=q) |
        Q(descricao__icontains=q) 
        )
    
    topicos = Topico.objects.order_by('nome')
    
    sala_count = salas.count()

    sala_mensagens = Mensagem.objects.filter(Q(sala__topico__nome__icontains=q))
    
    context={'salas':salas, 'topicos':topicos, 'sala_count':sala_count, 'sala_mensagens':sala_mensagens}
    return render(request, 'base/home.html', context)


def room(request, pk):
    sala = Sala.objects.get(id=pk)
    sala_messages = sala.mensagem_set.all()
    participantes = sala.participantes.all()

    if request.method == "POST":
        mensagem = Mensagem.objects.create(
            usuario = request.user,
            sala = sala,
            corpo=request.POST.get('corpo')
        )
        sala.participantes.add(request.user)
        return redirect('room', pk=sala.id)

    context={'sala':sala, 'mensagens': sala_messages, 'participantes':participantes}
    return render(request, 'base/room.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    salas = user.sala_set.all()
    sala_mensagens = user.mensagem_set.all()
    topicos = Topico.objects.all()
    context={'user':user, 'salas':salas, 'sala_mensagens':sala_mensagens, 'topicos':topicos}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = SalaForm()
    topicos = Topico.objects.all()
    if request.method == 'POST':
        topico_nome = request.POST.get('topico').lower()
        topico, created = Topico.objects.get_or_create(nome=topico_nome)

        Sala.objects.create(
            host=request.user,
            topico=topico,
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao'),
        )
        return redirect('home')

    context = {'form': form, 'topicos': topicos}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    sala = Sala.objects.get(id=pk)
    salaform = SalaForm(instance=sala)
    topicos = Topico.objects.all()

    if request.user != sala.host:
        return HttpResponse('Your are not allowed here!')

    if request.method == 'POST':
        topico_nome = request.POST.get('topico').lower()
        topico, created = Topico.objects.get_or_create(nome=topico_nome)
        sala.nome = request.POST.get('nome')
        sala.topico=topico
        sala.descricao=request.POST.get('descricao')
        sala.save()
        return redirect('room', pk=sala.id)
    
    context={'form':salaform, 'topicos':topicos, 'sala':sala}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    page = 'deleteRoom'
    sala = Sala.objects.get(id=pk)

    if request.user != sala.host:
        return HttpResponse('Your are not allowed here!')

    if request.method == 'POST':
        sala.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj':sala, 'page': page})


@login_required(login_url='login')
def deleteMessage(request, pk):
    mensagem = Mensagem.objects.get(id=pk)

    if request.user != mensagem.usuario:
        return HttpResponse('Your are not allowed here!')

    if request.method == 'POST':
        mensagem.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj':mensagem})


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    context={'form': form}        
    return render(request, 'base/update_user.html', context)        
