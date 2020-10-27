# Generated by Django 3.1.2 on 2020-10-27 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('idCafe', models.AutoField(primary_key=True, serialize=False)),
                ('Duracion', models.CharField(blank=True, default=None, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='doctores',
            fields=[
                ('iddoctores', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('apellido', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('cedula', models.IntegerField()),
                ('especialidad', models.CharField(blank=True, default=None, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fuma',
            fields=[
                ('idFuma', models.AutoField(primary_key=True, serialize=False)),
                ('Forma', models.CharField(blank=True, default=None, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Otros',
            fields=[
                ('idOtros', models.AutoField(primary_key=True, serialize=False)),
                ('Frecuencia', models.CharField(blank=True, default=None, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('idPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Apellido', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Cedula', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('Edad', models.DateTimeField()),
                ('Correo', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Direccion', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('Ocupacion', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculo')], max_length=1)),
                ('Motivo', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('fecha_ini', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Telefonos',
            fields=[
                ('idTelefonos', models.AutoField(primary_key=True, serialize=False)),
                ('movil', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('casa', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Paciente_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Odontodiagrama',
            fields=[
                ('idOdontodiagrama', models.AutoField(primary_key=True, serialize=False)),
                ('caries', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Paciente_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Intrabucal',
            fields=[
                ('idIntrabucal', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Paciente_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='HabitosCepillado',
            fields=[
                ('idHabitosCepillado', models.AutoField(primary_key=True, serialize=False)),
                ('Cafe_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.cafe')),
                ('Fuma_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.fuma')),
                ('Otros_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.otros')),
            ],
        ),
        migrations.CreateModel(
            name='foto',
            fields=[
                ('idfoto', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Paciente_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraBucal',
            fields=[
                ('idExtraBucal', models.AutoField(primary_key=True, serialize=False)),
                ('Perfil', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Piel_Mucosa', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('ATM', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('otros', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Paciente_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Evolucion',
            fields=[
                ('idEvolucion', models.AutoField(primary_key=True, serialize=False)),
                ('Tratamiento', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Fecha', models.DateTimeField()),
                ('Abono', models.IntegerField()),
                ('Resta', models.IntegerField()),
                ('ProximaCita', models.DateTimeField()),
                ('Paciente_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosticoOdontologico',
            fields=[
                ('idDiagnosticoOdontologico', models.AutoField(primary_key=True, serialize=False)),
                ('diagnostico', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Paciente_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='consulta',
            fields=[
                ('idconsulta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('sucursal', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('doctores_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.doctores')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='AntecedentesMedicos',
            fields=[
                ('idAntecedentes', models.AutoField(primary_key=True, serialize=False)),
                ('Personales', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Familiares', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Alergicos', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Hemorragias', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('otros', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('Paciente_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultorio.paciente')),
            ],
        ),
    ]