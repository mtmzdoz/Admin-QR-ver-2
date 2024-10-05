from django.urls import path

from . import views
from .views import home, agregar, detalle_pieza



urlpatterns =[
    path('', home, name="home"),
    path('agregar/', agregar, name="agregar"),
    path('pieza/<int:id>/', detalle_pieza, name='detalle_pieza'),  # Nueva ruta
    
    
]
