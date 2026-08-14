numero = int(input("Ingresa un número: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

print(f"Tabla de multiplicar del {numero} con enumerate():")
for fila, i in enumerate(range(1, 11), start=1):
    print(f"{numero} x {i} = {numero * i}")
