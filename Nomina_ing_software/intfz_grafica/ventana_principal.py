import tkinter as tk

def ventana_principal():
    # Crear una nueva ventana
    ventana = tk.Toplevel()
    ventana.title("Ventana Principal")
    ventana.geometry("600x400")

    # Contenido de la ventana principal
    tk.Label(ventana, text="¡Bienvenido a la Ventana Principal!", font=("Arial", 18)).pack(pady=50)
    tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=20)

    # Bucle principal
    ventana.mainloop()

ventana_principal()