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
    Edad = models.DateTimeField()
    Correo = models.CharField(max_length=45, null=True, blank=True, default=None)
    Direccion = models.CharField(max_length=60, null=True, blank=True, default=None)
    Ocupacion = models.CharField(max_length=45, null=True, blank=True, default=None)
    genero = (
		('F','Femenino'),
		('M','Masculo'),
	)
    sexo = models.CharField(max_length=1, choices = genero)
    Motivo = models.CharField(max_length=45, null=True, blank=True, default=None)
    fecha_ini = models.DateTimeField()
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.user

class doctores(models.Model):
    iddoctores = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=True, blank=True, default=None)
    apellido = models.CharField(max_length=45, null=True, blank=True, default=None)
    cedula = models.IntegerField()
    especialidad = models.CharField(max_length=45, null=True, blank=True, default=None)


class consulta(models.Model):
    idconsulta = models.AutoField(primary_key=True)
    fecha =  models.DateTimeField()
    sucursal = models.CharField(max_length=45, null=True, blank=True, default=None)

    doctores_id = models.OneToOneField(doctores, on_delete=models.CASCADE)
    user = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.Paciente_id


class AntecedentesMedicos(models.Model):
    idAntecedentes = models.AutoField(primary_key=True)
    Personales = models.CharField(max_length=45, null=True, blank=True, default=None)
    Familiares = models.CharField(max_length=45, null=True, blank=True, default=None)
    Alergicos = models.CharField(max_length=45, null=True, blank=True, default=None)
    Hemorragias = models.CharField(max_length=45, null=True, blank=True, default=None)
    otros = models.CharField(max_length=45, null=True, blank=True, default=None)

    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.Paciente_id

class DiagnosticoOdontologico(models.Model):
    idDiagnosticoOdontologico = models.AutoField(primary_key=True)
    diagnostico = models.CharField(max_length=45, null=True, blank=True, default=None)
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
    texto = models.CharField(max_length=45, null=True, blank=True, default=None)

    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.Paciente_id

class Odontodiagrama(models.Model):
    idOdontodiagrama = models.AutoField(primary_key=True)
    caries = models.CharField(max_length=45, null=True, blank=True, default=None)

    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.Paciente_id

class Evolucion(models.Model):
    idEvolucion = models.AutoField(primary_key=True)
    Tratamiento = models.CharField(max_length=45, null=True, blank=True, default=None)
    Fecha =  models.DateTimeField()
    Abono = models.IntegerField()
    Resta = models.IntegerField()
    ProximaCita =  models.DateTimeField()

    Paciente_id = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.Paciente_id

# Habitos
class Fuma(models.Model):
    idFuma = models.AutoField(primary_key=True)
    Forma = models.CharField(max_length=45, null=True, blank=True, default=None)

class Cafe(models.Model):
    idCafe = models.AutoField(primary_key=True)
    Duracion = models.CharField(max_length=45, null=True, blank=True, default=None)

class Otros(models.Model):
    idOtros = models.AutoField(primary_key=True)
    Frecuencia = models.CharField(max_length=45, null=True, blank=True, default=None)

class HabitosCepillado(models.Model):
    idHabitosCepillado = models.AutoField(primary_key=True)
    Fuma_id = models.OneToOneField(Fuma, on_delete=models.CASCADE)
    Cafe_id = models.OneToOneField(Cafe, on_delete=models.CASCADE)
    Otros_id = models.OneToOneField(Otros, on_delete=models.CASCADE)