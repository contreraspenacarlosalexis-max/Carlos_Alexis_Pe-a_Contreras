#carlos alexis peña contreras
# Pedir datos
precio = float(input("Ingresa el precio del producto: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

# Validar datos usando AND, OR y NOT
if precio > 0 and descuento >= 0 and not (descuento > 100):
    # Calcular descuento
    descuento_aplicado = precio * (descuento / 100)
    precio_final = precio - descuento_aplicado

    print("El precio final es:", precio_final)
elif precio <= 0 or descuento < 0 or descuento > 100:
    print("Datos no válidos")