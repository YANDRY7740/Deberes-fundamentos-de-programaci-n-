import tkinter as tk
from tkinter import messagebox

# Función para convertir de km a millas
def convertir_km_a_millas():
    try:
        km = float(entry.get())
        millas = km * 0.621371
        label_resultado.config(text=f"{km} km son {millas:.2f} millas")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido.")

# Función para convertir de millas a km
def convertir_millas_a_km():
    try:
        millas = float(entry.get())
        km = millas / 0.621371
        label_resultado.config(text=f"{millas} millas son {km:.2f} km")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Unidades")
ventana.geometry("400x200")

# Etiqueta de instrucción
label = tk.Label(ventana, text="Ingrese el valor a convertir:")
label.pack(pady=10)

# Campo de texto para ingresar la cantidad
entry = tk.Entry(ventana, width=30)
entry.pack(pady=5)

# Botón para convertir de km a millas
btn_km_a_millas = tk.Button(ventana, text="Convertir Km a Millas", command=convertir_km_a_millas)
btn_km_a_millas.pack(pady=5)

# Botón para convertir de millas a km
btn_millas_a_km = tk.Button(ventana, text="Convertir Millas a Km", command=convertir_millas_a_km)
btn_millas_a_km.pack(pady=5)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

# Iniciar el loop de la aplicación
ventana.mainloop()
