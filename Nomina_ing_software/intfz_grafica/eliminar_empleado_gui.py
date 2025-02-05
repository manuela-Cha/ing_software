"""import tkinter as tk
from tkinter import messagebox
from BD.Eliminar_empleado import Eliminar_empleado
from BD.conexion import Conectar 

class Eliminar_empleado_GUI:
    def __init__(self):
        # Creación de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Eliminar Empleado")
        self.ventana.geometry("500x500")

        # Etiquetas y campos de entrada
        tk.Label(self.ventana, text="Nombre:").pack(pady=5)
        self.entry_nombre = tk.Entry(self.ventana, width=30)
        self.entry_nombre.pack(pady=5)

        tk.Label(self.ventana, text="Apellido:").pack(pady=5)
        self.entry_apellido = tk.Entry(self.ventana, width=30)
        self.entry_apellido.pack(pady=5)

        tk.Label(self.ventana, text="Cedula:").pack(pady=5)
        self.entry_cedula = tk.Entry(self.ventana, width=30)
        self.entry_cedula.pack(pady=5)

        # Botón para eliminar empleado
        self.boton_eliminar = tk.Button(
            self.ventana, text="Eliminar Empleado",
            command=self.eliminar_empleado
        )
        self.boton_eliminar.pack(pady=20)

        # Iniciar el bucle de la interfaz gráfica
        self.ventana.mainloop()

    # Función para manejar el evento del botón
    def eliminar_empleado(self):
        nombre = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        cedula = self.entry_cedula.get().strip()

        # Validar que los campos no estén vacíos
        if not nombre or not apellido or not cedula:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Verificar si el empleado existe antes de eliminar
        if self.verificar_existencia(nombre, apellido, cedula):
            try:
                Eliminar_empleado.eliminar_empleado(nombre, apellido, cedula)
                messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Hubo un error al eliminar el empleado: {e}")
        else:
            messagebox.showerror("Error", "El empleado no existe en la base de datos.")"""