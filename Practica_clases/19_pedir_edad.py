class EdadInvalidaError(ValueError):
    pass


def pedir_edad(prompt_input=None):
    try:
        if prompt_input is None:
            raw = input("Ingrese su edad: ")
        else:
            raw = str(prompt_input)
        edad = int(raw)
        if edad < 0:
            raise EdadInvalidaError("La edad no puede ser negativa")
    except ValueError:
        print("Valor no válido: debe ingresar un número entero")
        return None
    except EdadInvalidaError as e:
        print(e)
        return None
    else:
        print("Edad válida ingresada:", edad)
        return edad
    finally:
        print("Intento de validación finalizado")


if __name__ == '__main__':

    pedir_edad('25')
    pedir_edad('-3')
    pedir_edad('no es un numero')
