#carlos alexis peña contreras
# Pedir el número
numero = int(input("Ingresa un número: "))

# Condiciones usando AND, OR y NOT
if numero % 2 == 0 and not (numero % 2 != 0):
    print("El número es par")
elif numero % 2 != 0 or not (numero % 2 == 0):
    print("El número es impar")