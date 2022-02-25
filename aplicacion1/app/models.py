from msilib.schema import Class
from pyexpat import model
from turtle import mode
from django.db import models
#6.- Agregar librerias
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#7.- crea la tabla
#8.- Quien crea el registro
class Producto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField()
    
    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
#9.- creacion de una clase
class Sandwitchs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    producto = models.ManyToManyField(Producto)

    class Meta:
        ordering = ['nombre']

    def get_productos(self):
        return "\n".join([p.nombre for p in self.producto.all()])
    
    def __str__(self):
        return self.nombre

class Precios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sandwich = models.ForeignKey(Sandwitchs, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ganancia = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    FechaIngresado = models.DateField(auto_now_add=True)

    def calculate(self):
        total = 0
        imp =1/2
        productos =self.sandwich.producto.all()
        for producto in productos:
            costo = producto.costo
            total += costo
        totalFloat = float(total)
        gananciaP = totalFloat * imp
        self.ganancia = gananciaP
        self.ganancia = totalFloat + gananciaP
        self.save()
        return ":"

    def __str__(self):
        return self.sandwich.nombre