import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de Sesión")
        self.ventana.geometry(f"{self.ventana.winfo_screenwidth()}x{self.ventana.winfo_screenheight()}")

        # Crear frame central
        frame_central = tk.Frame(self.ventana)
        frame_central.pack(expand=True)

        # Etiqueta y campo de entrada para el usuario
        tk.Label(frame_central, text="Usuario:", font=("Arial", 14)).pack(pady=10)
        self.entry_usuario = tk.Entry(frame_central, font=("Arial", 14))
        self.entry_usuario.pack(pady=5)

        # Etiqueta y campo de entrada para la contraseña
        tk.Label(frame_central, text="Contraseña:", font=("Arial", 14)).pack(pady=10)
        self.entry_contraseña = tk.Entry(frame_central, show="*", font=("Arial", 14))
        self.entry_contraseña.pack(pady=5)

        # Botón para iniciar sesión
        boton_login = tk.Button(frame_central, text="Iniciar sesión", font=("Arial", 14), command=self.verificar_login)
        boton_login.pack(pady=10)

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
                                Ventana_principal()
                            else:
                                from intfz_grafica.Ventana_Empleado_GUI.ventana_empleado import Ventana_Empleado_GUI
                                Ventana_Empleado_GUI(usuario)
                            return
            
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo de usuarios")

