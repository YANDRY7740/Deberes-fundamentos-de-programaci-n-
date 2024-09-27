import tkinter as tk
from tkinter import messagebox

# Función para convertir de kilómetros a metros
def convertir_km_a_m():
    try:
        km = float(entry.get())
        metros = km * 1000  # 1 km = 1000 metros
        label_resultado.config(text=f"{km} km son {metros:.2f} metros")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Kilómetros a Metros")
ventana.geometry("350x200")

# Etiqueta de instrucción
label = tk.Label(ventana, text="Ingrese los kilómetros a convertir:")
label.pack(pady=10)

# Campo de texto para ingresar los kilómetros
entry = tk.Entry(ventana, width=30)
entry.pack(pady=5)

# Botón para convertir de km a metros
btn_convertir = tk.Button(ventana, text="Convertir Km a Metros", command=convertir_km_a_m)
btn_convertir.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

# Iniciar el loop de la aplicación
ventana.mainloop()
