import tkinter as tk
from tkinter import messagebox, font

class Login:
    def __init__(self):
        # Definir colores
        self.color_primary = "#2ECC71"      # Verde principal
        self.color_secondary = "#27AE60"    # Verde secundario
        self.color_accent = "#1E8449"       # Verde oscuro para acentos
        self.color_bg = "#F5F5F5"           # Fondo gris muy claro
        self.color_text = "#2C3E50"         # Texto oscuro
        self.color_white = "#FFFFFF"        # Blanco puro
        
        # Inicializar ventana
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de Sesión")
        self.ventana.geometry("600x600")
        self.ventana.configure(bg=self.color_bg)
        
        # Crear fuentes personalizadas
        self.font_title = font.Font(family="Helvetica", size=16, weight="bold")
        self.font_subtitle = font.Font(family="Helvetica", size=12, weight="bold")
        self.font_button = font.Font(family="Helvetica", size=10, weight="bold")
        self.font_normal = font.Font(family="Helvetica", size=10)
        
        # Crear frame central con borde redondeado y sombra
        frame_central = tk.Frame(self.ventana, bg=self.color_white, padx=40, pady=40,
                                highlightbackground=self.color_secondary, highlightthickness=2)
        frame_central.pack(expand=True, pady=80)
        
        # Logo o título principal
        titulo = tk.Label(frame_central, text="Sistema de Nómina", font=self.font_title, 
                          bg=self.color_white, fg=self.color_primary)
        titulo.pack(pady=(0, 30))
        
        # Etiqueta y campo de entrada para el usuario
        frame_usuario = tk.Frame(frame_central, bg=self.color_white)
        frame_usuario.pack(fill="x", pady=10)
        
        tk.Label(frame_usuario, text="Usuario:", font=self.font_subtitle, 
                 bg=self.color_white, fg=self.color_text, anchor="w").pack(fill="x")
        
        self.entry_usuario = tk.Entry(frame_usuario, font=self.font_normal, 
                                     bd=0, highlightthickness=1, highlightbackground=self.color_secondary)
        self.entry_usuario.pack(fill="x", ipady=8, pady=(5, 0))
        
        # Etiqueta y campo de entrada para la contraseña
        frame_password = tk.Frame(frame_central, bg=self.color_white)
        frame_password.pack(fill="x", pady=10)
        
        tk.Label(frame_password, text="Contraseña:", font=self.font_subtitle, 
                 bg=self.color_white, fg=self.color_text, anchor="w").pack(fill="x")
        
        self.entry_contraseña = tk.Entry(frame_password, show="•", font=self.font_normal, 
                                        bd=0, highlightthickness=1, highlightbackground=self.color_secondary)
        self.entry_contraseña.pack(fill="x", ipady=8, pady=(5, 0))
        
        # Botón para iniciar sesión
        frame_boton = tk.Frame(frame_central, bg=self.color_white)
        frame_boton.pack(fill="x", pady=(20, 10))
        
        boton_login = tk.Button(frame_boton, text="INICIAR SESIÓN", font=self.font_button, 
                               bg=self.color_primary, fg=self.color_white, activebackground=self.color_accent,
                               relief="flat", command=self.verificar_login, cursor="hand2")
        boton_login.pack(fill="x", ipady=10)
        
        # Iniciar la ventana
        self.ventana.mainloop()

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contraseña.get()
        
        try:
            with open("Nomina_ing_software/archivos_de_texto/Usuarios_y_contras.txt", "r") as file:
                for linea in file:
                    datos = linea.strip().split()
                    if len(datos) == 3:
                        user, password, role = datos
                        if user == usuario and password == contrasena:
                            messagebox.showinfo("Inicio de sesión", "¡Inicio de sesión exitoso!")
                            self.ventana.destroy()  # Cierra la ventana de login
                            if role.lower() == "admin":
                                from intfz_grafica.Ventana_Principal_GUI.ventana_principal import Ventana_principal
                                #Ventana_principal()
                            else:
                                from intfz_grafica.Ventana_Empleado_GUI.ventana_empleado import Ventana_Empleado_GUI
                                Ventana_Empleado_GUI(usuario)
                            return
            
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo de usuarios")
