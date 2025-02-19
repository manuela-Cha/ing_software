import tkinter as tk
from tkinter import messagebox

class Registrar_empleado_GUI:
    def __init__(self):
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

        """tk.Label(self.ventana, text="Turno:").pack(pady=5)
        self.entry_turno = tk.Entry(self.ventana, width=30)
        self.entry_turno.pack(pady=5)

        tk.Label(self.ventana, text="Ruta asignada:").pack(pady=5)
        self.entry_ruta_asignada = tk.Entry(self.ventana, width=30)
        self.entry_ruta_asignada.pack(pady=5)"""

        # Botón para agregar empleado
        self.boton_agregar = tk.Button(
            self.ventana, text="Agregar Empleado",
            command=self.agregar_empleado
        )
        self.boton_agregar.pack(pady=20)

        #Botón para cerrar
        self.boton_cerrar = tk.Button(self.ventana, text="Cerrar", command=self.abrir_ventana_principal)
        self.boton_cerrar.pack(pady=10)

        # Iniciar el bucle de la interfaz gráfica
        self.ventana.mainloop()

    def agregar_empleado(self):
        # Obtener datos ingresados
        nombre = self.entry_nombre.get().strip().lower()
        apellido = self.entry_apellido.get().strip().lower()
        cedula = self.entry_cedula.get().strip()

        # Verificar que no haya campos vacíos
        if not nombre or not apellido or not cedula:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Verificar si la cédula ya existe en el archivo
        with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(" ")
                if len(datos) == 3:
                    cedula_archivo = datos[2]
                    if cedula == cedula_archivo:
                        messagebox.showerror("Error", "El empleado ya existe.")
                        return

        # Si no existe, agregar el empleado al archivo
        with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'a') as archivo:
            archivo.write(f"{nombre} {apellido} {cedula} Disponible\n")
        
        messagebox.showinfo("Éxito", "Empleado agregado correctamente.")
        
        # Limpiar los campos de entrada
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_cedula.delete(0, tk.END)
        """self.entry_turno.delete(0, tk.END)
        self.entry_ruta_asignada.delete(0, tk.END)"""

    def abrir_ventana_principal(self):
        """Abre la ventana principal y oculta la de vehiculo temporalmente."""
        self.ventana.withdraw()  # Ocultar la ventana principal
        from intfz_grafica.Ventana_Principal_GUI.ventana_principal import Ventana_principal
        Ventana_principal()


