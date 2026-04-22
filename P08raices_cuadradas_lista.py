#carlos alexis peña contreras
import math

numeros = []

try:
    for i in range(3):
        n = float(input("Ingresa un número: "))
        numeros.append(n)

    for num in numeros:
        if num >= 0:
            print("Raíz de", num, "=", math.sqrt(num))
        else:
            print("No se puede sacar raíz de número negativo")

except ValueError:
    print("Error: dato inválido")