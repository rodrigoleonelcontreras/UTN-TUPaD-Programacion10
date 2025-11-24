
# TP 6 - Estructuras de datos complejas (sin objetos)

# 1) Diccionario inicial
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregar frutas
precios_frutas.update({
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
})

# 2) Actualizar precios
precios_frutas.update({
    'Banana': 1330,
    'Manzana': 1700,
    'Melón': 2800
})

# 3) Lista de frutas sin precios
lista_frutas = list(precios_frutas.keys())

# 4) Agenda telefónica
def agenda_telefonica():
    contactos = {}
    for _ in range(5):
        nombre = input("Nombre: ")
        numero = input("Número: ")
        contactos[nombre] = numero

    consulta = input("Ingresá un nombre para buscar: ")
    if consulta in contactos:
        print("Número:", contactos[consulta])
    else:
        print("No existe el contacto.")

# 5) Procesar frase
def procesar_frase(frase):
    palabras = frase.lower().split()
    unicas = set(palabras)
    conteo = {}
    for p in palabras:
        conteo[p] = conteo.get(p, 0) + 1
    return unicas, conteo

# 6) Notas de alumnos
def notas_alumnos():
    alumnos = {}
    for _ in range(3):
        nombre = input("Alumno: ")
        notas = tuple(float(input("Nota: ")) for _ in range(3))
        alumnos[nombre] = notas

    for nombre, notas in alumnos.items():
        print(nombre, "promedio:", sum(notas)/3)

# 7) Sets de aprobados
def aprobados(p1, p2):
    ambos = p1 & p2
    solo_uno = p1 ^ p2
    total = p1 | p2
    return ambos, solo_uno, total

# 8) Stock
def manejador_stock():
    stock = {}
    while True:
        prod = input("Producto: ")
        if prod in stock:
            cant = int(input("Sumar unidades: "))
            stock[prod] += cant
        else:
            cant = int(input("Nuevo producto. Unidades: "))
            stock[prod] = cant
        print(stock)

# 9) Agenda con tuplas
def agenda_eventos():
    agenda = {}
    while True:
        dia = input("Día: ")
        hora = input("Hora: ")
        evento = input("Evento: ")
        agenda[(dia, hora)] = evento
        print(agenda)

# 10) Invertir diccionario capitales
def invertir(dic):
    return {capital: pais for pais, capital in dic.items()}
