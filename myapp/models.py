from django.db import models
from django.utils import timezone
# Create your models here.

opciones_pieza= [
    [0, "Busto"],
    [2, "Pintura"],
    [3, "Retrato"],
    [4, "Otro"]
]

class Agregar(models.Model):
    #decir que tipo de dato estamos introduciendo 
    titulo= models.CharField(max_length=100) #CharField para strings o textos pequeños
    autor= models.CharField(max_length=30)
    pieza= models.IntegerField(choices= opciones_pieza)
    descripcion= models.TextField(max_length=255) #TextField para textos largos
    fecha= models.DateField()
    Imagen= models.ImageField(upload_to="imagenes", null=True)

    #imagenes= models.ImageField(upload_to="imagenes", null=True)
    
    def __str__(self):
        return self.titulo

#Campo para pausar información en vez de eliminarla    
class Elemento(models.Model):
    nombre=models.CharField(max_length=255)
    detalles=models.TextField()
    activo=models.BooleanField(default=True) #Campo para pausar información
    actualizado_en=models.DateTimeField(auto_now=True) #Marca cuando fue actualizado
    
    def __str__(self):
        return self.nombre
    
class Notificacion(models.Model):
    mensaje=models.TextField()
    fecha=models.DateTimeField(default=timezone.now)
    tipo=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.tipo}: {self.mensaje[:50]}' 