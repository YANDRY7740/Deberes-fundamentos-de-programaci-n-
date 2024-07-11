class ConexionBaseDeDatos:
    def __init__(self, nombre_bd):
        """
        Constructor de la clase ConexionBaseDeDatos.
        Inicializa el nombre de la base de datos.
        Simula la apertura de una conexión a la base de datos.
        """
        self.nombre_bd = nombre_bd
        self.conectado = False
        self.abrir_conexion()

    def abrir_conexion(self):
        """
        Método que simula la apertura de una conexión a la base de datos.
        """
        self.conectado = True
        print(f"Conexión a la base de datos '{self.nombre_bd}' establecida.")

    def cerrar_conexion(self):
        """
        Método que simula el cierre de la conexión a la base de datos.
        """
        if self.conectado:
            self.conectado = False
            print(f"Conexión a la base de datos '{self.nombre_bd}' cerrada.")

    def __del__(self):
        """
        Destructor de la clase ConexionBaseDeDatos.
        Asegura que la conexión se cierre al destruir el objeto.
        """
        self.cerrar_conexion()


# Ejemplo de uso de la clase ConexionBaseDeDatos
if __name__ == "__main__":
    # Crear una instancia de ConexionBaseDeDatos
    conexion_bd = ConexionBaseDeDatos("mi_base_de_datos")

    # Realizar algunas operaciones simuladas
    print("Realizando operaciones en la base de datos...")

    # Forzar la eliminación del objeto para invocar el destructor
    del conexion_bd

