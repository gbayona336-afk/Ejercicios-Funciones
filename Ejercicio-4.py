
"""
Ejercicio 4: Funcion que calcula el pago semanal de dos personas

ENTRADA
- horas1: horas trabajadas por la primera persona.
- tarifa1: pago por hora de la primera persona.
- horas2: horas trabajadas por la segunda persona.
- tarifa2: pago por hora de la segunda persona.

PROCESO
- Crear una funcion que reciba las horas y la tarifa.
- Si las horas son menores o iguales a 40, multiplicar horas por tarifa.
- Si las horas superan 40, pagar las primeras 40 horas normalmente.
- Pagar las horas adicionales a 1.5 veces la tarifa.
- Calcular el pago de las dos personas y sumar los resultados.

SALIDA
- Mostrar el pago semanal de cada persona.
- Mostrar el total de los dos pagos en pesos.
"""

def pago_semanal(horas: float, tarifa: float) -> float:
    if horas <= 40:
        pago = horas * tarifa
    else:
        pago = 40 * tarifa + (horas - 40) * tarifa * 1.5
    return pago

horas1 = float(input("Ingrese las horas de la primera persona: "))
tarifa1 = float(input("Ingrese la tarifa por hora de la primera persona: "))

horas2 = float(input("Ingrese las horas de la segunda persona: "))
tarifa2 = float(input("Ingrese la tarifa por hora de la segunda persona: "))

pago1 = pago_semanal(horas1, tarifa1)
pago2 = pago_semanal(horas2, tarifa2)

total = pago1 + pago2

print("Pago de la primera persona:", pago1, "pesos")
print("Pago de la segunda persona:", pago2, "pesos")
print("Total de los pagos:", total, "pesos")
