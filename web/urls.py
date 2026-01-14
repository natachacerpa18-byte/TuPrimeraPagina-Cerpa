from django.urls import path
from .views import (
    inicio,
    buscar_cliente,
    crear_cliente,
    crear_servicio,
    crear_turno,
    about,
)

urlpatterns = [
    path("", inicio, name="inicio"),
    path("buscar-cliente/", buscar_cliente, name="buscar_cliente"),
    path("crear-cliente/", crear_cliente, name="crear_cliente"),
    path("crear-servicio/", crear_servicio, name="crear_servicio"),
    path("crear-turno/", crear_turno, name="crear_turno"),
    path("about/", about, name="about"),
]
