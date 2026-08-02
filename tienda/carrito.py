class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, producto):
        id_producto = str(producto.id)
        # Si el producto NO está en el carrito, lo creamos con cantidad 1
        if id_producto not in self.carrito.keys():
            self.carrito[id_producto] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio_final": float(producto.precio_final),
                "cantidad": 1,
                "acumulado": float(producto.precio_final), # El total por este juego
                "imagen": producto.imagen.url if producto.imagen else "",
            }
        # Si YA ESTÁ en el carrito, le sumamos 1 a la cantidad y actualizamos el acumulado
        else:
            self.carrito[id_producto]["cantidad"] += 1
            self.carrito[id_producto]["acumulado"] += float(producto.precio_final)
        self.guardar()

    def restar(self, producto):
        id_producto = str(producto.id)
        if id_producto in self.carrito.keys():
            self.carrito[id_producto]["cantidad"] -= 1
            self.carrito[id_producto]["acumulado"] -= float(producto.precio_final)
            
            # Si la cantidad llega a 0 o menos, lo borramos de la mochila
            if self.carrito[id_producto]["cantidad"] <= 0:
                self.eliminar(producto)
            else:
                self.guardar()

    def eliminar(self, producto):
        id_producto = str(producto.id)
        if id_producto in self.carrito:
            del self.carrito[id_producto]
            self.guardar()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True