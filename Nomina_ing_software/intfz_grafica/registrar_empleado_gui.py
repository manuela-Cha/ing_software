import tkinter as tk
from tkinter import messagebox
import subprocess
import os
from Nomina_ing_software.funcionalidades.Agregar_empleado import Agregar_empleado

class Registrar_empleado_GUI:
    def __init__(self):
        # Iniciar la API Flask
        self.iniciar_api()

        # Creación de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Agregar Empleado")
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

        tk.Label(self.ventana, text="Turno:").pack(pady=5)
        self.entry_turno = tk.Entry(self.ventana, width=30)
        self.entry_turno.pack(pady=5)

        tk.Label(self.ventana, text="Ruta asignada:").pack(pady=5)
        self.entry_ruta_asignada = tk.Entry(self.ventana, width=30)
        self.entry_ruta_asignada.pack(pady=5)

        # Botón para agregar empleado
        self.boton_agregar = tk.Button(
            self.ventana, text="Agregar Empleado",
            command=self.registrar_empleado
        )
        self.boton_agregar.pack(pady=20)

        # Iniciar el bucle de la interfaz gráfica
        self.ventana.mainloop()

    def iniciar_api(self):
        """Inicia la API Flask."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        api_path = os.path.join(script_dir, "..", "api", "app.py")

        if not os.path.isfile(api_path):
            messagebox.showerror("Error", f"No se encontró la API en: {api_path}")
            return

        try:
            subprocess.Popen(["python", api_path])
            print("Iniciando API Flask...")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar la API Flask: {e}")

    def registrar_empleado(self):
        try:
            Agregar_empleado.registrar_empleado(
                self.entry_nombre.get().strip(),
                self.entry_apellido.get().strip(),
                self.entry_cedula.get().strip(),
                self.entry_turno.get().strip(),
                self.entry_ruta_asignada.get().strip()
            )
            messagebox.showinfo("Éxito", "Empleado agregado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar empleado: {e}")

if __name__ == "__main__":
    Registrar_empleado_GUI()