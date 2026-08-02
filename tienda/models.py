from django.db import models

# Creamos la tabla para los tags de los productos
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(
        max_length=20,
        default="primary",
        help_text="Color Bootstrap (ej: primary, success, warning, danger, info)"
    )

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    # Opciones para el menu desplegable en el panel de administrador

    CONSOLAS = (
        ('PS', 'Playstation'),
        ('XB', 'Xbox'),
        ('NT', 'Nintendo'),
        ('PC', 'PC'),
    )

    # CREAMOS LAS OPCIONES DE SECCIONES (ESTO SE USARA PARA CADA PLATAFORMA)
    SECCIONES_TIENDA = (
        ('DEST', 'Juegos Destacados'),
        ('ACC', 'Acción'),
        ('ADV', 'Aventura'),
        ('DEP', 'Deportes'),
    )

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    # Campo numerico para el % de descuento
    descuento = models.IntegerField(default=0, help_text="Porcentaje de descuento (ejemplo: 20 para 20%)")

    plataforma = models.CharField(max_length=2, choices=CONSOLAS)

    seccion = models.CharField(max_length=4, choices=SECCIONES_TIENDA, default='DEST')

    # Campo para subir la portada del juego
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    # Campo para conectar los tags (Etiquetas)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    # Propiedad calculada: El administrador pone el %, y Django calcula el precio final en automatico
    @property
    def precio_final(self):
        if self.descuento > 0:
            rebaja = (self.precio * self.descuento) / 100
            return round(self.precio - rebaja, 2)
        return self.precio

    def __strt__(self):
        return f"{self.conmbre} - {self.get_plataforma_display()}"
