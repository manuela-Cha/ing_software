import tkinter as tk
from tkinter import messagebox

class EstadoVehiculo:
    def __init__(self):
        # Ruta del archivo donde se almacenan los vehículos
        self.ruta_vehiculos = "Nomina_ing_software/archivos_de_texto/Vehiculos.txt"

        # Creación de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Estado de Vehículo")
        self.ventana.geometry("500x450")

        # Etiqueta y campo para la placa
        tk.Label(self.ventana, text="Placa:").pack(pady=5)
        self.entry_placa = tk.Entry(self.ventana, width=30)
        self.entry_placa.pack(pady=5)

        self.estado_vehiculo = None

        # Etiqueta para seleccionar estado
        tk.Label(self.ventana, text="Seleccione el estado del vehículo:").pack(pady=5)

        # Frame para los botones de estado
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=5)

        self.boton_optimo = tk.Button(frame_botones, text="optimo", width=12, command=lambda: self.seleccionar_estado("optimo"))
        self.boton_optimo.pack(side=tk.LEFT, padx=5)

        self.boton_no_optimo = tk.Button(frame_botones, text="No optimo", width=12, command=lambda: self.seleccionar_estado("En revision"))
        self.boton_no_optimo.pack(side=tk.LEFT, padx=5)

        # Botón para registrar
        self.boton_registrar = tk.Button(self.ventana, text="Registrar estado del vehiculo", command=self.registrar_vehiculo)
        self.boton_registrar.pack(pady=10)

        #Botón para cerrar
        self.boton_cerrar = tk.Button(self.ventana, text="Cerrar", command=self.abrir_ventana_principal)
        self.boton_cerrar.pack(pady=10)

        # Área para mostrar vehículos existentes
        tk.Label(self.ventana, text="Vehículos registrados:").pack(pady=5)
        self.lista_vehiculos = tk.Listbox(self.ventana, width=50, height=10)
        self.lista_vehiculos.pack(pady=5)

        self.cargar_vehiculos()  # Cargar vehículos al iniciar

        self.ventana.mainloop()

    def seleccionar_estado(self, estado):
        """Actualiza el estado del vehículo seleccionado."""
        self.estado_vehiculo = estado

        if estado == "Óptimo":
            self.boton_optimo.config(bg="light blue", relief=tk.SUNKEN)
            self.boton_no_optimo.config(bg="SystemButtonFace", relief=tk.RAISED)
        else:
            self.boton_optimo.config(bg="SystemButtonFace", relief=tk.RAISED)
            self.boton_no_optimo.config(bg="light blue", relief=tk.SUNKEN)

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
        from intfz_grafica.ventana_principal import Ventana_principal
        Ventana_principal()
