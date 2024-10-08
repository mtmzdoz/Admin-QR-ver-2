from django.conf import settings
from django.shortcuts import render, get_object_or_404
import qrcode  # Importa la librería de qrcode
from .forms import AgregarForm
from .models import Agregar
import os

def home(request):
    inicio = 'myapp/home.html'
    return render(request, inicio)


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
            qr_path = os.path.join(settings.IMAGENES_ROOT, 'qr_codes', qr_filename)
            qr_img.save(qr_path)

            # Guardar la ruta del código QR en el modelo
            nueva_pieza.codigo_qr = qr_filename
            nueva_pieza.save()

            data["mensaje"] = "Guardado y QR generado"
            data["qr_url"] = os.path.join(settings.IMAGENES_URL, 'qr_codes', qr_filename)  # Enviar la URL a la plantilla

        else:
            data["form"] = formulario

    return render(request, 'myapp/agregar.html', data)

def detalle_pieza(request, id):
    pieza = get_object_or_404(Agregar, id=id)
    return render(request, 'myapp/detalle_pieza.html', {'pieza': pieza})
