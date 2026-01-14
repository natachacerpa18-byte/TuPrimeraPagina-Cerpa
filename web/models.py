from django.db import models
from ckeditor.fields import RichTextField

# Modelo que representa a los clientes del centro de masajes
class Cliente(models.Model): 
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self): # Método para que Django muestre un nombre legible en el admin
        return self.nombre

# Modelo que representa los distintos servicios de masajes
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre

# Modelo que representa los turnos reservados, este relaciona un cliente con un servicio
class Turno(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.cliente} - {self.fecha}"

class Page(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='pages/')
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo