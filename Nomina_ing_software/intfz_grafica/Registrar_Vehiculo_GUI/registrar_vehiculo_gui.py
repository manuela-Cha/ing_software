import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

class RegistrarvehiculoGUI:
    def __init__(self):
        # Creación de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Agregar Vehículo")
        self.ventana.geometry("500x500")

        # Definir colores
        self.color_primary = "#2ECC71"      # Verde principal
        self.color_secondary = "#27AE60"    # Verde secundario
        self.color_accent = "#1E8449"       # Verde oscuro para acentos
        self.color_bg = "#F5F5F5"           # Fondo gris muy claro
        self.color_text = "#2C3E50"         # Texto oscuro
        self.color_white = "#FFFFFF"        # Blanco puro

        # Crear fuentes personalizadas
        self.font_title = font.Font(family="Helvetica", size=16, weight="bold")
        self.font_subtitle = font.Font(family="Helvetica", size=12, weight="bold")
        self.font_button = font.Font(family="Helvetica", size=10, weight="bold")
        self.font_normal = font.Font(family="Helvetica", size=10)

        # Configurar el color de fondo de la ventana principal
        self.ventana.configure(bg=self.color_bg)

        # Etiquetas y campos de entrada
        label_id = tk.Label(self.ventana, 
                          text="ID del Vehículo:", 
                          bg=self.color_bg,
                          fg=self.color_text,
                          font=self.font_subtitle)
        label_id.pack(pady=5)
        
        self.entry_id_vehiculo = tk.Entry(self.ventana, 
                                        width=30,
                                        bg=self.color_white,
                                        fg=self.color_text,
                                        font=self.font_normal,
                                        insertbackground=self.color_text)
        self.entry_id_vehiculo.pack(pady=5)

        # Botón para agregar vehículo
        self.boton_agregar = tk.Button(self.ventana, 
                                     text="Agregar Vehículo",
                                     command=self.agregar_vehiculo,
                                     bg=self.color_primary,
                                     fg=self.color_white,
                                     font=self.font_button,
                                     activebackground=self.color_secondary,
                                     activeforeground=self.color_white,
                                     relief="flat",
                                     padx=10,
                                     pady=5)
        self.boton_agregar.pack(pady=20)

        # Botón para cerrar
        self.boton_cerrar = tk.Button(self.ventana, 
                                    text="Cerrar", 
                                    command=self.abrir_ventana_principal,
                                    bg=self.color_accent,
                                    fg=self.color_white,
                                    font=self.font_button,
                                    activebackground=self.color_secondary,
                                    activeforeground=self.color_white,
                                    relief="flat",
                                    padx=10,
                                    pady=5)
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
        try:
            with open('Nomina_ing_software/archivos_de_texto/Vehiculos.txt', 'r') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    datos = linea.strip().split(" ")
                    if len(datos) >= 1:  # Changed to >= 1 to handle lines with status
                        id_archivo = datos[0]
                        if id_vehiculo == id_archivo:
                            messagebox.showerror("Error", "El vehículo ya existe.")
                            return
        except FileNotFoundError:
            # If file doesn't exist, we'll create it when writing
            pass

        # Si no existe, agregar el vehículo al archivo
        with open('Nomina_ing_software/archivos_de_texto/Vehiculos.txt', 'a') as archivo:
            archivo.write(f"{id_vehiculo} Disponible\n")
        
        messagebox.showinfo("Éxito", "Vehículo agregado correctamente.")
        
        # Limpiar el campo de entrada
        self.entry_id_vehiculo.delete(0, tk.END)

    def abrir_ventana_principal(self):
        """Abre la ventana principal y oculta la de vehículo temporalmente."""
        self.ventana.withdraw()  # Ocultar la ventana principal
        from intfz_grafica.Ventana_Principal_GUI.ventana_principal import Ventana_principal
        Ventana_principal()

if __name__ == "__main__":
    RegistrarvehiculoGUI()
    