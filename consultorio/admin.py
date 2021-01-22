from django.contrib import admin
from consultorio.models import *

# Register your models here.
admin.site.register(doctores)
admin.site.register(consulta)
admin.site.register(Paciente)
admin.site.register(AntecedentesMedicos)
admin.site.register(DiagnosticoOdontologico)
admin.site.register(foto)
admin.site.register(Telefonos)
admin.site.register(ExtraBucal)
admin.site.register(Intrabucal)
admin.site.register(Odontodiagrama)
admin.site.register(Fuma)
admin.site.register(Cafe)
admin.site.register(Otros)
admin.site.register(HabitosCepillado)