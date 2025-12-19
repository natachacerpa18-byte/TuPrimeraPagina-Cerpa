from django.contrib import admin
from .models import Cliente, Servicio, Turno

# Registro de los modelos para poder administrarlos desde el panel de Django
admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Turno)
