
# TP Estructuras Condicionales - Programación 1
# Archivo listo para entregar

def ejercicio_1():
    edad = int(input("Ingrese su edad: "))
    if edad > 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")

def ejercicio_2():
    nota = float(input("Ingrese su nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

def ejercicio_3():
    n = int(input("Ingrese un número (debe ser par): "))
    if n % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

def ejercicio_4():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        categoria = "Niño/a"
    elif 12 <= edad < 18:
        categoria = "Adolescente"
    elif 18 <= edad < 30:
        categoria = "Adulto/a joven"
    else:
        categoria = "Adulto/a"
    print(f"Pertenece a la categoría: {categoria}")

def ejercicio_5():
    pwd = input("Ingrese una contraseña (8 a 14 caracteres): ")
    if 8 <= len(pwd) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

def ejercicio_6():
    consumo = float(input("Ingrese el consumo mensual en kWh: "))
    if consumo < 150:
        categoria = "Consumo bajo"
    elif 150 <= consumo <= 300:
        categoria = "Consumo medio"
    else:
        categoria = "Consumo alto"
    print(categoria)
    if consumo > 500:
        print("Considere medidas de ahorro energético")

def ejercicio_7():
    s = input("Ingrese una frase o palabra: ")
    if s.strip() == "":
        print("(entrada vacía)")
        return
    ultima = s.strip()[-1].lower()
    if ultima in "aeiouáéíóú":
        resultado = s + "!"
    else:
        resultado = s
    print(resultado)

def ejercicio_8():
    nombre = input("Ingrese su nombre: ")
    print("Opciones: 1) MAYÚSCULAS  2) minúsculas  3) Primera letra mayúscula")
    opcion = input("Elija 1, 2 o 3: ").strip()
    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("Opción inválida")

def ejercicio_9():
    mag = float(input("Ingrese la magnitud del terremoto (escala Richter): "))
    if mag < 3:
        cat = "Muy leve (imperceptible)"
    elif 3 <= mag < 4:
        cat = "Leve (ligeramente perceptible)"
    elif 4 <= mag < 5:
        cat = "Moderado (sentido por personas, generalmente no causa daños)"
    elif 5 <= mag < 6:
        cat = "Fuerte (puede causar daños en estructuras débiles)"
    elif 6 <= mag < 7:
        cat = "Muy Fuerte (puede causar daños significativos)"
    else:
        cat = "Extremo (puede causar graves daños a gran escala)"
    print(cat)

def ejercicio_10():
    hemisferio = input("¿En qué hemisferio está? (N/S): ").strip().upper()
    mes = int(input("Ingrese el mes (1-12): "))
    dia = int(input("Ingrese el día (1-31): "))
    mmdd = mes * 100 + dia

    if hemisferio == "N":
        if 321 <= mmdd <= 620:
            estacion = "Primavera"
        elif 621 <= mmdd <= 922:
            estacion = "Verano"
        elif 923 <= mmdd <= 1220:
            estacion = "Otoño"
        else:
            estacion = "Invierno"
    elif hemisferio == "S":
        if 321 <= mmdd <= 620:
            estacion = "Otoño"
        elif 621 <= mmdd <= 922:
            estacion = "Invierno"
        elif 923 <= mmdd <= 1220:
            estacion = "Primavera"
        else:
            estacion = "Verano"
    else:
        print("Hemisferio inválido. Ingrese 'N' o 'S'.")
        return
    print(f"Estación: {estacion}")

def menu():
    opciones = {
        "1": ("Ejercicio 1 - Mayor de edad", ejercicio_1),
        "2": ("Ejercicio 2 - Aprobado/Desaprobado", ejercicio_2),
        "3": ("Ejercicio 3 - Número par", ejercicio_3),
        "4": ("Ejercicio 4 - Categoría por edad", ejercicio_4),
        "5": ("Ejercicio 5 - Longitud contraseña", ejercicio_5),
        "6": ("Ejercicio 6 - Consumo eléctrico", ejercicio_6),
        "7": ("Ejercicio 7 - Frase termina en vocal", ejercicio_7),
        "8": ("Ejercicio 8 - Transformar nombre", ejercicio_8),
        "9": ("Ejercicio 9 - Clasificar terremoto", ejercicio_9),
        "10": ("Ejercicio 10 - Estación por hemisferio/fecha", ejercicio_10),
        "0": ("Salir", None)
    }

    while True:
        print("\n--- Menú TP: Estructuras condicionales ---")
        for k, v in opciones.items():
            print(f"{k}) {v[0]}")
        choice = input("Elija una opción (0 para salir): ").strip()
        if choice == "0":
            print("Saliendo. ¡Hasta luego!")
            break
        action = opciones.get(choice)
        if action:
            print(f"\n>>> {action[0]}\n")
            try:
                action[1]()
            except Exception as e:
                print(f"Error al ejecutar la opción: {e}")
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
