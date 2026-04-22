#carlos alexis peña contreras 
numeros = [10, 20, 30, 40, 50]

# Usando FOR
suma_for = 0
for n in numeros:
    suma_for += n
print("Suma con FOR:", suma_for)

# Usando WHILE
suma_while = 0
i = 0
while i < len(numeros):
    suma_while += numeros[i]
    i += 1
print("Suma con WHILE:", suma_while)