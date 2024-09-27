import tkinter as tk
from tkinter import messagebox

# Función para agregar una nueva tarea
def agregar_tarea():
    tarea = entry.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entry.delete(0, tk.END)  # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "Ingrese una tarea.")

# Función para eliminar la tarea seleccionada
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        lista_tareas.delete(tarea_seleccionada)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Función para marcar la tarea como completada
def completar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(tarea_seleccionada)
        lista_tareas.delete(tarea_seleccionada)
        lista_tareas.insert(tk.END, f"{tarea} ✔")  # Marcar la tarea como completada
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para completar.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas - To-Do List")
ventana.geometry("400x400")

# Etiqueta
label = tk.Label(ventana, text="Ingrese una nueva tarea:")
label.pack(pady=10)

# Campo de texto
entry = tk.Entry(ventana, width=40)
entry.pack(pady=5)

# Botón para agregar tarea
btn_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=10)
lista_tareas.pack(pady=10)

# Botón para eliminar tarea
btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Botón para marcar tarea como completada
btn_completar = tk.Button(ventana, text="Completar Tarea", command=completar_tarea)
btn_completar.pack(pady=5)

# Iniciar el loop de la aplicación
ventana.mainloop()
