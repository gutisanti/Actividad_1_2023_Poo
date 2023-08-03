#punto 1
def main():
    
    nombre = input("Por favor, introduce tu nombre: ")

    
    edad = input("Por favor, introduce tu edad: ")

    
    print("Hola, " + nombre + "! Tienes " + edad + " años.")

if __name__ == "__main__":
    main()

#punto 2
import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

radio = 5
area = calcular_area_circulo(radio)
print("El área del círculo es:", area)


#punto 3
import random

def generar_lista_numeros_aleatorios(n):
    lista_aleatoria = [random.randint(1, 100) for _ in range(n)]
    return lista_aleatoria

cantidad_numeros = int(input("Ingresa la cantidad de números aleatorios que deseas generar: "))
numeros_aleatorios = generar_lista_numeros_aleatorios(cantidad_numeros)
print("Lista de números aleatorios:", numeros_aleatorios)


#punto 4
def es_par(numero):
    return numero % 2 == 0

numero = int(input("Ingresa un número entero: "))
if es_par(numero):
    print(numero, "es un número par.")
else:
    print(numero, "es un número impar.")


#punto 5
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)
print("La temperatura en grados Celsius es:", celsius)


#punto 6
def calcular_suma_lista(lista):
    suma = sum(lista)
    return suma

lista_numeros = [1, 2, 3, 4, 5]
suma = calcular_suma_lista(lista_numeros)
print("La suma de los números en la lista es:", suma)

#punto 7
def encontrar_extremos_lista(lista):
    minimo = min(lista)
    maximo = max(lista)
    return minimo, maximo

lista_numeros = [10, 4, 67, 23, 1, 58, 34]
minimo, maximo = encontrar_extremos_lista(lista_numeros)
print("El número más pequeño en la lista es:", minimo)
print("El número más grande en la lista es:", maximo)

#punto 8
def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

lista_numeros = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(lista_numeros)
print("Lista invertida:", lista_invertida)

#punto 9
import random

def generar_matriz(filas, columnas):
    matriz = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]
    return matriz

filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))
matriz_numeros = generar_matriz(filas, columnas)

print("Matriz generada:")
for fila in matriz_numeros:
    print(fila)

#punto 10
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

numero = int(input("Ingresa un número entero para calcular su factorial: "))
factorial = calcular_factorial(numero)
print("El factorial de", numero, "es:", factorial)

#punto 11
lista_pares = [num for num in range(1, 101) if num % 2 == 0]
print("Lista de números pares entre 1 y 100:", lista_pares)

#punto 12
for numero in range(1, 11):
    print(numero)

#punto 13
def calcular_operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    return suma, resta, multiplicacion, division

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division = calcular_operaciones(numero1, numero2)

print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)

#punto 14
def calcular_media(lista):
    if not lista:
        return None
    suma = sum(lista)
    media = suma / len(lista)
    return media

lista_numeros = [10, 20, 30, 40, 50]
media = calcular_media(lista_numeros)
print("La media aritmética de la lista es:", media)

#punto 15
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

texto = input("Ingresa una cadena de texto: ")
if es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

    