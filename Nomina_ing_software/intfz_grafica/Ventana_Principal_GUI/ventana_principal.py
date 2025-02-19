import tkinter as tk
from intfz_grafica.Estado_Vehiculo_GUI.Registrar_estado import EstadoVehiculo  
from intfz_grafica.Eliminar_Empleado_GUI.eliminar_empleado_gui import Eliminar_empleado_GUI
from intfz_grafica.Registrar_Empleado_GUI.registrar_empleado_gui import Registrar_empleado_GUI
from intfz_grafica.Registrar_Vehiculo_GUI.registrar_vehiculo_gui import RegistrarvehiculoGUI
from intfz_grafica.Formar_Grupo_GUI.Formar_grupo import Formar_Grupo_GUI
from tkinter import messagebox

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
            ("Registrar empleado", self.registrar_empleado), #Lista
            ("Formar grupo", self.formar_grupo),
            ("Eliminar empleado", self.eliminar_empleado), #Lista
            ("Registrar nuevo vehículo", self.registrar_vehiculo),
            ("Asignar ruta", self.asignar_ruta),
            ("Registrar estado del vehículo", self.abrir_estado_vehiculo),
            ("Cerrar", self.cerrar)
        ]

        for texto, comando in botones:
            btn = tk.Button(frame_central, text=texto, font=("Arial", 14), width=25, height=2, command=comando)
            btn.pack(pady=10)

        self.ventana.mainloop()

    def registrar_empleado(self):
        """Abre la ventana de Registrar empleado y oculta la principal temporalmente."""
        self.ventana.withdraw()  # Ocultar la ventana principal
        Registrar_empleado_GUI()  # Pasar la referencia de la ventana principal

    def formar_grupo(self):
        print("Función para formar grupo")
        self.ventana.withdraw()
        Formar_Grupo_GUI()

    def eliminar_empleado(self):
        """Abre la ventana de Eliminar empleado y oculta la principal temporalmente."""
        self.ventana.withdraw()  # Ocultar la ventana principal
        Eliminar_empleado_GUI()  # Pasar la referencia de la ventana principal

    def registrar_vehiculo(self):
        """Abre la ventana de Registrar vehículo y oculta la principal temporalmente."""   
        self.ventana.withdraw()
        RegistrarvehiculoGUI()

    def asignar_ruta(self):
        print("Función para asignar ruta")

    def abrir_estado_vehiculo(self):
        """Abre la ventana de EstadoVehiculo y oculta la principal temporalmente."""
        self.ventana.withdraw()  # Ocultar la ventana principal
        EstadoVehiculo()  # Pasar la referencia de la ventana principal

    def cerrar(self):
        respuesta = messagebox.askyesno(
            "Confirmar cierre",
            "Si cierra el programa, los grupos creados se disolverán ya que al volver a iniciar se interpretará como un día nuevo.\n¿Desea continuar?"
        )
        if respuesta:  # Si el usuario selecciona 'Sí'
            self.ventana.destroy()


# Ejecutar la aplicación
Ventana_principal()
