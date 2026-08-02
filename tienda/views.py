from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .carrito import Carrito


from .models import Producto

def inicio(request):
    # Traemos todos los productos
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def nintendo(request):
    # Traemos TODOS los juegos que sean solo de Nintendo
    juegos_nt = Producto.objects.filter(plataforma='NT')
    
    # Los filtramos en variables separadas
    contexto = {
        'destacados': juegos_nt.filter(seccion='DEST'),
        'accion': juegos_nt.filter(seccion='ACC'),
        'aventura': juegos_nt.filter(seccion='ADV'),
        'deportes': juegos_nt.filter(seccion='DEP'),
        
        # Filtra cualquier juego que tenga descuento mayor a 0, sin importar su sección
        'ofertas': juegos_nt.filter(descuento__gt=0),
    }
    
    # Enviamos el contexto al HTML
    return render(request, 'catalogo/nintendo/index.html', contexto)

def playstation(request):

    # Traemos TODOS los juegos que sean solo de PS
    juegos_ps = Producto.objects.filter(plataforma='PS')
       
    # Los filtramos en variables separadas 
    contexto = {
        'destacados': juegos_ps.filter(seccion='DEST'),
        'accion': juegos_ps.filter(seccion='ACC'),
        'aventura': juegos_ps.filter(seccion='ADV'),
        'deportes': juegos_ps.filter(seccion='DEP'),
           
        # Filtra cualquier juego de Nintendo que tenga descuento mayor a 0, sin importar su sección
        'ofertas': juegos_ps.filter(descuento__gt=0),
    }

    # Enviamos el contexto al HTML
    return render(request, 'catalogo/play-station/index.html', contexto)

def xbox(request):
    # Traemos TODOS los juegos que sean solo de XB
    juegos_xb = Producto.objects.filter(plataforma='XB')
           
    # Los filtramos en variables separadas       
    contexto = {
            'destacados': juegos_xb.filter(seccion='DEST'),
            'accion': juegos_xb.filter(seccion='ACC'),
            'aventura': juegos_xb.filter(seccion='ADV'),
            'deportes': juegos_xb.filter(seccion='DEP'),
               
            # Filtra cualquier juego de Nintendo que tenga descuento mayor a 0, sin importar su sección
            'ofertas': juegos_xb.filter(descuento__gt=0),
    }

    # Enviamos el contexto al HTML
    return render(request, 'catalogo/xbox/index.html', contexto)

def pc(request):
    # Traemos TODOS los juegos que sean solo de PC
    juegos_pc = Producto.objects.filter(plataforma='PC')
           
    # Los filtramos en variables separadas       
    contexto = {
            'destacados': juegos_pc.filter(seccion='DEST'),
            'accion': juegos_pc.filter(seccion='ACC'),
            'aventura': juegos_pc.filter(seccion='ADV'),
            'deportes': juegos_pc.filter(seccion='DEP'),
               
            # Filtra cualquier juego de Nintendo que tenga descuento mayor a 0, sin importar su sección
            'ofertas': juegos_pc.filter(descuento__gt=0),
    }

    # Enviamos el contexto al HTML
    return render(request, 'catalogo/pc/index.html', contexto)


def ofertas(request):
    todas_ofertas = Producto.objects.filter(descuento__gt=0)
    
    contexto = {
        'ofertas_nintendo': todas_ofertas.filter(plataforma='NT'),
        'ofertas_playstation': todas_ofertas.filter(plataforma='PS'),
        'ofertas_xbox': todas_ofertas.filter(plataforma='XB'),
        'ofertas_pc': todas_ofertas.filter(plataforma='PC'),
        
    }
    return render(request, 'ofertas/index.html', contexto)

def contacto(request):
    return render(request, 'contacto/index.html')


def buscar(request):
    # 1. Atrapamos lo que el usuario escribió en el input name="q"
    query = request.GET.get('q', '') 
    
    if query:
        # 2. Filtramos la base de datos. 
        # nombre__icontains busca si la palabra está dentro del nombre del juego
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        # Si no escribió nada, devolvemos una lista vacía
        productos = Producto.objects.none()
        
    # 3. Enviamos los resultados a una nueva plantilla
    return render(request, 'buscar/index.html', {
        'productos': productos, 
        'query': query
    })

def registro(request):
    # Si el usuario hace clic en el botón "Registrarse" (envía datos)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save() # Guarda al usuario en la base de datos de SQLite
            login(request, usuario) # Inicia la sesión automáticamente tras registrarse
            return redirect('inicio') # Lo mandamos a la página principal
    else:
        # Si el usuario solo está visitando la página por primera vez
        form = UserCreationForm()
        
    return render(request, 'registro/index.html', {'form': form})

# Manejo del carrito de compras
def agregar_producto(request, producto_id):
    # Instanciar
    carrito = Carrito(request)
    # Buscamos el producto en la base de datos
    producto = Producto.objects.get(id=producto_id)
    
    carrito.agregar(producto)
    
    # Redirigimos al usuario a la misma página donde estaba
    return redirect(request.META.get('HTTP_REFERER', '/'))

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('ver_carrito') 

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('ver_carrito')

def ver_carrito(request):
    # Traemos la mochila de la sesión actual
    carrito = request.session.get('carrito', {})
    
    # Sumamos los precios de todos los productos que están adentro
    total = sum(item['acumulado'] for item in carrito.values())
    
    # Enviamos los datos a una nueva plantilla
    return render(request, 'carrito/index.html', {
        'carrito': carrito,
        'total': total
    })

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('ver_carrito')

