from django.shortcuts import render,redirect,get_object_or_404

from django.db.models import Q

from .models import *
from .serializers import *
from .forms import *

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    salas = Sala.objects.filter(
        Q(topico__nome__icontains=q) |
        Q(nome__icontains=q) |
        Q(descricao__icontains=q) 
        )
    
    topicos = Topico.objects.order_by('nome')
    
    sala_count = salas.count()
    
    context={'salas':salas, 'topicos':topicos, 'sala_count':sala_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    sala = Sala.objects.get(id=pk)
    context={'sala':sala}
    return render(request, 'base/room.html', context)

def createRoom(request):
    salaform = SalaForm()
    if request.method == 'POST':
        salaform = SalaForm(request.POST or None, request.FILES)
        if salaform.is_valid():
            sala = salaform.save(commit=False)
            sala.save()
            return redirect('home')
    context={'form':salaform}
    return render(request, 'base/create_room.html', context)

def updateRoom(request, pk):
    sala = Sala.objects.get(id=pk)
    salaform = SalaForm(instance=sala)
    if request.method == 'POST':
        salaform = SalaForm(request.POST or None, request.FILES, instance=sala)
        if salaform.is_valid():
            salaform.save()
            return redirect('home')
    
    context={'form':salaform}
    return render(request, 'base/create_room.html', context)


def deleteRoom(request, pk):
    sala = Sala.objects.get(id=pk)
    if request.method == 'POST':
        sala.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj':sala})