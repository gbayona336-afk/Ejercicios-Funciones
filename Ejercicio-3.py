
"""
Ejercico 3: Funciones que verifican si una medicion esta dentro de la tolerancia.

ENTRADA
- objetivo: valor esperado de la medicion.
- tolerancia: margen de error permitido.
- medicion1: primera medicion realizada.
- medicion2: segunda medicion realizada.

PROCESO
- Crear una funcion que calcule el valor absoluto de un numero.
- Crear una funcion que calcule el error entre la medicion y el objetivo.
- Comparar el error con la tolerancia permitida.
- Aceptar la medicion si el error es menor o igual a la tolerancia.
- Consultar las dos mediciones por separado.

SALIDA
- Mostrar si cada medicion es aceptable o no.
"""

def valor_absoluto(numero: float) -> float:
    if numero < 0:
        return -numero
    return numero

def aceptacion(medicion: float, objetivo: float, tolerancia: float) -> bool:
    error = valor_absoluto(medicion - objetivo)
    return error <= tolerancia

objetivo = float(input("Ingrese el objetivo: "))
tolerancia = float(input("Ingrese la tolerancia: "))

medicion1 = float(input("Ingrese la primera medicion: "))
medicion2 = float(input("Ingrese la segunda medicion: "))

resultado1 = aceptacion(medicion1, objetivo, tolerancia)
resultado2 = aceptacion(medicion2, objetivo, tolerancia)

print("Primera medicion aceptable:", resultado1)
print("Segunda medicion aceptable:", resultado2)
