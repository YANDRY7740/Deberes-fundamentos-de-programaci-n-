# Crear el diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Yandry",
    "edad": 18,
    "ciudad": "Lago Agrio",
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Lago Agrio"

# Agregar la clave "profesion" al diccionario
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0981213156"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)
