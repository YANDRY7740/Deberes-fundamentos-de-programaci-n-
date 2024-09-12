import tkinter as tk
from tkinter import messagebox

# Función para agregar números a la lista
def agregar_numero():
    try:
        numero = float(entry.get())
        lista.insert(tk.END, numero)
        entry.delete(0, tk.END)  # Limpiar campo de texto
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Función para calcular el promedio
def calcular_promedio():
    try:
        numeros = list(map(float, lista.get(0, tk.END)))
        if numeros:
            promedio = sum(numeros) / len(numeros)
            messagebox.showinfo("Promedio", f"El promedio es: {promedio:.2f}")
        else:
            messagebox.showwarning("Advertencia", "La lista está vacía.")
    except ValueError:
        messagebox.showerror("Error", "No se puede calcular el promedio.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI - Cálculo de Promedio")
ventana.geometry("400x350")

# Etiqueta y campo de texto
label = tk.Label(ventana, text="Ingrese un número:")
label.pack(pady=10)
entry = tk.Entry(ventana, width=30)
entry.pack(pady=5)

# Botón para agregar número
btn_agregar = tk.Button(ventana, text="Agregar Número", command=agregar_numero)
btn_agregar.pack(pady=5)

# Lista para mostrar los números agregados
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Botón para calcular el promedio
btn_promedio = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio)
btn_promedio.pack(pady=5)

# Botón para limpiar la lista
btn_limpiar = tk.Button(ventana, text="Limpiar Lista", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Iniciar el loop de la aplicación
ventana.mainloop()
