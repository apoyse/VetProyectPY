from django.db import models

class Empleados(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni = models.IntegerField(primary_key=True)
    telefono = models.IntegerField()
    cargo = models.CharField(max_length=50)


class Pacientes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    nombre_mascota = models.CharField(max_length=50)
    observacion =  models.CharField(max_length=300)
    id = models.models.AutoField(primary_key=True)

class Productos():
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    stock=models.IntegerField()
    id = models.models.AutoField(primary_key=True)
# Create your models here.
