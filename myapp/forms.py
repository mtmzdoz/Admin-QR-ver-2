from django import forms
from .models import Agregar

class AgregarForm(forms.ModelForm):

    class Meta:
        model = Agregar
        #fields= ["titulo", "autor", "pieza", "descripcion", "fecha"]
        fields= '__all__'
    