from django.db import models
from django.contrib.auth.models import User


class Topico(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.nome

class Sala(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topico = models.ForeignKey(Topico, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=200)
    descricao =  models.TextField(null=True, blank=True)
    #participantes =
    criado = models.DateTimeField(auto_now_add=True) 
    editado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Salas'
        ordering = ['-editado', '-criado']
        
    def __str__(self) -> str:
        return self.nome 


class Mensagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    corpo = models.TextField()
    criado = models.DateTimeField(auto_now_add=True) 
    editado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Mensagens'
        
    def __str__(self) -> str:
        return self.corpo[0:50]