from django.db import models
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
    Imagen= models.ImageField(upload_to="static/imagenes", null=True)

    
    def __str__(self):
        return self.titulo
    
