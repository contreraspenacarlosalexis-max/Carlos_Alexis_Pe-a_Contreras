#carlos alexis peña contreras
# Pedir el número
numero = float(input("Ingresa un número: "))

# Condiciones usando AND, OR y NOT
if numero > 0 and not (numero == 0):
    print("El número es positivo")
elif numero < 0 or not (numero > 0):
    if numero < 0:
        print("El número es negativo")
    else:
        print("El número es cero")
