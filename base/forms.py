from django import forms
from .models import *

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'