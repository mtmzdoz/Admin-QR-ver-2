from django import forms
from .models import Agregar
from datetime import date

#Formulario para agregar nueva obra
class AgregarForm(forms.ModelForm):

    class Meta:
        model = Agregar
        #fields= ["titulo", "autor", "pieza", "descripcion", "fecha"]
        fields= '__all__' 

        widgets = {
            "fecha": forms.SelectDateWidget(years=range(1600, date.today().year)) #Selector de fecha con rango
        }

#Formulario para actualizar imagen de un registro existente
class UpdateImg(forms.ModelForm):
    class Meta:
        model= Agregar
        fields= [ "Imagen"]

#Formulario para actualizar título, descripción y fecha de un registro
class UpdateForm(forms.ModelForm):
    class Meta:
        model= Agregar
        fields= ["titulo", "descripcion", "fecha"]

        widgets = {
            "fecha": forms.SelectDateWidget(years=range(1600, date.today().year))
        }