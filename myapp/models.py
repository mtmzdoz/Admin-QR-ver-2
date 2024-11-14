from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractUser

opciones_pieza= [
    [0, "Busto"],
    [2, "Pintura"],
    [3, "Retrato"],
    [4, "Otro"]
]

opciones_ubicacion=[
    [0, "Salón Gabriela Mistral"],
    [1, "Hemeroteca"],
    [2, "Salón Medina"],
    [3, "Sala Ercilla"],
    [4, "Salón Camilo Henríquez"],
    [5, "Sector Alameda 1er piso"],
    [6, "Sector Alameda 2do piso"],
    [7, "Sector Moneda 1er piso"],
    [8, "Sector Moneda 2do piso"],

]
class Agregar(models.Model):
    #decir que tipo de dato estamos introduciendo 
    titulo= models.CharField(max_length=100) #CharField para strings o textos pequeños
    autor= models.CharField(max_length=30)
    ubicacion= models.IntegerField(choices=opciones_ubicacion, null=True)
    pieza= models.IntegerField(choices= opciones_pieza, null=True)
    descripcion= models.TextField(max_length=255) #TextField para textos largos
    fecha= models.DateField(null=True)
    Imagen= models.ImageField(upload_to="imagenes", null=True)
    activo=models.BooleanField(default=True) #Campo para pausar información
    codigo_qr=models.ImageField(upload_to="qr_codes/", null=True)

    
    def __str__(self):
        return self.titulo
    
class Notificacion(models.Model):
    mensaje=models.TextField()
    fecha=models.DateTimeField(default=timezone.now)
    tipo=models.CharField(max_length=50)
    ###def str(self):
        ###return f'{self.tipo}:{self.mensaje[:50]}'
    
