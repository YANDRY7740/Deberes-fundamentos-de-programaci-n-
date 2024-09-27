#Clase base: Animal
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido
        self._edad = edad  # Atributo protegido

    def hablar(self):
        raise NotImplementedError("Las subclases deben implementar este método")

    def informacion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"

#Clase derivada: Perro
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.__raza = raza  # Atributo privado

    def hablar(self):
        return "¡Guau!"

    def informacion(self):
        info_base = super().informacion()
        return f"{info_base}, Raza: {self.__raza}"


class Gato(Animal):
    def hablar(self):
        return "¡Miau!"

# Código principal
if __name__ == "__main__":
    animales = [
        Perro(nombre="Buddy", edad=3, raza="Golden Retriever"),
        Gato(nombre="Bigotes", edad=2)
    ]

    for animal in animales:
        print(animal.informacion())
        print(animal.hablar())



