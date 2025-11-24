
# TP 7 - Recursividad

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def mostrar_factoriales(hasta):
    for i in range(1, hasta+1):
        print(f"Factorial de {i}: {factorial(i)}")

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def mostrar_fibonacci(hasta):
    serie = []
    for i in range(hasta+1):
        serie.append(fibonacci(i))
    return serie

def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp-1)

def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n-1)

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)
