from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import *
  

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'
        exclude = ['host', 'participantes']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']