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
]