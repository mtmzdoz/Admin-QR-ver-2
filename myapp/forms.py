from django import forms
from .models import Agregar
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class AgregarForm(forms.ModelForm):

    class Meta:
        model = Agregar
        #fields= ["titulo", "autor", "pieza", "descripcion", "fecha"]
        fields= '__all__'

        widgets = {
            "fecha": forms.SelectDateWidget(years=range(1600, date.today().year))
        }


class UpdateImg(forms.ModelForm):
    class Meta:
        model= Agregar
        fields= [ "Imagen"]

class UpdateForm(forms.ModelForm):
    class Meta:
        model= Agregar
        fields= ["titulo", "descripcion", "fecha"]

        widgets = {
            "fecha": forms.SelectDateWidget(years=range(1600, date.today().year))
        }

class CustomUserCreationForm(UserCreationForm): #creamos un form custom a partir del que django nos da Usercreationform
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name","email","password1", "password2"]