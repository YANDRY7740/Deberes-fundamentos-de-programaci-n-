import math


def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    area = math.pi * radio ** 2
    return area


def convertir_celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de Celsius a Fahrenheit."""
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("Seleccione una opción:")
    print("1. Calcular el área de un círculo")
    print("2. Convertir temperatura de Celsius a Fahrenheit")
    print("3. Salir")


def main():
    """Función principal del programa."""
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo con radio {radio} es {area:.2f}")

        elif opcion == 2:
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            fahrenheit = convertir_celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit")

        elif opcion == 3:
            continuar = False
            print("Gracias por usar el programa. ¡Adiós!")

        else:
            print("Opción no válida, por favor intente nuevamente.")


if __name__ == "__main__":
    main()
