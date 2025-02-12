import tkinter as tk
from intfz_grafica.Estado_Vehiculo_GUI.Registrar_estado import EstadoVehiculo  # Importar la clase sin ejecutarla
from intfz_grafica.Eliminar_Empleado_GUI.eliminar_empleado_gui import Eliminar_empleado_GUI

class Ventana_principal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana Principal")

        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

        frame_central = tk.Frame(self.ventana)
        frame_central.pack(expand=True)

        botones = [
            ("Registrar empleado", self.registrar_empleado),
            ("Formar grupo", self.formar_grupo),
            ("Eliminar empleado", self.eliminar_empleado),
            ("Registrar nuevo vehículo", self.registrar_vehiculo),
            ("Asignar ruta", self.asignar_ruta),
            ("Registrar estado del vehículo", self.abrir_estado_vehiculo)  # Redirige a EstadoVehiculo
        ]

        for texto, comando in botones:
            btn = tk.Button(frame_central, text=texto, font=("Arial", 14), width=25, height=2, command=comando)
            btn.pack(pady=10)

        self.ventana.mainloop()

    def registrar_empleado(self):
        print("Función para registrar empleado")

    def formar_grupo(self):
        print("Función para formar grupo")

    def eliminar_empleado(self):
        """Abre la ventana de Eliminar empleado y oculta la principal temporalmente."""
        self.ventana.withdraw()  # Ocultar la ventana principal
        Eliminar_empleado_GUI()  # Pasar la referencia de la ventana principal

    def registrar_vehiculo(self):
        print("Función para registrar nuevo vehículo")

    def asignar_ruta(self):
        print("Función para asignar ruta")

    def abrir_estado_vehiculo(self):
        """Abre la ventana de EstadoVehiculo y oculta la principal temporalmente."""
        self.ventana.withdraw()  # Ocultar la ventana principal
        EstadoVehiculo()  # Pasar la referencia de la ventana principal

# Ejecutar la aplicación
Ventana_principal()
