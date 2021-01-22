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
    Direccion = forms.CharField(label='Direccion', max_length=50)
    Ocupacion = forms.CharField(label='Ocupacion', max_length=50)
    Correo = forms.CharField(label='Correo', max_length=30)
    Motivo = forms.CharField(label='Motivo', max_length=100)
    fecha_ini = forms.DateField(label='fecha_ini')

class Foto(forms.Form):
    url = forms.CharField(label='url', max_length=45)

class Telefono(forms.Form):
    movil = forms.CharField(label='movil', max_length=15)
    casa = forms.CharField(label='casa', max_length=15)

class Antecedentes(forms.Form):
    Personales = forms.CharField(label='Personales', max_length=45)
    Familiares = forms.CharField(label='Familiares', max_length=45)
    Alergicos = forms.CharField(label='Alergicos', max_length=45)
    Hemorragias = forms.CharField(label='Hemorragias', max_length=45)
    otras = forms.CharField(label='otras', max_length=45)

class Fumas(forms.Form):
    B_fuma = forms.CharField(label='B_fuma', max_length=1)
    Forma = forms.CharField(label='Forma', max_length=15)

class Cafes(forms.Form):
    B_cafe = forms.CharField(label='B_cafe', max_length=1)
    Duracion = forms.CharField(label='Duracion', max_length=15)

class Otro(forms.Form):
    B_otros = forms.CharField(label='B_otros', max_length=1)
    Frecuencia = forms.CharField(label='Frecuencia', max_length=15)

class Intra(forms.Form):
    texto = forms.CharField(widget=forms.Textarea, max_length=100)

class Extra(forms.Form):
    Perfil = forms.CharField(label='Perfil', max_length=45)
    Piel_Mucosa = forms.CharField(label='Piel_Mucosa', max_length=45)
    ATM = forms.CharField(label='ATM', max_length=45)
    otros = forms.CharField(label='otros', max_length=45)
    
class Diagno(forms.Form):
    diagnostico = forms.CharField(widget=forms.Textarea, max_length=500)

class Historias(forms.Form):
    busca = forms.CharField(label='busca', max_length=45)
    buscalo = forms.CharField(label='buscalo', max_length=1)
    
class Cita(forms.Form):
    Citar = forms.CharField(label='Citar', max_length=45)
    date = forms.DateTimeField(label='date')
    motivo = forms.CharField(label='motivo', max_length=45)

class Dia(forms.Form):
    dia = forms.DateTimeField(label='dia')

class Evolucion(forms.Form):
    Fecha = forms.CharField(label='Fecha')
    Tratamiento = forms.CharField(label='Tratamiento', max_length=45)
    Abono = forms.CharField(label='Abono', required=True)
    Resta = forms.CharField(label='Resta',required=True)
    