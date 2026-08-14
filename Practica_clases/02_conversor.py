def pedir_numero(mensaje: str) -> float:
    """Pide un valor por consola y asegura que sea un número válido."""
    return float(input(mensaje).strip())


def main():
    try:
        n1 = pedir_numero("Ingrese primer número: ")
        n2 = pedir_numero("Ingrese segundo número: ")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return

    print(f"Suma: {n1 + n2}")
    print(f"Resta: {n1 - n2}")
    print(f"Multiplicación: {n1 * n2}")
    print(f"División: {n1 / n2}" if n2 != 0
          else "División: No se puede dividir entre cero.")


if __name__ == "__main__":
    main()
