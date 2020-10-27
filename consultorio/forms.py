from django import forms
from django.contrib.auth.models import User
from .models import  *
from django.contrib.auth.forms import UserCreationForm

class Login(forms.Form):
    username = forms.CharField(label='Usuario', max_length=30)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), max_length=100)

class Pacientes (forms.Form):
	Nombre = forms.CharField(label='Nombre', max_length=30)
	Apellido = forms.CharField(label='Apellido', max_length=30)
