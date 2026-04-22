#carlos alexis peña contreras
import statistics

numeros = []

try:
    for i in range(5):
        n = float(input("Ingresa un número: "))
        numeros.append(n)

    promedio = statistics.mean(numeros)
    print("El promedio es:", promedio)

except ValueError:
    print("Error: debes ingresar solo números")
