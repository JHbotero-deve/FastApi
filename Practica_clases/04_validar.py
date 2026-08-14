# 4. Validador de acceso(operadores lógicos)
#   Crea variables tiene_usuario, tiene_clave_correcta y cuenta_bloqueada. Usando and , or y not, imprime
# " Acceso concedido" solo si el usuario tiene usuario y clave correctos y la cuenta no está bloqueada; en
#   cualquier otro caso imprime "Acceso denegado". Agrega un ejemplo de corto-circuito similar al de
#    4_operadores_logicos.py.
from subprocess import run
run("cls", shell=True)

tiene_usuario = False
tiene_clave_correcta = True
cuenta_bloqueada = False

if tiene_usuario and tiene_clave_correcta and not cuenta_bloqueada:
    print("Acceso concedido")
else:
    print("Acceso denegado")

# Ejemplo de corto circuito con and y not
# Si el primer valor es False, Python no evalúa el segundo operando de and.
# Esto evita llamadas innecesarias cuando ya se sabe que la expresión será False.


def verificar_usuario():
    print("Verificando usuario...")
    return tiene_usuario


def verificar_clave():
    print("Verificando clave...")
    return tiene_clave_correcta


if verificar_usuario() and verificar_clave() and not cuenta_bloqueada:
    print("Acceso concedido (corto circuito)")
else:
    print("Acceso denegado (corto circuito)")
