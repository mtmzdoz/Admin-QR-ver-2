from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
import qrcode  # Importa la librería de qrcode
from .forms import AgregarForm, UpdateImg, UpdateForm, CustomUserCreationForm
from .models import Agregar
import os
from django.contrib.auth import authenticate, login, logout#Permite autenticar el usuario
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required 
from .decorators import user_iniciado #permisos usuarios


def home(request):
    inicio = 'myapp/home.html'
    return render(request, inicio)

 
#redirige directamente al login
@permission_required('myapp.view_agregar')
@login_required(login_url="/accounts/login/")
def agregar(request):

    data = {
        'form': AgregarForm()
    }

    if request.method == 'POST':
        formulario = AgregarForm(request.POST, request.FILES)
        if formulario.is_valid():
            nueva_pieza = formulario.save()  # Guardar la pieza en la base de datos

            # Generar el código QR con la URL de la pieza
            url_pieza = f"http://127.0.0.1:8000/pieza/{nueva_pieza.id}/"
            qr_img = qrcode.make(url_pieza)

            # Guardar el código QR en la carpeta media
            qr_filename = f'qr_{nueva_pieza.id}.png'
            qr_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes', qr_filename)
            qr_img.save(qr_path)

            # Guardar la ruta del código QR en el modelo
            nueva_pieza.codigo_qr = qr_filename
            nueva_pieza.save()

            data["mensaje"] = "Guardado y QR generado"
            data["qr_url"] = os.path.join(settings.MEDIA_URL, 'qr_codes', qr_filename)  # Enviar la URL a la plantilla

        else:
            data["form"] = formulario

    return render(request, 'myapp/Pieza/agregar.html', data)

@permission_required('myapp.view_articulo')
@login_required(login_url="/accounts/login/")
def detalle_pieza(request, id):
    pieza = get_object_or_404(Agregar, id=id)
    return render(request, 'myapp/detalle_pieza.html', {'pieza': pieza})

@permission_required('myapp.view_articulo')
@login_required(login_url="/accounts/login/")
def listado_piezas(request):
    elemento= Agregar.objects.all()

    data = {
        'elemento': elemento
    }
    return render(request, 'myapp/pieza_admin.html', data)

@permission_required('myapp.view_imagen')
@login_required(login_url="/accounts/login/")
def actualizar_img(request, id):
    pieza= get_object_or_404(Agregar, id=id)

    data = {
        'form': UpdateImg(instance=pieza)
    }
    if request.method == 'POST':
        nueva_img = Agregar.objects.get(id=id)
        formulario = UpdateImg(instance=pieza, data=request.FILES, files=request.FILES)
        if formulario.is_valid():
            nueva_img.Imagen.delete()
            formulario.save()  # Guardar 
            return redirect(to="listado_piezas")

        data["form"] = formulario
    
    return render(request, 'myapp/Pieza/modificar.html', data)

@permission_required('myapp.view_imagen')
@login_required(login_url="/accounts/login/")
def actualizar_datos(request, id):
    pieza= get_object_or_404(Agregar, id=id)

    data = {
        'form': UpdateForm(instance=pieza)
    }
    if request.method == 'POST':
        formulario = UpdateForm(data=request.POST, instance=pieza, files=request.FILES)
        if formulario.is_valid():
            formulario.save()  # Guardar 
            return redirect(to="listado_piezas")

        data["form"] = formulario
    
    return render(request, 'myapp/Pieza/modificar.html', data)


@permission_required('myapp.delete_articulo')
@login_required(login_url="/accounts/login/")
def eliminar_pieza(request, id):
    pieza= get_object_or_404(Agregar, id=id)
    if request.method== 'POST':
        pieza.delete()
        return redirect(to="listado_piezas")
    return render(request, 'myapp/Pieza/eliminar.html', {'pieza': pieza})






@user_iniciado
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user= formulario.save()  
            user= authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
          
            email = formulario.cleaned_data['email']
            dominio_mail= email.split('@')[-1]
            if dominio_mail == 'gmail.com':
                group = Group.objects.get(name='Usuario')
            elif dominio_mail == 'usm.cl':
                group = Group.objects.get(name='Admin')
            else:
                group = Group.objects.get(name='Usuario')
            user.groups.add(group)
            

            login(request,user) #queda logeado
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")

        data["form"] = formulario
    
    return render(request, 'registration/registro.html', data)

def logoutUser(request):
    logout(request)
    return redirect(to='home')