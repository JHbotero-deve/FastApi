import datetime

while True:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Ver hora")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("------------------------¡Hola! Espero que tengas un gran día------------------------")
    elif opcion == "2":
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        print("------------------------La hora actual es:",
              hora_actual, "------------------------")
    elif opcion == "3":
        print(".................................Saliendo del programa...........................")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
        continue
