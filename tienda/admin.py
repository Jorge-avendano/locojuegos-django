from django.contrib import admin
from .models import Producto, Etiqueta

# Personalizamos la forma en que se muestra Producto en el panel Admin
class ProductoAdmin(admin.ModelAdmin):
    # Definimos qué columnas verás en la lista del panel de administración
    list_display = ('nombre', 'plataforma', 'precio', 'descuento', 'precio_final')

    # Esto crea el selector con dos cajas y flechas de traspaso
    filter_horizontal = ('etiquetas',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Etiqueta)