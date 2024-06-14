# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal para ejecutar el programa
def main():
    print("Programa para calcular el promedio semanal de la temperatura")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()

# Programación Orientada a Objetos (POO)

class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    print("Programa para calcular el promedio semanal de la temperatura usando POO")
    clima_semanal = ClimaDiario()
    clima_semanal.ingresar_temperaturas()
    promedio = clima_semanal.calcular_promedio()
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}")

if __name__ == "__main__":
    main()
