import tkinter as tk
from tkinter import messagebox

class Formulario(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        # Campo Nombre
        self.nombre_label = tk.Label(self, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack()

        # Campo Edad
        self.edad_label = tk.Label(self, text="Edad:")
        self.edad_label.pack()
        self.edad_entry = tk.Entry(self)
        self.edad_entry.pack()

        # Campo Curso
        self.curso_label = tk.Label(self, text="Curso:")
        self.curso_label.pack()
        self.curso_entry = tk.Entry(self)
        self.curso_entry.pack()

        # Campo Nombre de usuario en juegos
        self.juego_label = tk.Label(self, text="Nombre de usuario en juegos:")
        self.juego_label.pack()
        self.juego_entry = tk.Entry(self)
        self.juego_entry.pack()

        # Campo Asignaturas favoritas
        self.asignaturas_label = tk.Label(self, text="Asignaturas favoritas (separadas por comas):")
        self.asignaturas_label.pack()
        self.asignaturas_entry = tk.Entry(self)
        self.asignaturas_entry.pack()

        # Botón para enviar formulario
        self.enviar_button = tk.Button(self, text="Enviar", command=self.enviar_formulario)
        self.enviar_button.pack()

    def enviar_formulario(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        curso = self.curso_entry.get()
        juego_usuario = self.juego_entry.get()
        asignaturas = self.asignaturas_entry.get().split(',')

        # Mostramos un mensaje con la información recolectada
        mensaje = f"Nombre: {nombre}\nEdad: {edad}\nCurso: {curso}\nNombre de usuario en juegos: {juego_usuario}\nAsignaturas favoritas: {', '.join(asignaturas)}"
        messagebox.showinfo("Información del formulario", mensaje)

# Creamos la ventana principal y el formulario
root = tk.Tk()
formulario = Formulario(master=root)

# Ejecutamos la ventana principal
formulario.mainloop()
