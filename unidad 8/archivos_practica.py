
# Práctica Programación 1 - Archivos

import os

ARCHIVO = "productos.txt"

def crear_archivo_inicial():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.write("Lapicera,120.5,30\n")
            f.write("Cuaderno,350.0,15\n")
            f.write("Regla,90.0,25\n")

def leer_productos():
    productos = []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            nombre, precio, cantidad = linea.strip().split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
    return productos

def mostrar_productos(productos):
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

def agregar_producto(nombre, precio, cantidad):
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{precio},{cantidad}\n")

def buscar_producto(productos, nombre_buscar):
    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            return p
    return None

def guardar_productos(productos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

def programa_principal():
    crear_archivo_inicial()

    productos = leer_productos()
    print("PRODUCTOS ACTUALES:")
    mostrar_productos(productos)

    print("\nAgregar nuevo producto:")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    agregar_producto(nombre, precio, cantidad)

    # recargar
    productos = leer_productos()

    print("\nLista actualizada:")
    mostrar_productos(productos)

    nombre_buscar = input("\nIngresá un nombre para buscar: ")
    encontrado = buscar_producto(productos, nombre_buscar)
    if encontrado:
        print("ENCONTRADO:", encontrado)
    else:
        print("Producto no encontrado.")

    guardar_productos(productos)

if __name__ == "__main__":
    programa_principal()
