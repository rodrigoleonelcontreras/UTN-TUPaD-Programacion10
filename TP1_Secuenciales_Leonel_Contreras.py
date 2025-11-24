
# TP 1 - Estructuras Secuenciales
# Alumno: Leonel Contreras
# Fecha: 24/11/2025

# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
import math
radio = float(input("Radio: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"Área: {area}, Perímetro: {perimetro}")

# Ejercicio 5
seg = int(input("Segundos: "))
horas = seg / 3600
print(f"Equivale a {horas} horas")

# Ejercicio 6
num = int(input("Número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# Ejercicio 7
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)

# Ejercicio 8
peso = float(input("Peso en kg: "))
altura = float(input("Altura en m: "))
imc = peso / (altura**2)
print(f"IMC = {imc}")

# Ejercicio 9
c = float(input("Temperatura en Celsius: "))
f = (9/5) * c + 32
print(f"{f} Fahrenheit")

# Ejercicio 10
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
prom = (n1 + n2 + n3) / 3
print(f"Promedio = {prom}")
