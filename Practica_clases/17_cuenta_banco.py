class CuentaBanco:
    def __init__(self, titular, balance=0.0):
        self.titular = titular
        self.__balance = float(balance)

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor que cero")
        self.__balance += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero")
        if cantidad > self.__balance:
            raise ValueError("Fondos insuficientes")
        self.__balance -= cantidad

    def revisar_saldo(self):
        return self.__balance

    def aplicar_interes(self, tasa):

        if tasa < 0:
            raise ValueError("La tasa no puede ser negativa")
        self.__balance *= (1 + tasa)


if __name__ == '__main__':
    cuenta = CuentaBanco('Luis', balance=1000)
    print('Saldo inicial:', cuenta.revisar_saldo())
    cuenta.depositar(200)
    print('Saldo tras depósito:', cuenta.revisar_saldo())
    cuenta.retirar(150)
    print('Saldo tras retiro:', cuenta.revisar_saldo())
    cuenta.aplicar_interes(0.05)
    print('Saldo tras aplicar interés 5%:', round(cuenta.revisar_saldo(), 2))
