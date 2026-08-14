from functools import wraps


def aplicar_descuento(func, precio):
    return func(precio)


def descuento_10(precio):
    return precio * 0.9


def descuento_20(precio):
    return precio * 0.8


def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("[auth] Autenticación simulada: OK")
        return func(*args, **kwargs)
    return wrapper


@require_auth
def demo_descuentos():
    precio = 100.0
    print("Precio original:", precio)
    print("Descuento 10%:", aplicar_descuento(descuento_10, precio))
    print("Descuento 20%:", aplicar_descuento(descuento_20, precio))


if __name__ == '__main__':
    demo_descuentos()
