from django.shortcuts import render
from .models import Cliente

def inicio(request):
    return render(request, 'web/inicio.html')

def buscar_cliente(request):
    clientes = []
    if request.GET.get('nombre'):
        clientes = Cliente.objects.filter(nombre__icontains=request.GET.get('nombre'))
    return render(request, 'web/buscar_cliente.html', {'clientes': clientes})
