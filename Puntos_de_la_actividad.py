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



    