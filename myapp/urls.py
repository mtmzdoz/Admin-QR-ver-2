from django.urls import path

from . import views
from .views import home, agregar, detalle_pieza, listado_piezas, actualizar_desc, actualizar_img, eliminar_pieza

###

urlpatterns =[
    path('', home, name="home"),
    path('agregar/', agregar, name="agregar"),
    path('pieza/<int:id>/', detalle_pieza, name='detalle_pieza'),  # Nueva ruta
    path('listado-piezas/', listado_piezas, name="listado_piezas"),
    path('actualizar-img/<id>/', actualizar_img , name="actualizar_img"),
    path('actualizar-desc/<id>/', actualizar_desc, name='actualizar_desc'),
    path('eliminar-pieza/<id>/', eliminar_pieza, name='eliminar_pieza'),
   
]
