
"""
Ejercicio 2: Comparar el precio por gramo de dos paquetes.

ENTRADA
- precio1: precio total del primer paquete en pesos.
- gramos1: cantidad en gramos del primer paquete.
- precio2: precio total del segundo paquete en pesos.
- gramos2: cantidad en gramos del segundo paquete.

PROCESO
- Crear una funcion que calcule el precio por gramo.
- Calcular el precio por gramo de ambos paquetes.
- Comparar los dos precios obtenidos.
- Indicar cual paquete es mas economico o si cuestan igual por gramo.

SALIDA
- Mostrar el precio por gramo de cada paquete.
- Indicar cual paquete es mas economico o si hay igualdad.
"""

def precio_por_gramo(precio: float, gramos: float) -> float:
    precio_gramo = precio / gramos
    return precio_gramo

precio1 = float(input("Ingrese el precio del primer paquete: "))
gramos1 = float(input("Ingrese los gramos del primer paquete: "))

precio2 = float(input("Ingrese el precio del segundo paquete: "))
gramos2 = float(input("Ingrese los gramos del segundo paquete: "))

valor1 = precio_por_gramo(precio1, gramos1)
valor2 = precio_por_gramo(precio2, gramos2)

print("Precio por gramo del paquete 1:", valor1, "pesos")
print("Precio por gramo del paquete 2:", valor2, "pesos")

if valor1 < valor2:
    print("El paquete 1 es mas economico.")
elif valor2 < valor1:
    print("El paquete 2 es mas economico.")
else:
    print("Los dos paquetes cuestan igual por gramo.")
