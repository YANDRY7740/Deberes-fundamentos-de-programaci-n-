# Escritura de Archivo de Texto
with open("my_notes.txt", "w") as file:
    file.write("Nota 1: Hoy tengo que hacer la compra.\n")
    file.write("Nota 2: Recordar llamar a Juan para su cumpleaños.\n")
    file.write("Nota 3: Revisar el informe antes de la reunión de mañana.\n")

# Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() elimina los espacios en blanco al inicio y final de la línea

# Cierre de Archivos
# No es necesario cerrar explícitamente el archivo ya que se hace automáticamente cuando se usa 'with open()'
