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
    Cedula = forms.CharField(label='Cedula', max_length=10)
    Edad = forms.DateField(label='Edad')
    sexo = forms.CharField(label='sexo', max_length=1)
    Direccion = forms.CharField(label='Direccion', max_length=10)
    Ocupacion = forms.CharField(label='Ocupacion', max_length=10)
    Correo = forms.CharField(label='Correo', max_length=30)
    Motivo = forms.CharField(label='Motivo', max_length=100)
    fecha_ini = forms.DateField(label='fecha_ini')