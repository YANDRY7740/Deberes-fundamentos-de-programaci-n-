import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = {}
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Creando un nuevo archivo...")
            open(self.archivo, 'w').close()
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(str(producto) + '\n')
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: El producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()
            print(f"Producto {producto.nombre} añadido exitosamente.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nombre:
                producto.nombre = nombre
            if cantidad:
                producto.cantidad = cantidad
            if precio:
                producto.precio = precio
            self.guardar_inventario()
            print(f"Producto {producto.nombre} actualizado exitosamente.")
        else:
            print("Error: El producto no existe en el inventario.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado exitosamente.")
        else:
            print("Error: El producto no existe en el inventario.")

#EJEMPLO DE USO
# Crear el inventario
inventario = Inventario()

# Agregar un producto
inventario.agregar_producto(Producto('001', 'Manzanas', 50, 0.5))

# Actualizar un producto
inventario.actualizar_producto('001', cantidad=75)

# Eliminar un producto
inventario.eliminar_producto('001')
