#carlos alexis peña contreras
try:
    # Pedir dos números
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    # División
    resultado = num1 / num2

    print("El resultado es:", resultado)

except ZeroDivisionError:
    print("Error: no se puede dividir entre 0")

except ValueError:
    print("Error: debes ingresar solo números")

except:
    print("Ocurrió un error inesperado")