import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

class Registrar_empleado_GUI:
    def __init__(self):
        # Creación de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Agregar Empleado")
        self.ventana.geometry("500x500")
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

        # Etiquetas y campos de entrada
        label_nombre = tk.Label(self.main_container, 
                              text="Nombre:", 
                              bg=self.color_bg, 
                              fg=self.color_text,
                              font=self.font_subtitle)
        label_nombre.pack(pady=5)
        
        self.entry_nombre = tk.Entry(self.main_container, 
                                   width=30,
                                   bg=self.color_white,
                                   fg=self.color_text,
                                   font=self.font_normal,
                                   insertbackground=self.color_text)
        self.entry_nombre.pack(pady=5)

        label_apellido = tk.Label(self.main_container, 
                                text="Apellido:", 
                                bg=self.color_bg,
                                fg=self.color_text,
                                font=self.font_subtitle)
        label_apellido.pack(pady=5)
        
        self.entry_apellido = tk.Entry(self.main_container, 
                                     width=30,
                                     bg=self.color_white,
                                     fg=self.color_text,
                                     font=self.font_normal,
                                     insertbackground=self.color_text)
        self.entry_apellido.pack(pady=5)

        label_cedula = tk.Label(self.main_container, 
                               text="Cedula:", 
                               bg=self.color_bg,
                               fg=self.color_text,
                               font=self.font_subtitle)
        label_cedula.pack(pady=5)
        
        self.entry_cedula = tk.Entry(self.main_container, 
                                   width=30,
                                   bg=self.color_white,
                                   fg=self.color_text,
                                   font=self.font_normal,
                                   insertbackground=self.color_text)
        self.entry_cedula.pack(pady=5)

        label_contrasenia = tk.Label(self.main_container, 
                                   text="Contraseña:", 
                                   bg=self.color_bg,
                                   fg=self.color_text,
                                   font=self.font_subtitle)
        label_contrasenia.pack(pady=5)
        
        self.entry_contrasenia = tk.Entry(self.main_container, 
                                        width=30,
                                        bg=self.color_white,
                                        fg=self.color_text,
                                        font=self.font_normal,
                                        insertbackground=self.color_text)
        self.entry_contrasenia.pack(pady=5)

        """label_ruta = tk.Label(self.main_container, 
                            text="Ruta asignada:", 
                            bg=self.color_bg,
                            fg=self.color_text,
                            font=self.font_subtitle)
        label_ruta.pack(pady=5)
        
        self.entry_ruta_asignada = tk.Entry(self.main_container, 
                                          width=30,
                                          bg=self.color_white,
                                          fg=self.color_text,
                                          font=self.font_normal,
                                          insertbackground=self.color_text)
        self.entry_ruta_asignada.pack(pady=5)"""

        # Botón para agregar empleado
        self.boton_agregar = tk.Button(self.main_container, 
                                     text="Agregar Empleado",
                                     command=self.agregar_empleado,
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

        # Footer con copyright y botón de ayuda
        self.create_footer()

        # Iniciar el bucle de la interfaz gráfica
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
                text="Ayuda - Agregar Empleado",
                font=self.font_subtitle,
                bg=self.color_white,
                fg=self.color_text).pack(pady=(0, 10))

        help_text = """Instrucciones:
- Nombre: Ingrese el nombre del empleado.
- Apellido: Ingrese el apellido del empleado.
- Cédula: Ingrese el número de cédula (único).
- Contraseña: Ingrese una contraseña para el empleado.
- Agregar Empleado: Haga clic para registrar el empleado.
- Cerrar: Regresa al Panel de Administración.

Nota: Todos los campos son obligatorios y la cédula no debe estar registrada previamente."""
        
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

    def agregar_empleado(self):
        # Obtener datos ingresados
        nombre = self.entry_nombre.get().strip().lower()
        apellido = self.entry_apellido.get().strip().lower()
        cedula = self.entry_cedula.get().strip()
        contrasenia = self.entry_contrasenia.get().strip()

        # Verificar que no haya campos vacíos
        if not nombre or not apellido or not cedula:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Verificar si la cédula ya existe en el archivo
        with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(" ")
                if len(datos) >= 3:  # Changed from == 3 to >= 3 to handle existing files with more fields
                    cedula_archivo = datos[2]
                    if cedula == cedula_archivo:
                        messagebox.showerror("Error", "El empleado ya existe.")
                        return

        # Si no existe, agregar el empleado al archivo
        with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'a') as archivo:
            archivo.write(f"{nombre} {apellido} {cedula} Disponible\n")

        with open('Nomina_ing_software/archivos_de_texto/Usuarios_y_contras.txt', 'a') as archivo:
            archivo.write(f"{cedula} {contrasenia} empleado\n")
        
        messagebox.showinfo("Éxito", "Empleado agregado correctamente.")
        
        # Limpiar los campos de entrada
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_cedula.delete(0, tk.END)
        self.entry_contrasenia.delete(0, tk.END)
        """self.entry_ruta_asignada.delete(0, tk.END)"""

    def abrir_ventana_principal(self):
        """Abre la ventana principal y oculta la de empleado temporalmente."""
        self.ventana.withdraw()  # Ocultar la ventana principal
        from intfz_grafica.Ventana_Principal_GUI.ventana_principal import Ventana_principal
        Ventana_principal()

if __name__ == "__main__":
    Registrar_empleado_GUI()