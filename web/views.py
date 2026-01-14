from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm, ServicioForm, TurnoForm

# Vista principal del sitio
def inicio(request):
    return render(request, 'web/inicio.html')

# Para buscar clientes por nombre
def buscar_cliente(request):
    clientes = []

    if request.GET.get('nombre'):
        clientes = Cliente.objects.filter(
            nombre__icontains=request.GET.get('nombre')
        )

    return render(
        request,
        'web/buscar_cliente.html',
        {'clientes': clientes}
    )

# Para crear un nuevo cliente
def crear_cliente(request):

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'web/cliente_creado.html')
    else:
        form = ClienteForm()

    return render(request, 'web/crear_cliente.html', {'form': form})

# Para crear un nuevo servicio
def crear_servicio(request):

    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'web/servicio_creado.html')
    else:
        form = ServicioForm()

    return render(request, 'web/crear_servicio.html', {'form': form})

# Para creaar un nuevo turno
def crear_turno(request):

    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'web/turno_creado.html')
    else:
        form = TurnoForm()

    return render(request, 'web/crear_turno.html', {'form': form})


from django.shortcuts import render

def about(request):
    return render(request, "web/about.html")
