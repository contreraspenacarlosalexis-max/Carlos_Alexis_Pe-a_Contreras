#carlos alexis peña contreras
import random

numeros = []

try:
    for i in range(5):
        num = random.randint(1, 10)
        numeros.append(num)

    print("Lista:", numeros)
    print("Suma:", sum(numeros))

except:
    print("Ocurrió un error")
