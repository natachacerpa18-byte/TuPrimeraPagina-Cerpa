from django.urls import path
from .views import inicio, buscar_cliente

urlpatterns = [
    path('', inicio, name='inicio'),
    path('buscar-cliente/', buscar_cliente, name='buscar_cliente'),
]
