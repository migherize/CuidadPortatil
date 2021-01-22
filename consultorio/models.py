from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Zona de Perfil

class Paciente(models.Model):
    idPaciente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=45, null=True, blank=True, default=None)
    Apellido = models.CharField(max_length=45, null=True, blank=True, default=None)
    Cedula = models.CharField(max_length=10, null=True, blank=True, default=None)
    Edad = models.DateField()
    Correo = models.CharField(max_length=45, null=True, blank=True, default=None)
    Direccion = models.CharField(max_length=60, null=True, blank=True, default=None)
    Ocupacion = models.CharField(max_length=45, null=True, blank=True, default=None)
    genero = (
		('F','Femenino'),
		('M','Masculo'),
	)
    sexo = models.CharField(max_length=1, choices = genero)
    Motivo = models.CharField(max_length=45, null=True, blank=True, default=None)
    fecha_ini = models.DateField()
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.Nombre

class doctores(models.Model):
    iddoctores = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=True, blank=True, default=None)
    apellido = models.CharField(max_length=45, null=True, blank=True, default=None)
    cedula = models.IntegerField()
    especialidad = models.CharField(max_length=45, null=True, blank=True, default=None)

    def __unicode__(self):
        return self.nombre

class consulta(models.Model):
    idconsulta = models.AutoField(primary_key=True)
    fecha =  models.DateTimeField()
    motivo = models.CharField(max_length=45, null=True, blank=True, default=None)
    Tratamiento = models.CharField(max_length=45, null=True, blank=True, default=None)
    Abono = models.IntegerField(null=True, blank=True)
    Resta = models.IntegerField(null=True, blank=True)
    sucursal = models.CharField(max_length=45, null=True, blank=True, default=None)
    ProximaCita =  models.DateTimeField(null=True, blank=True)

    doctores_id = models.ForeignKey(doctores, on_delete=models.CASCADE)
    user = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.user


class AntecedentesMedicos(models.Model):
    idAntecedentes = models.AutoField(primary_key=True)
    Personales = models.CharField(max_length=45, null=True, blank=True, default=None)
    Familiares = models.CharField(max_length=45, null=True, blank=True, default=None)
    Alergicos = models.CharField(max_length=45, null=True, blank=True, default=None)
    Hemorragias = models.CharField(max_length=45, null=True, blank=True, default=None)
    otras = models.CharField(max_length=45, null=True, blank=True, default=None)

    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.Paciente_id

class DiagnosticoOdontologico(models.Model):
    idDiagnosticoOdontologico = models.AutoField(primary_key=True)
    diagnostico = models.TextField(max_length=500, null=True, blank=True, default=None)
    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    
    def __unicode__(self):
    	return self.Paciente_id

class foto(models.Model):
    idfoto = models.AutoField(primary_key=True)
    url = models.CharField(max_length=45, null=True, blank=True, default=None)

    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    
    def __unicode__(self):
    	return self.Paciente_id

class Telefonos(models.Model):
    idTelefonos = models.AutoField(primary_key=True)
    movil = models.CharField(max_length=45, null=True, blank=True, default=None)
    casa = models.CharField(max_length=45, null=True, blank=True, default=None)
    
    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.Paciente_id

class ExtraBucal(models.Model):
    idExtraBucal = models.AutoField(primary_key=True)
    Perfil = models.CharField(max_length=45, null=True, blank=True, default=None)
    Piel_Mucosa = models.CharField(max_length=45, null=True, blank=True, default=None)
    ATM = models.CharField(max_length=45, null=True, blank=True, default=None)
    otros = models.CharField(max_length=45, null=True, blank=True, default=None)

    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.Paciente_id

class Intrabucal(models.Model):
    idIntrabucal = models.AutoField(primary_key=True)
    texto = models.TextField(max_length=500, null=True, blank=True, default=None)

    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.Paciente_id

class Odontodiagrama(models.Model):
    idOdontodiagrama = models.AutoField(primary_key=True)
    caries = models.CharField(max_length=200, null=True, blank=True, default=None)

    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.Paciente_id

# Habitos

class HabitosCepillado(models.Model):
    idHabitosCepillado = models.AutoField(primary_key=True)
    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)

class Fuma(models.Model):
    idFuma = models.AutoField(primary_key=True)
    booleano = (
		('Y','Si'),
		('N','No'),
	)
    B_fuma = models.CharField(max_length=1, choices = booleano)
    Forma = models.CharField(max_length=45, null=True, blank=True, default=None)
    Fuma_id = models.OneToOneField(HabitosCepillado, on_delete=models.CASCADE)

class Cafe(models.Model):
    idCafe = models.AutoField(primary_key=True)
    booleano = (
		('Y','Si'),
		('N','No'),
	)
    B_cafe = models.CharField(max_length=1, choices = booleano)
    Duracion = models.CharField(max_length=45, null=True, blank=True, default=None)
    Cafe_id = models.OneToOneField(HabitosCepillado, on_delete=models.CASCADE)

class Otros(models.Model):
    idOtros = models.AutoField(primary_key=True)
    booleano = (
		('Y','Si'),
		('N','No'),
	)
    B_otros = models.CharField(max_length=1, choices = booleano)
    Frecuencia = models.CharField(max_length=45, null=True, blank=True, default=None)
    
    Otros_id = models.OneToOneField(HabitosCepillado, on_delete=models.CASCADE)