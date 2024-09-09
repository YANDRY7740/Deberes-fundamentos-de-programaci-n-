# Clase Libro: Representa un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # La tupla almacena título y autor, ya que estos valores no cambiarán.
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

# Clase Usuario: Representa un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def listar_libros_prestados(self):
        return [str(libro) for libro in self.libros_prestados]

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

# Clase Biblioteca: Gestiona libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios únicos
        self.historial_prestamos = []

    # Funcionalidad para añadir un libro
    def añadir_libro(self, libro):
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' añadido a la biblioteca.")

    # Funcionalidad para eliminar un libro
    def eliminar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"Libro con ISBN {isbn} no encontrado en la biblioteca.")

    # Funcionalidad para registrar un usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios_registrados.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")

    # Funcionalidad para dar de baja un usuario
    def dar_de_baja_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            if len(usuario.libros_prestados) == 0:
                self.usuarios_registrados.remove(usuario.id_usuario)
                print(f"Usuario '{usuario.nombre}' dado de baja.")
            else:
                print(f"El usuario '{usuario.nombre}' tiene libros pendientes por devolver.")
        else:
            print(f"Usuario con ID {usuario.id_usuario} no encontrado.")

    # Funcionalidad para prestar un libro a un usuario
    def prestar_libro(self, isbn, usuario):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            usuario.prestar_libro(libro)
            self.historial_prestamos.append((usuario.id_usuario, isbn))
            print(f"Libro '{libro.info[0]}' prestado a '{usuario.nombre}'.")
        else:
            print(f"Libro con ISBN {isbn} no disponible o ya prestado.")

    # Funcionalidad para devolver un libro
    def devolver_libro(self, isbn, usuario):
        libro = usuario.devolver_libro(isbn)
        if libro:
            self.libros_disponibles[isbn] = libro
            print(f"Libro '{libro.info[0]}' devuelto por '{usuario.nombre}'.")
        else:
            print(f"Usuario '{usuario.nombre}' no tiene el libro con ISBN {isbn}.")

    # Buscar libros por título, autor o categoría
    def buscar_libros(self, termino_busqueda):
        resultados = []
        for libro in self.libros_disponibles.values():
            if (termino_busqueda.lower() in libro.info[0].lower() or  # Búsqueda por título
                termino_busqueda.lower() in libro.info[1].lower() or  # Búsqueda por autor
                termino_busqueda.lower() in libro.categoria.lower()):  # Búsqueda por categoría
                resultados.append(str(libro))
        return resultados if resultados else "No se encontraron libros."

    # Mostrar libros prestados a un usuario
    def listar_libros_prestados_usuario(self, usuario):
        libros = usuario.listar_libros_prestados()
        return libros if libros else "No tiene libros prestados."

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("El Quijote", "Miguel de Cervantes", "Novela", "978-3-16-148410-0")
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Realismo Mágico", "978-0-14-310629-6")

    # Añadir libros a la biblioteca
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Juan Pérez", 1)
    usuario2 = Usuario("Ana García", 2)
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("978-3-16-148410-0", usuario1)

    # Listar libros prestados de un usuario
    print("Libros prestados por Juan:")
    print(biblioteca.listar_libros_prestados_usuario(usuario1))

    # Devolver un libro
    biblioteca.devolver_libro("978-3-16-148410-0", usuario1)

    # Buscar libros por categoría
    print("Búsqueda por 'Realismo Mágico':")
    print(biblioteca.buscar_libros("Realismo Mágico"))

    # Dar de baja a un usuario
    biblioteca.dar_de_baja_usuario(usuario1)
