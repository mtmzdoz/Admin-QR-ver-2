from django import forms
from .models import Agregar
from datetime import date

class AgregarForm(forms.ModelForm):

    class Meta:
        model = Agregar
        #fields= ["titulo", "autor", "pieza", "descripcion", "fecha"]
        fields= '__all__'

        widgets = {
            "fecha": forms.SelectDateWidget(years=range(1600, date.today().year))
        }