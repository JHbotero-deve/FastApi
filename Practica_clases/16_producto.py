class Producto:
    _contador = 0

    def __init__(self, nombre, precio):
        if not Producto.es_precio_valido(precio):
            raise ValueError("El precio debe ser mayor a cero")
        self.nombre = nombre
        self.precio = precio
        Producto._contador += 1

    @classmethod
    def total_productos(cls):
        return cls._contador

    @staticmethod
    def es_precio_valido(precio):
        return precio > 0


if __name__ == '__main__':
    p1 = Producto("Lapicero", 1.5)
    p2 = Producto("Cuaderno", 3.2)
    print("Total productos creados:", Producto.total_productos())
    print("Precio válido (0):", Producto.es_precio_valido(0))
    print("Precio válido (5):", Producto.es_precio_valido(5))
