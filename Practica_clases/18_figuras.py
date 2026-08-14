from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


if __name__ == '__main__':
    figuras = [Circulo(3), Rectangulo(4, 5), Circulo(1.5)]
    for f in figuras:
        print(f"Área de {f.__class__.__name__}: {f.area():.4f}")
