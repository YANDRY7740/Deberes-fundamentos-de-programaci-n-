class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Métodos para obtener los atributos
    def get_id(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Métodos para establecer los atributos
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id_producto}, Nombre: {self.__nombre}, Cantidad: {self.__cantidad}, Precio: ${self.__precio:.2f}"


import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: Ya existe un producto con este ID.")
        else:
            self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [prod for prod in self.productos.values() if prod.get_nombre().lower() == nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("No hay productos en el inventario.")

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            productos_serializados = {id_producto: vars(prod) for id_producto, prod in self.productos.items()}
            json.dump(productos_serializados, f)
        print("Inventario guardado en archivo.")

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                productos_serializados = json.load(f)
                for id_producto, datos in productos_serializados.items():
                    producto = Producto(**datos)
                    self.productos[id_producto] = producto
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo.")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Cargar inventario desde archivo")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (presiona Enter para mantener la actual): ")
            precio = input("Nuevo precio (presiona Enter para mantener el actual): ")
            inventario.actualizar_producto(id_producto,
                                           cantidad=int(cantidad) if cantidad else None,
                                           precio=float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            archivo = input("Nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(archivo)

        elif opcion == '7':
            archivo = input("Nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(archivo)

        elif opcion == '8':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 8.")


if __name__ == "__main__":
    menu()
