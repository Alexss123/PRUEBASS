# Programa que convierte minutos a horas y minutos

# Función principal
def convertir_minutos_a_horas(minutos):
    horas = minutos // 60  # Calcular horas
    minutos_restantes = minutos % 60  # Calcular minutos restantes
    return horas, minutos_restantes

# Solicitar al usuario la cantidad de minutos
try:
    cantidad_minutos = int(input("Ingrese la cantidad de minutos: "))
    if cantidad_minutos < 0:
        print("Por favor, ingrese un número positivo.")
    else:
        # Convertir y mostrar el resultado
        horas, minutos_restantes = convertir_minutos_a_horas(cantidad_minutos)
        print(f"{cantidad_minutos} minutos son {horas} horas y {minutos_restantes} minutos.")
except ValueError:
    print("Por favor, ingrese un número válido.")
