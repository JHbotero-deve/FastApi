class Empleado:
    def __init__(self, nombre, horas=0, salario=0):
        self.nombre = nombre
        self._horas_trabajadas = horas
        self.__salario = salario

    def _registrar_horas(self, cantidad):
        self._horas_trabajadas += cantidad

    def __calcular_bono(self):
        return self.__salario * 0.1

    def mostrar_bono(self):
        return self.__calcular_bono()


if __name__ == '__main__':
    emp = Empleado("Alicia", horas=40, salario=5000)
    emp._registrar_horas(5)
    print(f"Empleado: {emp.nombre}, horas:{emp._horas_trabajadas}")
    print("Bono (método público):", emp.mostrar_bono())
    print("Salarioprivado (accedido externamente):", emp._Empleado__salario)
