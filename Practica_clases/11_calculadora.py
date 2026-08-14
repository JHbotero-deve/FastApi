def calculadora(operacion, *numeros, **opciones):
    decimales = opciones.get("decimales", 2)

    if not numeros:
        return round(0, decimales)
    if operacion == "sumar":
        resultado = sum(numeros)
    elif operacion == "restar":
        resultado = numeros[0]
        for n in numeros[1:]:
            resultado -= n
    elif operacion == "multiplicar":
        resultado = 1
        for n in numeros:
            resultado *= n
    elif operacion == "dividir":
        resultado = numeros[0]
        for n in numeros[1:]:
            if n == 0:
                return "Error:división por cero"
            resultado /= n
    else:
        return "Operación no válida"

    return round(resultado, decimales)


print(calculadora("sumar", 100, 200, 3020))
print(calculadora("restar", 100, 20, 30, decimales=3))
print(calculadora("multiplicar", 2, 3, 4))
print(calculadora("dividir", 100, 2, 5, decimales=4))
