import time
from functools import wraps


def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio:.4f} s")
        return resultado
    return wrapper


@medir_tiempo
def calculo_largo(n=200_000):
    total = 0
    for i in range(n):
        total += i
    return total


if __name__ == '__main__':
    print("Ejecutando cálculo largo (demo medir_tiempo)...")
    _ = calculo_largo()
