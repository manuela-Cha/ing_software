import tkinter as tk
from tkinter import messagebox


# Función para manejar el inicio de sesión
def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    if usuario == "admin" and contraseña == "1234":  # Ejemplo de credenciales
        messagebox.showinfo("Inicio de sesión", "¡Inicio de sesión exitoso!")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para manejar el caso de "Olvidé mi contraseña"
def olvidar_contraseña():
    messagebox.showinfo("Recuperar contraseña", "Se enviará un correo para recuperar tu contraseña")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")

# Configurar la ventana para que ocupe toda la pantalla
ventana.geometry(f"{ventana.winfo_screenwidth()}x{ventana.winfo_screenheight()}")

# Etiqueta y campo de entrada para el usuario
frame_central = tk.Frame(ventana)
frame_central.pack(expand=True)

tk.Label(frame_central, text="Usuario:", font=("Arial", 14)).pack(pady=10)
entry_usuario = tk.Entry(frame_central, font=("Arial", 14))
entry_usuario.pack(pady=5)

# Etiqueta y campo de entrada para la contraseña
tk.Label(frame_central, text="Contraseña:", font=("Arial", 14)).pack(pady=10)
entry_contraseña = tk.Entry(frame_central, show="*", font=("Arial", 14))
entry_contraseña.pack(pady=5)

# Botón para iniciar sesión
boton_login = tk.Button(frame_central, text="Iniciar sesión", font=("Arial", 14), command=iniciar_sesion)
boton_login.pack(pady=10)

# Botón para "Olvidé mi contraseña"
boton_olvidar = tk.Button(frame_central, text="Olvidé mi contraseña", font=("Arial", 14), command=olvidar_contraseña)
boton_olvidar.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
