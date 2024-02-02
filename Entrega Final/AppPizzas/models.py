from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):
    nombre = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=30)
    masa = models.CharField(max_length=30)
    ingrediente1 = models.CharField(max_length=30)
    ingrediente2 = models.CharField(max_length=30)
    ingrediente3 = models.CharField(max_length=30)
    ingrediente4 = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} --- {self.masa}"
    
class Creador(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} --- {self.edad}"

class Asesor(models.Model):
    nombre = models.CharField(max_length=30)
    cod_ases = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} --- {self.cod_ases}"


class AvatarImagen (models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares",null=True,blank=True)
    
    def __str__(self):
        return f"{self.usuario} --- {self.imagen}"