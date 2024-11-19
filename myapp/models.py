from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractUser
from datetime import date

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
meses = [
        [1, 'Enero'],
        [2, 'Febrero'],
        [3, 'Marzo'],
        [4, 'Abril'],
        [5, 'Mayo'],
        [6, 'Junio'],
        [7, 'Julio'],
        [8, 'Agosto'],
        [9, 'Septiembre'],
        [10, 'Octubre'],
        [11, 'Noviembre'],
        [12, 'Diciembre'],
    ]
dias = [
    [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], 
    [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10'], 
    [11, '11'], [12, '12'], [13, '13'], [14, '14'], [15, '15'], 
    [16, '16'], [17, '17'], [18, '18'], [19, '19'], [20, '20'], 
    [21, '21'], [22, '22'], [23, '23'], [24, '24'], [25, '25'], 
    [26, '26'], [27, '27'], [28, '28'], [29, '29'], [30, '30'], 
    [31, '31']
]
class Agregar(models.Model):
    años = [(year, str(year)) for year in range(1000, date.today().year + 1)]
    #decir que tipo de dato estamos introduciendo 
    titulo= models.CharField(max_length=100) #CharField para strings o textos pequeños
    autor= models.CharField(max_length=30)
    ubicación= models.IntegerField(choices=opciones_ubicacion, null=True)
    pieza= models.IntegerField(choices= opciones_pieza, null=True)
    descripción= models.TextField(max_length=255) #TextField para textos largos
    año = models.IntegerField(choices=años, null=True, blank=True)
    mes = models.IntegerField(choices= meses, null=True, blank=True)
    día = models.IntegerField(choices= dias, null=True, blank=True)
    Imagen= models.ImageField(upload_to="imagenes", null=True)
    activo=models.BooleanField(default=True) #Campo para pausar información
    codigo_qr=models.ImageField(upload_to="qr_codes/", null=True)

    
    def __str__(self):
        return self.titulo

    
