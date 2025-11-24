
# TP 5 - Listas - Soluciones

import random

def ejercicio1():
    notas = []
    for i in range(10):
        nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
        notas.append(nota)

    print("Notas ingresadas:")
    for n in notas:
        print(n)

    promedio = sum(notas) / len(notas)
    print("Promedio:", promedio)
    print("Nota más alta:", max(notas))
    print("Nota más baja:", min(notas))


def ejercicio2():
    productos = []
    for i in range(5):
        prod = input(f"Ingrese el producto {i+1}: ")
        productos.append(prod)

    print("Lista ordenada:", sorted(productos))

    eliminar = input("¿Qué producto desea eliminar?: ")
    if eliminar in productos:
        productos.remove(eliminar)
    print("Lista actualizada:", productos)


def ejercicio3():
    lista = [random.randint(1, 100) for _ in range(15)]
    pares = []
    impares = []

    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    print("Cantidad de pares:", len(pares))
    print("Cantidad de impares:", len(impares))


def ejercicio4():
    lista = [1, 2, 2, 3, 4, 4, 5, 1]
    sin_repetidos = []

    for n in lista:
        if n not in sin_repetidos:
            sin_repetidos.append(n)

    print("Lista sin repetidos:", sin_repetidos)


def ejercicio5():
    estudiantes = []
    for i in range(8):
        nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
        estudiantes.append(nombre)

    opcion = input("¿Desea agregar(A) o eliminar(E) un estudiante?: ").upper()

    if opcion == "A":
        nuevo = input("Nombre del nuevo estudiante: ")
        estudiantes.append(nuevo)
    elif opcion == "E":
        elim = input("Nombre del estudiante a eliminar: ")
        if elim in estudiantes:
            estudiantes.remove(elim)

    print("Lista final:", estudiantes)


def ejercicio6():
    lista = [3, 8, 1, 9, 7, 4, 2]
    lista_rotada = [lista[-1]] + lista[:-1]
    print("Lista rotada:", lista_rotada)


def ejercicio7():
    matriz = []
    for i in range(7):
        minima = float(input(f"Temperatura mínima del día {i+1}: "))
        maxima = float(input(f"Temperatura máxima del día {i+1}: "))
        matriz.append([minima, maxima])

    prom_min = sum([fila[0] for fila in matriz]) / 7
    prom_max = sum([fila[1] for fila in matriz]) / 7

    print("Promedio mínimas:", prom_min)
    print("Promedio máximas:", prom_max)

    amplitudes = [fila[1] - fila[0] for fila in matriz]
    dia_max_amp = amplitudes.index(max(amplitudes)) + 1
    print("Día con mayor amplitud térmica:", dia_max_amp)


def ejercicio8():
    matriz = []
    for i in range(5):
        fila = []
        for j in range(3):
            nota = float(input(f"Nota del estudiante {i+1}, materia {j+1}: "))
            fila.append(nota)
        matriz.append(fila)

    print("Promedio por estudiante:")
    for i in range(5):
        print(f"Estudiante {i+1}: {sum(matriz[i]) / 3}")

    print("Promedio por materia:")
    for j in range(3):
        promedio = sum([matriz[i][j] for i in range(5)]) / 5
        print(f"Materia {j+1}: {promedio}")


def ejercicio9():
    tablero = [["-" for _ in range(3)] for _ in range(3)]

    turno = "X"

    for _ in range(9):
        print("Tablero actual:")
        for fila in tablero:
            print(fila)

        fila = int(input(f"Jugador {turno}, ingrese fila (0-2): "))
        col = int(input(f"Jugador {turno}, ingrese columna (0-2): "))

        if tablero[fila][col] == "-":
            tablero[fila][col] = turno
        else:
            print("Casilla ocupada, pierdes el turno.")

        turno = "O" if turno == "X" else "X"

    print("Tablero final:")
    for fila in tablero:
        print(fila)


def ejercicio10():
    matriz = []
    for i in range(4):
        fila = []
        for j in range(7):
            venta = float(input(f"Ingrese ventas del producto {i+1}, día {j+1}: "))
            fila.append(venta)
        matriz.append(fila)

    print("Total vendido por cada producto:")
    for i in range(4):
        print(f"Producto {i+1}: {sum(matriz[i])}")

    totales_por_dia = [sum([matriz[i][j] for i in range(4)]) for j in range(7)]
    dia_max_ventas = totales_por_dia.index(max(totales_por_dia)) + 1
    print("Día con mayores ventas totales:", dia_max_ventas)

    totales_producto = [sum(matriz[i]) for i in range(4)]
    prod_max = totales_producto.index(max(totales_producto)) + 1
    print("Producto más vendido:", prod_max)
