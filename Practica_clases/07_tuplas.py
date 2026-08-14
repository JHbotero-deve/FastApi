meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

print("Tupla de meses:", meses)

mes_Usuario = input("Ingrese un mes: ")
posicion = meses.index(mes_Usuario)
print(f"La posición del mes {mes_Usuario} es: {posicion}")


conteo = meses.count(mes_Usuario)
print(f"El mes {mes_Usuario} aparece {conteo} veces en la tupla.")

try:
    meses[7] = "EneroNuevo"
except TypeError as e:
    print("Error al intentar modificar la tupla:", e)
