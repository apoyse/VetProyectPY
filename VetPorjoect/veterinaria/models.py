from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime
from django.urls import reverse
class Empleados(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni = models.IntegerField(primary_key=True)
    telefono = models.IntegerField(null=True)
    cargo = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,null=True)
    imagen = models.ImageField(upload_to='empleados/',null=True)
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





class Post(models.Model):
    titulo=models.CharField(max_length=200)
    contenido=RichTextField(blank=True,null=True)
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    fecha_creacion=models.DateField(auto_now=datetime.now())


    def __str__(self):
        return self.titulo + ' ('+self.autor+')'

    class Meta:
        ordering=['-pk']

    
    def get_absolute_url(self):
        return reverse('post_detalle', args=[str(self.id)])

    
    @property
    def get_comentarios_count(self):
        return self.comentarios.all().count()

class Comentario(models.Model):
    autor = models.CharField(max_length=255)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField('contenido', null=False, blank=False)
    post = models.ForeignKey(Post, related_name="comentarios", on_delete=models.CASCADE)

    def __str__(self):
        
        return f'{self.autor}'