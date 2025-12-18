from django.contrib import admin
from .models import Cliente, Servicio, Turno

admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Turno)
