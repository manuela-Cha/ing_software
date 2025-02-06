import tkinter as tk
from tkinter import messagebox

class EstadoVehiculo:
    def __init__(self):
        # Creación de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Estado de Vehículo")
        self.ventana.geometry("300x200")

        # Etiqueta y campo para la placa
        tk.Label(self.ventana, text="Placa").pack(pady=5)
        self.entry_placa = tk.Entry(self.ventana, width=30)
        self.entry_placa.pack(pady=5)

        self.estado_vehiculo = None

        tk.Label(self.ventana, text="Seleccione el estado del vehículo").pack(pady=5)

        
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=5)

        
        self.boton_optimo = tk.Button(frame_botones, text="Óptimo", width=12,command=lambda: self.seleccionar_estado("óptimo"))
        self.boton_optimo.pack(side=tk.LEFT, padx=5)  

        self.boton_no_optimo = tk.Button(frame_botones, text="No Óptimo", width=12,command=lambda: self.seleccionar_estado("no óptimo"))
        self.boton_no_optimo.pack(side=tk.LEFT, padx=5)

        # Botón para registrar
        self.boton_registrar = tk.Button(self.ventana, text="Registrar vehículo", command=self.registrar_vehiculo)
        self.boton_registrar.pack(pady=10)

        self.ventana.mainloop()

    def seleccionar_estado(self, estado):
        self.estado_vehiculo = estado

        if estado == "óptimo":
            self.boton_optimo.config(bg="light blue", relief=tk.SUNKEN)
            self.boton_no_optimo.config(bg="SystemButtonFace", relief=tk.RAISED) 
        else:
            self.boton_optimo.config(bg="SystemButtonFace", relief=tk.RAISED) 
            self.boton_no_optimo.config(bg="light blue", relief=tk.SUNKEN)

    def registrar_vehiculo(self):
        placa = self.entry_placa.get().strip().upper()  

        if not placa:
            messagebox.showwarning("Entrada inválida", "Debe ingresar la placa del vehículo.")
            return

        if not self.estado_vehiculo:
            messagebox.showwarning("Estado no seleccionado", "Debe seleccionar el estado del vehículo.")
            return

        if self.estado_vehiculo == "no óptimo":
            self.notificar_administracion(placa)
            return 

        messagebox.showinfo("Registro exitoso", f"Vehículo con placa {placa} registrado correctamente.")

    def notificar_administracion(self, placa):
        messagebox.showwarning("Notificación", f"El vehículo con placa {placa} no está en condiciones óptimas. Se notificará a la administración.")

# Ejecutar la aplicación
EstadoVehiculo()
