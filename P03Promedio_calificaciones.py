#Carlos Alexis Peña Contreras
# Pedir las 3 calificaciones
cal1 = float(input("Ingresa la primera calificación: "))
cal2 = float(input("Ingresa la segunda calificación: "))
cal3 = float(input("Ingresa la tercera calificación: "))

# Calcular el promedio
promedio = (cal1 + cal2 + cal3) / 3

# Mostrar el promedio
print("Tu promedio es:", promedio)

# Evaluar con if - elif - else
if promedio >= 6:
    print("Aprobado")
elif promedio >= 5:
    print("Recuperación")
else:
    print("Reprobado")
