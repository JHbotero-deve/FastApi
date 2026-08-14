tareas = []


tareas.append("Comprar leche")
tareas.append("Estudiar Python")
tareas.append("Llamar a la mamá")
tareas.append("Pagar la luz")
tareas.append("Hacer ejercicio")
tareas.append("Estudiar Python")
tareas.append("Leer un libro")
tareas.append("Estudiar Python")
tareas.append("Pagar la luz")
tareas.append("Pagar la luz")
tareas.append("Hacer ejercicio")

print("Lista de tareas:", tareas)

tareas.remove("Comprar leche")

print("Lista de tareas después de eliminar 'Comprar leche':", tareas)


repetidos = tareas.count("Estudiar Python")
print("Número de veces que 'Estudiar Python' aparece en la lista:", repetidos)


lista_ordenada = sorted(tareas)
print("Lista de tareas ordenada alfabéticamente:", lista_ordenada)

print("Lista de tareas original:", tareas)
