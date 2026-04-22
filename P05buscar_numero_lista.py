#carlos alexis peña contreras
numeros = [5, 9, 14, 22, 30]
buscar = int(input("¿Qué número quieres buscar?: "))

# FOR
encontrado_for = False
for n in numeros:
    if n == buscar:
        encontrado_for = True
        break
print("Encontrado con FOR:", encontrado_for)

# WHILE
encontrado_while = False
i = 0
while i < len(numeros):
    if numeros[i] == buscar:
        encontrado_while = True
        break
    i += 1
print("Encontrado con WHILE:", encontrado_while)