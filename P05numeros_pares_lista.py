#carlos alexis peña contreras
numeros = [3, 8, 15, 20, 7, 12]

# FOR
pares_for = 0
for n in numeros:
    if n % 2 == 0:
        pares_for += 1
print("Pares con FOR:", pares_for)

# WHILE
pares_while = 0
i = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        pares_while += 1
    i += 1
print("Pares con WHILE:", pares_while)