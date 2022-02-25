from django.contrib import admin
from.models import Producto, Sandwitchs, Precios

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """producto admin"""

    list_display =('id', 'nombre', 'costo', 'cantidad', 'user')

@admin.register(Sandwitchs)
class SandwitchsAdmin(admin.ModelAdmin):
    """Sandwitchs admin"""

    list_display = ('id', 'nombre', 'get_productos', 'user')

@admin.register(Precios)
class Precios(admin.ModelAdmin):
    """Precios admin"""

    list_display = ('id', 'sandwich', 'precio', 'ganancia', 'user')
