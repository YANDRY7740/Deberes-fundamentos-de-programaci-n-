#IMPLEMENTACION:
from datetime import datetime, timedelta


# Clase Cliente
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"


# Clase Habitación
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def __str__(self):
        return f"Habitación {self.numero}: {self.tipo}, Precio: ${self.precio}, Disponible: {self.disponible}"


# Clase Reserva
class Reserva:
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} en Habitación {self.habitacion.numero} del {self.fecha_inicio} al {self.fecha_fin}"


# Clase Hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        for habitacion in self.habitaciones:
            print(habitacion)

    def verificar_disponibilidad(self, numero_habitacion, fecha_inicio, fecha_fin):
        for reserva in self.reservas:
            if reserva.habitacion.numero == numero_habitacion:
                if (fecha_inicio < reserva.fecha_fin and fecha_fin > reserva.fecha_inicio):
                    return False
        return True

    def realizar_reserva(self, cliente, numero_habitacion, fecha_inicio, fecha_fin):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                if self.verificar_disponibilidad(numero_habitacion, fecha_inicio, fecha_fin):
                    nueva_reserva = Reserva(cliente, habitacion, fecha_inicio, fecha_fin)
                    self.reservas.append(nueva_reserva)
                    habitacion.disponible = False
                    print(f"Reserva realizada: {nueva_reserva}")
                    return
                else:
                    print(f"La habitación {numero_habitacion} no está disponible en las fechas solicitadas.")
                    return
        print(f"No se encontró la habitación {numero_habitacion}.")


# Ejemplo de uso del sistema de reservas
# Crear hotel
hotel = Hotel("Hotel Python")

# Crear habitaciones
habitacion1 = Habitacion(101, "Simple", 50)
habitacion2 = Habitacion(102, "Doble", 80)

# Agregar habitaciones al hotel
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

# Mostrar habitaciones del hotel
print("Habitaciones disponibles en el hotel:")
hotel.mostrar_habitaciones()

# Crear cliente
cliente1 = Cliente("Juan Perez", "juan.perez@example.com")

# Realizar reserva
fecha_inicio = datetime(2024, 6, 21)
fecha_fin = datetime(2024, 6, 25)
hotel.realizar_reserva(cliente1, 101, fecha_inicio, fecha_fin)

# Intentar realizar una reserva en una habitación ocupada
hotel.realizar_reserva(cliente1, 101, fecha_inicio, fecha_fin)

# Mostrar habitaciones del hotel después de realizar una reserva
print("\nHabitaciones disponibles en el hotel después de la reserva:")
hotel.mostrar_habitaciones()

