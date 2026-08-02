from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView #Importacion para la autenticación
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nintendo/', views.nintendo, name='nintendo'),
    path('playstation/', views.playstation, name='playstation'),
    path('xbox/', views.xbox, name='xbox'),
    path('pc/', views.pc, name='pc'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('contacto/', views.contacto, name='contacto'),

    # ruta para la barra de busqueda
    path('buscar/', views.buscar, name='buscar'), 

    # Rutas de Autenticación
    path('login/', LoginView.as_view(template_name='login/index.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    # Ruta de registro
    path('registro/', views.registro, name='registro'),

    # Rutas del Carrito de Compras
    path('agregar/<int:producto_id>/', views.agregar_producto, name='Add'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='Del'),
    path('restar/<int:producto_id>/', views.restar_producto, name='Sub'),
    path('limpiar/', views.limpiar_carrito, name='CLS'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),

    # Rutas de compra e historial
    path('procesar-pago/', views.procesar_pago, name='procesar_pago'),
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),
]