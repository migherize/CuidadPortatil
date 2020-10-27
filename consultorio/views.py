from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from django.core.mail import EmailMessage

# Create your views here.

def CuidadPortatil(request):
	return render(request, 'consultorio/CuidadPortatil.html', {})

def signUp(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Login(request.POST)
        # check whether it's valid:
        if form.is_valid():
        	username = form.cleaned_data['username']
        	password = form.cleaned_data['password']
        	print(username,password)
        	user = authenticate(username=username, password=password)
        	print("user2",user)
        	if user is not None:
        		login(request, user)
        		print("Bienvenido")
        		return render(request, 'consultorio/menu.html', {'user':user})
        	else:
        		print("No estas logiado, registrate")
        		return HttpResponseRedirect('/Login/')
    else:
    	form = Login()

    print("debe escribir")
    return render(request, 'consultorio/login.html', {'form': form})

def signOut(request):
	logout(request)
	print("Hasta Luego")
	return HttpResponseRedirect('/login/')

def main(request):
	return render(request, 'consultorio/menu.html',{})

def calendario(request):
	return render(request, 'consultorio/calendario.html',{})

def registro(request):
	if request.method == 'POST':
		form = Pacientes(request.POST)
		print(request.POST)
		print("---------------")
		print(form)
		if form.is_valid():
			nombre = form.cleaned_data['Nombre']
			apellido = form.cleaned_data['Apellido']
			paciente = Paciente.objects.create(nombre,apellido, Edad='1997-08-26 01:43:52-04',sexo='M',fecha_ini='2020-10-27 01:43:52-04',user='1')
			print("Aqui")
			print(paciente)

	return render(request, 'consultorio/Registro.html',{})

def historias(request):
	return render(request, 'consultorio/historias.html',{})