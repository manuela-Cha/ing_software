import tkinter as tk
from tkinter import messagebox 

class Eliminar_empleado_GUI:
    def __init__(self):
        # Creación de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Eliminar Empleado")
        self.ventana.geometry("500x450")

        # Etiquetas y campos de entrada
        tk.Label(self.ventana, text="Nombre:").pack(pady=5)
        self.entry_nombre = tk.Entry(self.ventana, width=30)
        self.entry_nombre.pack(pady=5)

        tk.Label(self.ventana, text="Apellido:").pack(pady=5)
        self.entry_apellido = tk.Entry(self.ventana, width=30)
        self.entry_apellido.pack(pady=5)

        tk.Label(self.ventana, text="Cedula:").pack(pady=5)
        self.entry_cedula = tk.Entry(self.ventana, width=30)
        self.entry_cedula.pack(pady=5)

        # Botón para eliminar empleado
        self.boton_eliminar = tk.Button(
            self.ventana, text="Eliminar Empleado",
            command=self.eliminar_empleado
        )
        self.boton_eliminar.pack(pady=20)

        #Botón para cerrar
        self.boton_cerrar = tk.Button(self.ventana, text="Cerrar", command=self.abrir_ventana_principal)
        self.boton_cerrar.pack(pady=10)

        # Iniciar el bucle de la interfaz gráfica
        self.ventana.mainloop()

    # Función para manejar el evento del botón
    def eliminar_empleado(self):
        nombre = self.entry_nombre.get().strip().lower()  # Convertir a minúsculas
        apellido = self.entry_apellido.get().strip().lower()  # Convertir a minúsculas
        cedula = self.entry_cedula.get().strip()  # La cédula se deja sin modificar

        # Validar que los campos no estén vacíos
        if not nombre or not apellido or not cedula:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Leer el archivo y verificar si el empleado existe
        empleado_encontrado = False
        with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
            lineas = archivo.readlines()

        # Revisar si el empleado está en alguna línea
        nueva_lista = []
        for linea in lineas:
            datos = linea.strip().split(" ")  
            if len(datos) == 4:  # Asegurarse de que tenga los 3 campos necesarios
                nombre_archivo = datos[0].lower()  # Convertir a minúsculas
                apellido_archivo = datos[1].lower()  # Convertir a minúsculas
                cedula_archivo = datos[2]  # La cédula se compara tal cual
                # Comparar sin importar mayúsculas y minúsculas
                if nombre == nombre_archivo and apellido == apellido_archivo and cedula == cedula_archivo:
                    empleado_encontrado = True
                    continue  # Saltar esta línea para eliminarla
            nueva_lista.append(linea)

        # Si el empleado fue encontrado, escribir el archivo sin esa línea
        if empleado_encontrado:
            with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'w') as archivo:
                archivo.writelines(nueva_lista)
        else:
            print(nombre, apellido, cedula, "|", nombre_archivo, apellido_archivo, cedula_archivo) 
            messagebox.showerror("Error","El empleado no existe en el archivo.")
        

        empleado_encontrado = False
        with open('Nomina_ing_software/archivos_de_texto/Usuarios_y_contras.txt', 'r') as archivo:
            lineas = archivo.readlines()

        # Revisar si el empleado está en alguna línea
        nueva_lista = []
        for linea in lineas:
            datos = linea.strip().split(" ") 
            if len(datos) == 3:  # Asegurarse de que tenga los 3 campos necesarios
                cedula_archivo = datos[0]  # La cédula se compara tal cual
                # Comparar sin importar mayúsculas y minúsculas
                if cedula == cedula_archivo:
                    empleado_encontrado = True
                    continue  # Saltar esta línea para eliminarla
            nueva_lista.append(linea)

        # Si el empleado fue encontrado, escribir el archivo sin esa línea
        if empleado_encontrado:
            with open('Nomina_ing_software/archivos_de_texto/Usuarios_y_contras.txt', 'w') as archivo:
                archivo.writelines(nueva_lista)
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
        else:
            messagebox.showerror("Error", "El empleado no existe en el archivo.")


    def abrir_ventana_principal(self):
        """Abre la ventana principal y oculta la de vehiculo temporalmente."""
        self.ventana.withdraw()  # Ocultar la ventana principal
        from intfz_grafica.Ventana_Principal_GUI.ventana_principal import Ventana_principal
        Ventana_principal()