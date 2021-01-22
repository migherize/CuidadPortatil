from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from django.core.mail import EmailMessage
import itertools
from datetime import datetime
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
	if request.method == 'GET':
		print("dale al calendario")
		return render(request, 'consultorio/calendario.html', {})
			
	elif request.method == 'POST':
		global citado, fecha, Motivo
		sustituir = False
		consultas= consulta.objects.all()
		form = Cita(request.POST)
		print("request",request.POST)

		if form.is_valid():
			cita = form.cleaned_data['Citar']
			fecha = form.cleaned_data['date']
			Motivo = form.cleaned_data['motivo']
			print("fecha",fecha)
			print("cita",cita)
			fecha2 = str(fecha)
			hora = fecha2[11:13]
			busqueda = Paciente.objects.filter(Cedula= cita)
			for c in consultas:
				if c.fecha == fecha:
					sustituir = True

			if sustituir:
				print("vamos a sustituir una cita") 
				instancia = consulta.objects.get(fecha=fecha)
				print("pase")
				print("inst",instancia.user.Nombre)
				print("inst",instancia.fecha)
				print("inst",instancia.idconsulta)
				print("inst",instancia.motivo)
				instancia.delete()
			if busqueda:
				citado = busqueda
				return render(request, 'consultorio/citas.html', {'busqueda': busqueda, 'paciente':True, 'hora':hora})	
			else:
				print("Paciente no encontrada")
		else:
			form2= Dia(request.POST)
			dia = form2['dia'].value()
			print("dia",dia)
			citas= list(consultas)
			band = False
			citas_dia = []
			print("muestro los citados del dia")
			for c in citas:
				d = str(c.fecha.date())
				if d == dia:
					print("Paciente:",c.fecha.hour,"hora:",c.user.Nombre)
					del_dia = c
					citas_dia.append(del_dia)
					band = True
			if band:
				return render(request, 'consultorio/citas.html', {'citas_dia': citas_dia})
			else:
				print("holi")
				return render(request, 'consultorio/citas.html')
	else:
		print("no entre")
	return render(request, 'consultorio/calendario.html',{})

def citar(request):

	global citado, fecha, Motivo

	for v in citado:
		citando = v

	u = Paciente.objects.all()
	user = list(u)
	for a in user:
		print("as ",a.Cedula)
		if citando.Cedula == a.Cedula:
			first = a
			
	print("user ",first.Cedula)
	d = doctores.objects.all()
	doc = list(d)
	first_doc = doc[0]
	print("doc ",first_doc.nombre)

	if request.method == 'GET':
		print("voy a citar")
		consulta.objects.create(fecha=fecha,motivo=Motivo, sucursal= 'Trujillo',doctores_id= first_doc,user=first)
		return render(request, 'consultorio/menu.html',{})
	return render(request, 'consultorio/citas.html', {})

def registro(request):
	if request.method == 'POST':
		form = Pacientes(request.POST)
		form2 = Foto(request.POST)
		form3 = Antecedentes(request.POST)
		form4 = Telefono(request.POST)
		form5 = Fumas(request.POST)
		form6 = Cafes(request.POST)
		form7 = Otro(request.POST)
		form8 = Intra(request.POST)
		form9 = Extra(request.POST)
		form10 = Diagno(request.POST)
		caries1 = {
			'1':'a0','2':'a1','3':'a2','4':'a3','5':'a4','6':'a5','7':'a6','8':'a7','9':'a8','10':'a9',
			'11':'a10','12':'a11','13':'a12','14':'a13','15':'a14','16':'a15','17':'a16','18':'a17','19':'a18',
			'20':'a19','21':'a20','22':'a21','23':'a22','24':'a23','25':'a24','26':'a25','27':'a26','28':'a27','29':'a28',
			'30':'a29','31':'a30','32':'a31','33':'a32','34':'a33','35':'a34','36':'a35','37':'a36','38':'a37','39':'a38',
			'40':'a39','41':'a40','42':'a41',
		}
		caries2 = {
			'1':'A0','2':'A1','3':'A2','4':'A3','5':'A4','6':'A5','7':'A6','8':'A7','9':'A8','10':'A9','11':'A10',
			'12':'A11','13':'A12','14':'A13','15':'A14','16':'A15','17':'A16','18':'A17','19':'A18','20':'A19',
			'21':'A20','22':'A21','23':'A22','24':'A23','25':'A24','26':'A25','27':'A26','28':'A27','29':'A28',
			'30':'A29','31':'A30','32':'A31','33':'A32','34':'A33','35':'A34','36':'A35','37':'A36','38':'A37',
			'39':'A38','40':'A39','41':'A40','42':'A41',
		}
		lista1 = []
		lista2 = []
		for c in caries1:
			lista1.append(request.POST[caries1[c]])
		for c in caries1:
			lista2.append(request.POST[caries2[c]])

		lista1+=lista2
		carie = ','.join(lista1)
		print("caries",carie)
		print("request", request.POST)
		print("formularios1", form.is_valid())
		print("formularios2", form2.is_valid())
		print("formularios3", form3.is_valid())
		print("formularios4", form4.is_valid())
		print("formularios5", form5.is_valid())
		print("formularios6", form6.is_valid())
		print("formularios7", form7.is_valid())
		print("formularios8", form8.is_valid())
		print("formularios9", form9.is_valid())
		print("formularios10", form10.is_valid())

		if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid() and form8.is_valid() and form9.is_valid() and form10.is_valid():
			print("paso")
			u = User.objects.all()
			user = list(u)
			first = user[0]
			perfil = Paciente.objects.create(**form.cleaned_data,user=first)
			foto.objects.create(**form2.cleaned_data,Paciente_id=perfil)
			AntecedentesMedicos.objects.create(**form3.cleaned_data,Paciente_id=perfil)
			Telefonos.objects.create(**form4.cleaned_data,Paciente_id=perfil)
			habitos = HabitosCepillado.objects.create(Paciente_id=perfil)
			Fuma.objects.create(**form5.cleaned_data,Fuma_id=habitos)
			Cafe.objects.create(**form6.cleaned_data,Cafe_id=habitos)
			Otros.objects.create(**form7.cleaned_data,Otros_id=habitos)
			Intrabucal.objects.create(**form8.cleaned_data,Paciente_id=perfil)
			ExtraBucal.objects.create(**form9.cleaned_data,Paciente_id=perfil)
			Odontodiagrama.objects.create(caries=carie,Paciente_id=perfil)
			DiagnosticoOdontologico.objects.create(**form10.cleaned_data,Paciente_id=perfil)
			print("correcto todo")
			return render(request, 'consultorio/Registro.html', {'formulario':True,'registro':'1'})
		else:
			print("no entro")
			return render(request, 'consultorio/Registro.html', {'formulario':True,'registro':'0'})
	return render(request, 'consultorio/Registro.html',{'formulario':True})

def historias(request):
	if request.method == 'POST':
		print(request.POST)
		form2 = Evolucion(request.POST)
		print("form2",form2)
		form = Historias(request.POST)
		if form2.is_valid():
			print("entre")
			Fecha = form2.cleaned_data['Fecha']
			Tratamiento = form2.cleaned_data['Tratamiento']
			Abono = form2.cleaned_data['Abono']
			Resta = form2.cleaned_data['Resta']
			consultas= consulta.objects.get(idconsulta=Fecha)
			consultas.Tratamiento = Tratamiento
			consultas.Abono = Abono
			consultas.Resta = Resta
			consultas.save()
		elif form.is_valid():
			busca = form.cleaned_data['busca']
			buscalo = form.cleaned_data['buscalo']
			print("busca",busca)
			print("buscalo",buscalo)
			if buscalo == 'c':
				busqueda=Paciente.objects.filter(Cedula=busca)
			elif buscalo == 'a':
				busqueda=Paciente.objects.filter(Apellido=busca)
			elif buscalo == 't':
				busqueda = Paciente.objects.all()
				return render(request, 'consultorio/busqueda.html', {'busqueda': busqueda, 'paciente':True, 'all':False})
			if busqueda:
				for v in busqueda:
					e = v
					print("v ",v.Edad)
					print("v ",v.Nombre)
				
				F=foto.objects.filter(Paciente_id=v)
				T=Telefonos.objects.filter(Paciente_id=v)
				A=AntecedentesMedicos.objects.filter(Paciente_id=v)
				H=HabitosCepillado.objects.filter(Paciente_id=v)
				I=Intrabucal.objects.filter(Paciente_id=v)
				E=ExtraBucal.objects.filter(Paciente_id=v)
				C=[]
				diagrama=Odontodiagrama.objects.filter(Paciente_id=v)
				D=DiagnosticoOdontologico.objects.filter(Paciente_id=v)
				evolucion=consulta.objects.filter(user=v).order_by('fecha')
				today = datetime.now()
				proxima= today
				for e in evolucion:
					if e.fecha>today:
						proxima = e.fecha
						break
				for d in diagrama:
					list_d = list(d.caries)				
				for r in range(0,83):
					list_d.remove(',')
				for l in range(0,84):
					C.append(list_d[l])
					if list_d[l] == '1':
						print("con carie",l)
				for e in evolucion:
					print("Evolucion",e.motivo)

				for a in H:
					fuma=Fuma.objects.filter(Fuma_id=a.idHabitosCepillado)
					cafe=Cafe.objects.filter(Cafe_id=a.idHabitosCepillado)
					otros=Otros.objects.filter(Otros_id=a.idHabitosCepillado)
					print("fuma",fuma)
					print("cafe",cafe)
					print("otros",otros)

				return render(request, 'consultorio/busqueda.html', {'busqueda': busqueda,'F': F,'T': T,'A': A,'H': H,'I': I,'E': E,'C': C,'D': D, 'paciente':True, 'evolucion': evolucion,'fuma':fuma, 'cafe':cafe,'otros':otros,'all':True, 'proxima':proxima})
				
			else:
				print("No existe paciente con ese ID")
				return render(request, 'consultorio/busqueda.html', {'paciente':False, 'all':False})

		else:
			buscalo = form.cleaned_data['buscalo']
			if buscalo == 't':
				busqueda = Paciente.objects.all()
				return render(request, 'consultorio/busqueda.html', {'busqueda': busqueda, 'paciente':True, 'all':False})
	return render(request, 'consultorio/historias.html',{})