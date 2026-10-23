
"""
Ejercicio 5: Funciones que calculan el subtotal y el total de una compra con descuento e impuesto.

ENTRADA
- base: precio original en pesos.
- descuento: porcentaje de descuento aplicado.
- impuesto: porcentaje de impuesto aplicado al subtotal.

PROCESO
- Crear una funcion que calcule el subtotal despues del descuento.
- Multiplicar la base por (1 - descuento / 100).
- Crear una funcion que calcule el total con impuesto.
- Multiplicar el subtotal por (1 + impuesto / 100).
- Utilizar el subtotal obtenido como parametro de la segunda funcion.

SALIDA
- Mostrar el subtotal despues del descuento.
- Mostrar el total despues de aplicar el impuesto.
"""

def subtotal_descontado(base: float, descuento: float) -> float:
    subtotal = base * (1 - descuento / 100)
    return subtotal

def total_con_impuesto(subtotal: float, impuesto: float) -> float:
    total = subtotal * (1 + impuesto / 100)
    return total

base = float(input("Ingrese el precio original: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
impuesto = float(input("Ingrese el porcentaje de impuesto: "))

subtotal = subtotal_descontado(base, descuento)
total = total_con_impuesto(subtotal, impuesto)

print("Subtotal despues del descuento:", subtotal, "pesos")
print("Total con impuesto:", total, "pesos")
