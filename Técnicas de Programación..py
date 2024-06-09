#Ejemplos para cada una de las técnicas de programación:
#Abstracción
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Uso de la abstracción
def animal_sound(animal: Animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()
animal_sound(dog)  # Salida: Woof!
animal_sound(cat)  # Salida: Meow!


#Encapsulación
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Atributo privado

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

# Uso de la encapsulación
account = BankAccount("Alice", 1000)
print(account.get_balance())  # Salida: 1000
account.deposit(500)
print(account.get_balance())  # Salida: 1500
account.withdraw(200)
print(account.get_balance())  # Salida: 1300

#Herencia
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar_motor(self):
        return "Motor arrancado"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def abrir_puertas(self):
        return f"{self.puertas} puertas abiertas"

# Uso de la herencia
coche = Coche("Toyota", "Corolla", 4)
print(coche.arrancar_motor())  # Salida: Motor arrancado
print(coche.abrir_puertas())   # Salida: 4 puertas abiertas

#Polimorfismo
class Pajaro:
    def hacer_sonido(self):
        return "Pío"

class Perro:
    def hacer_sonido(self):
        return "¡Guau!"

class Gato:
    def hacer_sonido(self):
        return "¡Miau!"

# Uso del polimorfismo
def sonido_animal(animal):
    print(animal.hacer_sonido())

pajaro = Pajaro()
perro = Perro()
gato = Gato()

sonido_animal(pajaro)  # Salida: Pío
sonido_animal(perro)   # Salida: ¡Guau!
sonido_animal(gato)    # Salida: ¡Miau!

