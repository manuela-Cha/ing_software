import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

class Añadir_admin:
    def __init__(self):
        # Creación de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Añadir Administrador")
        self.ventana.geometry("500x400")  # Ajusté el tamaño porque hay menos campos
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
        label_usuario = tk.Label(self.main_container, 
                               text="Usuario:", 
                               bg=self.color_bg, 
                               fg=self.color_text,
                               font=self.font_subtitle)
        label_usuario.pack(pady=5)
        
        self.entry_usuario = tk.Entry(self.main_container, 
                                    width=30,
                                    bg=self.color_white,
                                    fg=self.color_text,
                                    font=self.font_normal,
                                    insertbackground=self.color_text)
        self.entry_usuario.pack(pady=5)

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
                                        insertbackground=self.color_text,
                                        show="*")  # Oculta la contraseña
        self.entry_contrasenia.pack(pady=5)

        # Botón para añadir admin
        self.boton_agregar = tk.Button(self.main_container, 
                                     text="Añadir Administrador",
                                     command=self.agregar_admin,
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
                                    command=self.abrir_ventana_principal,  # Solo cierra la ventana por ahora
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

    def abrir_ventana_principal(self):
            self.ventana.withdraw()
            from intfz_grafica.Ventana_Principal_GUI.ventana_principal import Ventana_principal
            Ventana_principal()

    def mostrar_ayuda(self):
        """Muestra una ventana de ayuda."""
        help_window = tk.Toplevel(self.ventana)
        help_window.title("Ayuda")
        help_window.geometry("400x400")
        help_window.configure(bg=self.color_white)
        help_window.transient(self.ventana)
        help_window.grab_set()

        # Contenido de ayuda
        content_frame = tk.Frame(help_window, bg=self.color_white)
        content_frame.pack(expand=True, fill='both', padx=10, pady=10)

        tk.Label(content_frame,
                text="Ayuda - Añadir Administrador",
                font=self.font_subtitle,
                bg=self.color_white,
                fg=self.color_text).pack(pady=(0, 10))

        help_text = """Instrucciones:
- Usuario: Ingrese el nombre de usuario del administrador.
- Contraseña: Ingrese una contraseña segura para el administrador.
- Añadir Administrador: Haga clic para registrar el nuevo admin.
- Cerrar: Cierra la ventana actual.

Nota: Todos los campos son obligatorios y el usuario no debe estar registrado previamente."""
        
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
                 command=self.ventana.destroy,
                 activebackground=self.color_secondary,
                 relief="flat",
                 padx=10,
                 pady=5).pack(pady=(10, 0))
        
    

    def agregar_admin(self):
        # Obtener datos ingresados
        usuario = self.entry_usuario.get().strip()
        contrasenia = self.entry_contrasenia.get().strip()

        # Verificar que no haya campos vacíos
        if not usuario or not contrasenia:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Verificar si el usuario ya existe en el archivo
        try:
            with open('Nomina_ing_software/archivos_de_texto/Usuarios_y_contras.txt', 'r') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    datos = linea.strip().split(" ")
                    if len(datos) >= 1 and datos[0] == usuario:
                        messagebox.showerror("Error", "El usuario ya existe.")
                        return
        except FileNotFoundError:
            # Si el archivo no existe, se creará al escribir
            pass

        # Si no existe, agregar el admin al archivo
        with open('Nomina_ing_software/archivos_de_texto/Usuarios_y_contras.txt', 'a') as archivo:
            archivo.write(f"{usuario} {contrasenia} admin\n")
        
        messagebox.showinfo("Éxito", "Administrador añadido correctamente.")
        
        # Limpiar los campos de entrada
        self.entry_usuario.delete(0, tk.END)
        self.entry_contrasenia.delete(0, tk.END)

if __name__ == "__main__":
    Añadir_admin()