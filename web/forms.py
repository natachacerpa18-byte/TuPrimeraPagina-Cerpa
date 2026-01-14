from django import forms
from .models import Cliente, Servicio, Turno


# Formulario para cargar clientes
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "email", "telefono"]


# Formulario para cargar servicios
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ["nombre", "precio"]


# Formulario para cargar turnos
class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ["cliente", "servicio", "fecha"]
