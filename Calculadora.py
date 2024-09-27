import tkinter as tk

# Función para agregar números y operadores a la entrada
def agregar_valor(valor):
    entrada_actual = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, entrada_actual + str(valor))

# Función para calcular el resultado de la operación
def calcular():
    try:
        resultado = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultado))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Función para limpiar la entrada
def limpiar():
    entry.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("300x400")

# Campo de texto para mostrar la operación y el resultado
entry = tk.Entry(ventana, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definir los botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Crear los botones y colocarlos en la cuadrícula
for (texto, fila, columna) in botones:
    if texto == '=':
        btn = tk.Button(ventana, text=texto, width=10, height=3, command=calcular)
    else:
        btn = tk.Button(ventana, text=texto, width=10, height=3, command=lambda t=texto: agregar_valor(t))
    btn.grid(row=fila, column=columna, padx=5, pady=5)

# Botón para limpiar la entrada
btn_limpiar = tk.Button(ventana, text='C', width=10, height=3, command=limpiar)
btn_limpiar.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Iniciar el loop de la aplicación
ventana.mainloop()
