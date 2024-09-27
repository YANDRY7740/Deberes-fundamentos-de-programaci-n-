import tkinter as tk
from tkinter import messagebox

# Clase para gestionar la aplicación de la lista de tareas
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=10)

        # Botones para añadir, marcar como completada y eliminar
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.mark_task_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista para mostrar tareas
        self.task_listbox = tk.Listbox(self.root, width=40, height=10)
        self.task_listbox.pack(pady=10)

        # Permitir añadir tarea al presionar "Enter"
        self.root.bind("<Return>", lambda event: self.add_task())

    # Método para añadir tarea
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

    # Método para marcar una tarea como completada
    def mark_task_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = f"[Completada] {task}"
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, f"[Completada] {task}")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    # Método para eliminar una tarea
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
