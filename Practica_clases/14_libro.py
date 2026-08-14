class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def resumen(self):
        return f"{self.titulo}, de {self.autor} ({self.paginas} páginas)"


if __name__ == '__main__':
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    print(libro1.resumen())
    print(libro2.resumen())
