from django.contrib import admin

# Register your models here.

from .models import Agregar, Elemento, Notificacion

#Para que tambien se registre en Django Admin
admin.site.register(Agregar)
admin.site.register(Elemento)
admin.site.register(Notificacion)