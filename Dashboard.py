import os


def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo de script.

    Parámetros:
    ruta_script (str): La ruta al archivo de script.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def agregar_script(opciones):
    """
    Permite al usuario agregar un nuevo script al menú.

    Parámetros:
    opciones (dict): Diccionario con las opciones del menú.
    """
    nombre_script = input("Introduce el nombre descriptivo del script: ")
    ruta_script = input("Introduce la ruta relativa al script: ")
    clave = str(len(opciones) + 1)
    opciones[clave] = ruta_script
    print(f"Script '{nombre_script}' agregado con éxito!")


def mostrar_menu():
    """
    Muestra el menú principal y permite al usuario elegir entre ver un script, agregar un nuevo script o salir.
    """
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")
        print("A - Agregar nuevo script")

        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            break
        elif eleccion.upper() == 'A':
            agregar_script(opciones)
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
