import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

class EstadoVehiculo:
    def __init__(self):
        # Ruta del archivo donde se almacenan los vehículos
        self.ruta_vehiculos = "Nomina_ing_software/archivos_de_texto/Vehiculos.txt"

        # Creación de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Estado de Vehículo")
        self.ventana.geometry("600x550")
        self.ventana.resizable(False, False)

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

        # Main container
        self.main_container = tk.Frame(self.ventana, bg=self.color_bg)
        self.main_container.pack(expand=True, fill='both', padx=20, pady=20)

        # Etiqueta y campo para la placa
        label_placa = tk.Label(self.main_container, 
                              text="Placa:", 
                              bg=self.color_bg,
                              fg=self.color_text,
                              font=self.font_subtitle)
        label_placa.pack(pady=5)
        
        self.entry_placa = tk.Entry(self.main_container, 
                                  width=30,
                                  bg=self.color_white,
                                  fg=self.color_text,
                                  font=self.font_normal,
                                  insertbackground=self.color_text)
        self.entry_placa.pack(pady=5)

        self.estado_vehiculo = None

        # Etiqueta para seleccionar estado
        label_estado = tk.Label(self.main_container, 
                               text="Seleccione el estado del vehículo:", 
                               bg=self.color_bg,
                               fg=self.color_text,
                               font=self.font_subtitle)
        label_estado.pack(pady=5)

        # Frame para los botones de estado
        frame_botones = tk.Frame(self.main_container, bg=self.color_bg)
        frame_botones.pack(pady=5)

        self.boton_optimo = tk.Button(frame_botones, 
                                    text="Disponible", 
                                    width=12, 
                                    command=lambda: self.seleccionar_estado("Disponible"),
                                    bg=self.color_primary,
                                    fg=self.color_white,
                                    font=self.font_button,
                                    activebackground=self.color_secondary,
                                    activeforeground=self.color_white,
                                    relief="flat")
        self.boton_optimo.pack(side=tk.LEFT, padx=5)

        self.boton_no_optimo = tk.Button(frame_botones, 
                                       text="No-optimo", 
                                       width=12, 
                                       command=lambda: self.seleccionar_estado("No-optimo"),
                                       bg=self.color_primary,
                                       fg=self.color_white,
                                       font=self.font_button,
                                       activebackground=self.color_secondary,
                                       activeforeground=self.color_white,
                                       relief="flat")
        self.boton_no_optimo.pack(side=tk.LEFT, padx=5)

        # Botón para registrar
        self.boton_registrar = tk.Button(self.main_container, 
                                       text="Registrar estado del vehiculo", 
                                       command=self.registrar_vehiculo,
                                       bg=self.color_primary,
                                       fg=self.color_white,
                                       font=self.font_button,
                                       activebackground=self.color_secondary,
                                       activeforeground=self.color_white,
                                       relief="flat",
                                       padx=10,
                                       pady=5)
        self.boton_registrar.pack(pady=10)

        # Botón para cerrar
        self.boton_cerrar = tk.Button(self.main_container, 
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

        # Área para mostrar vehículos existentes
        label_vehiculos = tk.Label(self.main_container, 
                                 text="Vehículos registrados:", 
                                 bg=self.color_bg,
                                 fg=self.color_text,
                                 font=self.font_subtitle)
        label_vehiculos.pack(pady=5)
        
        self.lista_vehiculos = tk.Listbox(self.main_container, 
                                        width=50, 
                                        height=10,
                                        bg=self.color_white,
                                        fg=self.color_text,
                                        font=self.font_normal)
        self.lista_vehiculos.pack(pady=5)

        # Footer con copyright y botón de ayuda
        self.create_footer()

        self.cargar_vehiculos()  # Cargar vehículos al iniciar

        self.ventana.mainloop()

    def create_footer(self):
        """Crea el pie de página con copyright y botón de ayuda."""
        footer_frame = tk.Frame(self.main_container, bg=self.color_accent, height=30)
        footer_frame.pack(fill='x', pady=(15, 0))

        # Texto de copyright
        copyright_label = tk.Label(footer_frame,
                                  text="© 2025 Sistema de Gestión de Rutas - v1.0",
                                  bg=self.color_accent,
                                  fg=self.color_white,
                                  font=("Helvetica", 8))
        copyright_label.pack(side='left', padx=10, pady=5)

        # Botón de ayuda
        help_button = tk.Button(footer_frame,
                               text="?",
                               bg=self.color_accent,
                               fg=self.color_white,
                               bd=0,
                               font=("Helvetica", 10, "bold"),
                               activebackground=self.color_secondary,
                               command=self.mostrar_ayuda,
                               width=3,
                               height=1,
                               cursor="hand2")
        help_button.pack(side='right', padx=10, pady=5)

    def mostrar_ayuda(self):
        """Muestra una ventana de ayuda."""
        help_window = tk.Toplevel(self.ventana)
        help_window.title("Ayuda")
        help_window.geometry("400x300")
        help_window.configure(bg=self.color_white)
        help_window.transient(self.ventana)
        help_window.grab_set()

        # Contenido de ayuda
        content_frame = tk.Frame(help_window, bg=self.color_white)
        content_frame.pack(expand=True, fill='both', padx=10, pady=10)

        tk.Label(content_frame,
                text="Ayuda - Estado de Vehículo",
                font=self.font_subtitle,
                bg=self.color_white,
                fg=self.color_text).pack(pady=(0, 10))

        help_text = """Instrucciones:
- Placa: Ingrese la placa del vehículo (en mayúsculas).
- Estado: Seleccione 'Disponible' o 'No-optimo' con los botones.
- Registrar: Haga clic para actualizar el estado del vehículo.
- Cerrar: Regresa al Panel de Administración.
- Vehículos registrados: Lista de vehículos actuales.

Nota: La placa debe coincidir con un vehículo registrado."""
        
        tk.Label(content_frame,
                text=help_text,
                font=self.font_normal,
                bg=self.color_white,
                fg=self.color_text,
                justify="left",
                wraplength=380).pack(pady=10)

        # Botón de cerrar
        tk.Button(content_frame,
                 text="Cerrar",
                 font=self.font_normal,
                 bg=self.color_accent,
                 fg=self.color_white,
                 command=help_window.destroy,
                 activebackground=self.color_secondary,
                 relief="flat",
                 padx=10,
                 pady=5).pack(pady=(10, 0))

    def seleccionar_estado(self, estado):
        """Actualiza el estado del vehículo seleccionado."""
        self.estado_vehiculo = estado

        if estado == "Disponible":
            self.boton_optimo.config(bg=self.color_secondary, relief=tk.SUNKEN)
            self.boton_no_optimo.config(bg=self.color_primary, relief=tk.RAISED)
        else:
            self.boton_optimo.config(bg=self.color_primary, relief=tk.RAISED)
            self.boton_no_optimo.config(bg=self.color_secondary, relief=tk.SUNKEN)

    def cargar_vehiculos(self):
        """Carga los vehículos desde el archivo y los muestra en la lista."""
        self.lista_vehiculos.delete(0, tk.END)  # Limpiar lista antes de cargar

        try:
            with open(self.ruta_vehiculos, "r") as file:
                for linea in file:
                    self.lista_vehiculos.insert(tk.END, linea.strip())
        except FileNotFoundError:
            messagebox.showerror("Error", f"No se encontró el archivo {self.ruta_vehiculos}")

    def registrar_vehiculo(self):
        """Registra el nuevo estado del vehículo en el archivo."""
        placa = self.entry_placa.get().strip().upper()

        if not placa:
            messagebox.showwarning("Entrada inválida", "Debe ingresar la placa del vehículo.")
            return

        if not self.estado_vehiculo:
            messagebox.showwarning("Estado no seleccionado", "Debe seleccionar el estado del vehículo.")
            return

        vehiculo_encontrado = False

        try:
            with open(self.ruta_vehiculos, "r") as file:
                lineas = file.readlines()

            for i, linea in enumerate(lineas):
                palabras = linea.strip().split()
                if palabras and palabras[0] == placa:  # Validar si la placa coincide
                    palabras[-1] = self.estado_vehiculo  # Cambia el estado
                    lineas[i] = " ".join(palabras) + "\n"
                    vehiculo_encontrado = True
                    break

            if vehiculo_encontrado:
                with open(self.ruta_vehiculos, "w") as file:
                    file.writelines(lineas)

                messagebox.showinfo("Registro exitoso", f"Estado del vehículo {placa} actualizado a '{self.estado_vehiculo}'.")
                self.cargar_vehiculos()  # Actualizar lista de vehículos en la interfaz
            else:
                messagebox.showerror("Error", f"La placa {placa} no se encontró en el archivo.")

        except FileNotFoundError:
            messagebox.showerror("Error", f"No se encontró el archivo {self.ruta_vehiculos}")

    def abrir_ventana_principal(self):
        """Abre la ventana principal y oculta la de vehiculo temporalmente."""
        self.ventana.withdraw()  # Ocultar la ventana principal
        from Nomina_ing_software.intfz_grafica.Ventana_Principal_GUI.ventana_principal import Ventana_principal
        Ventana_principal()

if __name__ == "__main__":
    EstadoVehiculo()