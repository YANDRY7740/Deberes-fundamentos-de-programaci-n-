import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")
        self.root.geometry("400x400")

        # Lista de tareas
        self.tasks = []

        # Crear el campo de entrada para las tareas
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Atajo: Enter para añadir tarea

        # Crear la lista de tareas (Listbox)
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.pack(pady=10)

        # Crear los botones para añadir, marcar como completado y eliminar tareas
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Marcar Completada", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Enlace de atajos de teclado
        self.root.bind("<C>", lambda event: self.complete_task())
        self.root.bind("<D>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = not self.tasks[selected_task_index]["completed"]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["task"]
            if task["completed"]:
                task_text += " ✔"  # Marcar como completada
            self.task_listbox.insert(tk.END, task_text)

# Crear la ventana principal
root = tk.Tk()
app = TodoApp(root)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
