import tkinter as tk
from tkinter import messagebox
from BD import conexion
#from BD import conexion as conexion
#from intfz_grafica import registrar_empleado_gui
#from Nomina_ing_software.BD import conexion
#import Nomina_ing_software.BD.conexion as conexion
#import conexion
#from BD import conexion
#from ..BD import conexion


# Función para manejar el evento del botón
def manejar_agregar_empleado():
    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    
    # Validar que los campos no estén vacíos
    if not nombre or not apellido or not entry_pedidos.get().strip():
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    try:
        edad = int(entry_pedidos.get().strip())  # Convertir a entero
    except ValueError:
        messagebox.showerror("Error", "El número de pedidos debe ser un número entero.")
        return

    # Llamar a la función de agregar empleado
    conexion.registrar_empleado(nombre, apellido, edad)
    messagebox.showinfo("Éxito", "Empleado agregado correctamente.")

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Agregar Empleado")
ventana.geometry("400x300")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack(pady=5)

tk.Label(ventana, text="Apellido:").pack(pady=5)
entry_apellido = tk.Entry(ventana, width=30)
entry_apellido.pack(pady=5)

tk.Label(ventana, text="Edad:").pack(pady=5)
entry_pedidos = tk.Entry(ventana, width=30)
entry_pedidos.pack(pady=5)

# Botón para agregar empleado
boton_agregar = tk.Button(ventana, text="Agregar Empleado", command=manejar_agregar_empleado)
boton_agregar.pack(pady=20)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
