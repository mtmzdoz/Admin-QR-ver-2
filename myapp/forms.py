from django import forms
from .models import Agregar
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput
class AgregarForm(forms.ModelForm):

    class Meta:
        model = Agregar
        fields= ["titulo", "autor", "ubicacion", "pieza", "descripcion", "fecha", "Imagen"]

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
        fields= ["titulo", "ubicacion", "descripcion", "fecha"]

        widgets = {
            "fecha": forms.SelectDateWidget(years=range(1600, date.today().year))
        }

class CustomUserCreationForm(UserCreationForm): #creamos un form custom a partir del que django nos da Usercreationform
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name","email","password1", "password2"]

class UpdateCuenta(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput(render_value=True))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        
