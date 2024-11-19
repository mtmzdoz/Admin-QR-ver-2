from django import forms
from .models import Agregar
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput



class AgregarForm(forms.ModelForm):
   
    class Meta:
        model = Agregar
        fields= ["titulo", "autor", "ubicación", "pieza", "descripción", "día", "mes", "año", "Imagen"]


class UpdateImg(forms.ModelForm):
    class Meta:
        model= Agregar
        fields= [ "Imagen"]

class UpdateForm(forms.ModelForm):
    class Meta:
        model= Agregar
        fields= ["titulo", "ubicación", "descripción", "día", "mes", "año"]

        

class CustomUserCreationForm(UserCreationForm): #creamos un form custom a partir del que django nos da Usercreationform
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name","email","password1", "password2"]

class UpdateCuenta(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput(render_value=True),required=False)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]
    widgets = {
            'password': forms.PasswordInput(render_value=True),
        }
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            return self.instance.password  # Retorna la contraseña actual si no se proporciona una nueva
        return password