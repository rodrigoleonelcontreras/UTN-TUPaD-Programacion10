# TP Estructuras Repetitivas - Soluciones

import random

def ejercicio1():
    for i in range(101):
        print(i)

def ejercicio2():
    n = input("Ingrese un número entero: ")
    print("Cantidad de dígitos:", len(n))

def ejercicio3():
    a = int(input("Primer valor: "))
    b = int(input("Segundo valor: "))
    suma = 0
    for i in range(a+1, b):
        suma += i
    print("Suma:", suma)

def ejercicio4():
    total = 0
    while True:
        n = int(input("Ingrese un número (0 para terminar): "))
        if n == 0:
            break
        total += n
    print("Total acumulado:", total)

def ejercicio5():
    numero = random.randint(0,9)
    intentos = 0
    while True:
        intento = int(input("Adivine el número (0–9): "))
        intentos += 1
        if intento == numero:
            break
        print("Incorrecto, intente nuevamente.")
    print("Correcto! Intentos:", intentos)

def ejercicio6():
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)

def ejercicio7():
    n = int(input("Ingrese un número entero positivo: "))
    total = 0
    for i in range(n+1):
        total += i
    print("Suma:", total)

def ejercicio8():
    pares = impares = positivos = negativos = 0
    cantidad = 100
    for _ in range(cantidad):
        n = int(input("Ingrese un número: "))
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
        if n >= 0:
            positivos += 1
        else:
            negativos += 1
    print("Pares:", pares)
    print("Impares:", impares)
    print("Positivos:", positivos)
    print("Negativos:", negativos)

def ejercicio9():
    cantidad = 100
    total = 0
    for _ in range(cantidad):
        n = int(input("Ingrese un número: "))
        total += n
    print("Media:", total/cantidad)

def ejercicio10():
    n = input("Ingrese un número: ")
    print("Invertido:", n[::-1])
