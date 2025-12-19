from django import forms
from .models import Cliente, Servicio, Turno


# Formulario para cargar clientes
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


# Formulario para cargar servicios
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'


# Formulario para cargar turnos
class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
