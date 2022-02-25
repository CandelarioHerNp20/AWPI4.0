from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect


from .models import Producto, Sandwitchs, Precios
# Create your views here.
# redireccion a los templates html

def preciosL(request):
    lista = Precios.objects.order_by('-FechaIngresado')
    return render(request, 'precio/preciosL.html', {'precios': lista})