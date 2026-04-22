#carlos alexis peña contreras
# Pedir la edad
edad = int(input("Ingresa tu edad: "))

# Condiciones usando AND, OR y NOT
if edad >= 18 and not (edad < 0):
    print("Eres mayor de edad")
elif edad < 18 and edad >= 0:
    print("Eres menor de edad")
else:
    print("Edad no válida")
