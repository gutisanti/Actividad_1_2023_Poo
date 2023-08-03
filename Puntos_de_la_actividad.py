#punto 1
def main():
    # Solicitar el nombre al usuario
    nombre = input("Por favor, introduce tu nombre: ")

    # Solicitar la edad al usuario
    edad = input("Por favor, introduce tu edad: ")

    # Mostrar el nombre y la edad en pantalla
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

    