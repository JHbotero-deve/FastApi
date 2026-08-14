contactos = {
    "Ana": {"telefono": "123456789", "correo": "ana@mail.com"},
    "Carlos": {"telefono": "987654321", "correo": "carlos@mail.com"},
    "Laura": {"telefono": "555666777", "correo": "laura@mail.com"}
}

# Agregar un contacto nuevo
contactos["Jorge"] = {"telefono": "111222333", "correo": "jorgeh@ggmail.com"}
contactos["María"] = {"telefono": "444555666", "correo": "maria@mail.com"}
# Actualizar el teléfono de un contacto existente

contactos["Jorge"]["correo"] = "holllalall@gmail.com"
contactos["María"]["telefono"] = "777888999"

# Recorrer el diccionario e imprimir cada contacto usando .items()
print("Agenda de contactos:")
for nombre, datos in contactos.items():
    print(
        f"{nombre}, telefono: {datos['telefono']}, Correo: {datos['correo']}")
