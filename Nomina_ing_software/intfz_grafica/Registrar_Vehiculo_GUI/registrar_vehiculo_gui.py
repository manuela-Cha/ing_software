import tkinter as tk
from tkinter import messagebox

class RegistrarvehiculoGUI:
    def __init__(self):
        # Creación de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Agregar Vehículo")
        self.ventana.geometry("500x500")

        # Etiquetas y campos de entrada
        tk.Label(self.ventana, text="ID del Vehículo:").pack(pady=5)
        self.entry_id_vehiculo = tk.Entry(self.ventana, width=30)
        self.entry_id_vehiculo.pack(pady=5)

        # Botón para agregar vehículo
        self.boton_agregar = tk.Button(
            self.ventana, text="Agregar Vehículo",
            command=self.agregar_vehiculo
        )
        self.boton_agregar.pack(pady=20)

        # Botón para cerrar
        self.boton_cerrar = tk.Button(self.ventana, text="Cerrar", command=self.abrir_ventana_principal)
        self.boton_cerrar.pack(pady=10)

        # Iniciar el bucle de la interfaz gráfica
        self.ventana.mainloop()

    def agregar_vehiculo(self):
        # Obtener el ID del vehículo ingresado
        id_vehiculo = self.entry_id_vehiculo.get().strip()

        # Verificar que no haya campos vacíos
        if not id_vehiculo:
            messagebox.showerror("Error", "El ID del vehículo es obligatorio.")
            return

        # Verificar si el vehículo ya existe en el archivo
        with open('Nomina_ing_software/archivos_de_texto/Vehiculos.txt', 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(" ")
                if len(datos) == 1:  # Si la línea contiene solo un ID (del vehículo)
                    id_archivo = datos[0]
                    if id_vehiculo == id_archivo:
                        messagebox.showerror("Error", "El vehículo ya existe.")
                        return

        # Si no existe, agregar el vehículo al archivo
        with open('Nomina_ing_software/archivos_de_texto/Vehiculos.txt', 'a') as archivo:
            archivo.write(f"{id_vehiculo} Disponible \n")
        
        messagebox.showinfo("Éxito", "Vehículo agregado correctamente.")
        
        # Limpiar el campo de entrada
        self.entry_id_vehiculo.delete(0, tk.END)

    def abrir_ventana_principal(self):
        """Abre la ventana principal y oculta la de vehículo temporalmente."""
        self.ventana.withdraw()  # Ocultar la ventana principal
        from intfz_grafica.Ventana_Principal_GUI.ventana_principal import Ventana_principal
        Ventana_principal()
