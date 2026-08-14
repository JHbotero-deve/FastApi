def agregar_producto(productos, nombre, precio):
    productos.append({
        'nombre': nombre,
        'precio': float(precio)
    })


def calcular_total(productos):
    return sum(p['precio'] for p in productos)
