from django.db import models
# from django.contrib.auth.models import User

class Empleados(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni = models.IntegerField(primary_key=True)
    telefono = models.IntegerField(null=True)
    cargo = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido} "
   


class Pacientes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField(max_length=254,null=True)
    nombre_mascota = models.CharField(max_length=50)
    observacion =  models.CharField(max_length=300)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.dni} | {self.nombre_mascota} | {self.id}"

class Productos(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    stock=models.IntegerField()
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.nombre




class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    mensaje = models.CharField(max_length=300)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f" Contacto de {self.nombre} {self.apellido} "


class Page(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    slug = models.CharField('Slug', max_length = 150, unique = True)
    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
    def __str__(self):
        return self.titulo 
