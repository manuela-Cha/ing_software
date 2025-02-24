from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class Formar_Grupo_GUI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Formación de grupos")
        self.geometry("500x600")
        
        # Obtener listas actualizadas al crear la instancia
        self.trabajadores_disponibles = self.obtener_trabajadores_disponibles()
        self.vehiculos_disponibles = self.obtener_vehiculos_disponibles()
        
        # Valores para retornar las selecciones
        self.valores = [StringVar(self) for i in range(3)]
        self.valorVehiculo = StringVar(self)
        
        # Variables para la fecha
        self.dia = StringVar(self)
        self.mes = StringVar(self)
        self.anio = StringVar(self)
        
        # Añadir trace a los StringVar para actualizar las opciones
        self.valores[0].trace('w', lambda *args: self.actualizar_opciones(1))
        self.valores[1].trace('w', lambda *args: self.actualizar_opciones(2))
        
        # Almacenar los OptionMenu para poder actualizarlos
        self.trabajador_menus = []
        
        # Frame principal
        self.main_frame = Frame(self)
        self.main_frame.pack(padx=20, pady=20, expand=True, fill='both')
        
        # Título
        Label(self.main_frame, text="Formación de Grupo de Trabajo", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Creación frames de trabajadores
        for i in range(3):
            self.frameTrabajador(i)
        
        # Frame para vehículo
        self.frameVehiculo = Frame(self.main_frame, pady=10)
        self.vehiculoLabel = Label(self.frameVehiculo, text="Seleccione el vehículo a asignar")
        self.vehiculoOpciones = OptionMenu(self.frameVehiculo, self.valorVehiculo, *self.vehiculos_disponibles)
        self.vehiculoLabel.pack()
        self.vehiculoOpciones.pack()
        self.frameVehiculo.pack()
        
        # Frame para fecha
        self.frameFecha = Frame(self.main_frame, pady=10)
        Label(self.frameFecha, text="Fecha de creación del grupo").pack()
        
        # Frame para los campos de fecha
        fecha_campos = Frame(self.frameFecha)
        
        # Día
        Label(fecha_campos, text="Día:").grid(row=0, column=0, padx=5)
        dias = [str(i).zfill(2) for i in range(1, 32)]
        self.dia.set(datetime.now().strftime("%d"))
        ttk.Combobox(fecha_campos, textvariable=self.dia, values=dias, width=3).grid(row=0, column=1)
        
        # Mes
        Label(fecha_campos, text="Mes:").grid(row=0, column=2, padx=5)
        meses = [str(i).zfill(2) for i in range(1, 13)]
        self.mes.set(datetime.now().strftime("%m"))
        ttk.Combobox(fecha_campos, textvariable=self.mes, values=meses, width=3).grid(row=0, column=3)
        
        # Año
        Label(fecha_campos, text="Año:").grid(row=0, column=4, padx=5)
        anios = [str(i) for i in range(2024, 2035)]
        self.anio.set(datetime.now().strftime("%Y"))
        ttk.Combobox(fecha_campos, textvariable=self.anio, values=anios, width=5).grid(row=0, column=5)
        
        fecha_campos.pack(pady=5)
        self.frameFecha.pack()
        
        # Botón de confirmación
        self.confirm = Button(self.main_frame, bg="#AAA000", text="Confirmar selecciones",
                            command=self.verificacion, pady=5)
        self.confirm.pack(pady=20)
        
        self.mainloop()

    

    def obtener_fecha_seleccionada(self):
        return f"{self.anio.get()}-{self.mes.get()}-{self.dia.get()}"

    def registrar_grupo(self, trabajadores_seleccionados, vehiculo_seleccionado, fecha):
        # Obtener las cédulas de los trabajadores seleccionados
        cedulas = {}
        with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(" ")
                nombre_completo = datos[0] + " " + datos[1]
                if nombre_completo in trabajadores_seleccionados:
                    cedulas[nombre_completo] = datos[2]

        # Registrar el grupo en Grupos.txt
        with open('Nomina_ing_software/archivos_de_texto/Grupos.txt', 'a') as archivo:
            archivo.write(f"\nGRUPO CREADO EN FECHA: {fecha}\n")
            archivo.write("Integrantes:\n")
            for trabajador in trabajadores_seleccionados:
                archivo.write(f"- {trabajador} (CC: {cedulas[trabajador]})\n")
            archivo.write(f"Vehiculo asignado: {vehiculo_seleccionado}\n")
            archivo.write(f"Estado: Disponible\n")
            archivo.write("-" * 50 + "\n")

    def actualizacion_archivo(self, trabajadores_seleccionados, vehiculo_seleccionado):
        fecha_seleccionada = self.obtener_fecha_seleccionada()
        
        # Registrar el grupo
        self.registrar_grupo(trabajadores_seleccionados, vehiculo_seleccionado, fecha_seleccionada)
        
        # Actualizar el archivo de empleados
        with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
            lineas = archivo.readlines()
        with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'w') as archivo:
            for linea in lineas:
                datos = linea.strip().split(" ")
                if datos[0] + " " + datos[1] in trabajadores_seleccionados:
                    archivo.write(f"{datos[0]} {datos[1]} {datos[2]} Ocupado\n")
                else:
                    archivo.write(linea)
        
        # Actualizar el archivo de vehículos
        with open('Nomina_ing_software/archivos_de_texto/Vehiculos.txt', 'r') as archivo:
            lineas = archivo.readlines()
        with open('Nomina_ing_software/archivos_de_texto/Vehiculos.txt', 'w') as archivo:
            for linea in lineas:
                datos = linea.strip().split(" ")
                if datos[0] == vehiculo_seleccionado:
                    archivo.write(f"{datos[0]} Ocupado\n")
                else:
                    archivo.write(linea)
        
        messagebox.showinfo("Éxito", "Grupo formado y registrado correctamente.")
        self.destroy()
        from intfz_grafica.Ventana_Principal_GUI.ventana_principal import Ventana_principal
        Ventana_principal()
    
    def verificacion(self):
        trabajadores_seleccionados = [self.valores[0].get(), self.valores[1].get(), self.valores[2].get()]
        vehiculo_seleccionado = self.valorVehiculo.get()
        
        # Verificación de fecha válida
        try:
            fecha = self.obtener_fecha_seleccionada()
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Error", "La fecha seleccionada no es válida")
            return
        
        # Verificacion de que se escogió vehículo
        if vehiculo_seleccionado == "":
            messagebox.showwarning("Error", "Por favor seleccione un vehículo")
            return
            
        # Verificacion de que todos los campos tengan trabajador
        if "" in trabajadores_seleccionados:
            messagebox.showwarning("Error", "Todos los trabajadores deben ser seleccionados, por favor verifique")
            return
            
        # Verificacion de que todos los trabajadores sean distintos
        if len(trabajadores_seleccionados) != len(set(trabajadores_seleccionados)):
            messagebox.showwarning("Error", "Los trabajadores seleccionados deben ser distintos y todos deben estar asignados, por favor verifique")
            return
        
        # Llamar a actualizacion_archivo con los parámetros necesarios
        self.actualizacion_archivo(trabajadores_seleccionados, vehiculo_seleccionado)
    
    def frameTrabajador(self, number):
        aux = Frame(self.main_frame)
        auxLabel = Label(aux, text=f"Trabajador {number + 1}")
        
        # Usar self.trabajadores_disponibles en lugar de la variable global
        opciones_disponibles = self.trabajadores_disponibles if number == 0 else ['']
        menu = OptionMenu(aux, self.valores[number], *opciones_disponibles)
        self.trabajador_menus.append(menu)
        
        auxLabel.grid(row=number, column=0, padx=5)
        menu.grid(row=number, column=1, padx=5)
        aux.pack(pady=5)
    
    def actualizar_opciones(self, menu_index):
        # Obtener trabajadores ya seleccionados
        seleccionados = [var.get() for var in self.valores[:menu_index]]
        
        # Filtrar las opciones disponibles usando self.trabajadores_disponibles
        opciones_disponibles = [t for t in self.trabajadores_disponibles if t not in seleccionados]
        
        # Actualizar el menú correspondiente
        menu = self.trabajador_menus[menu_index]
        menu['menu'].delete(0, 'end')
        
        for opcion in opciones_disponibles:
            menu['menu'].add_command(
                label=opcion,
                command=lambda o=opcion: self.valores[menu_index].set(o)
            )

    def obtener_trabajadores_disponibles(self):
            """Método para obtener la lista actualizada de trabajadores disponibles"""
            trabajadores_dispo = []
            try:
                with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
                    for linea in archivo:
                        datos = linea.strip().split(" ")
                        if datos[3] == "Disponible":
                            nombre_completo = datos[0] + " " + datos[1]
                            trabajadores_dispo.append(nombre_completo)
            except Exception as e:
                messagebox.showerror("Error", f"Error al leer archivo de empleados: {str(e)}")
            return trabajadores_dispo

    def obtener_vehiculos_disponibles(self):
        """Método para obtener la lista actualizada de vehículos disponibles"""
        vehiculos_dispo = []
        try:
            with open('Nomina_ing_software/archivos_de_texto/Vehiculos.txt', 'r') as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" ")
                    if datos[1] == "Disponible":
                        vehiculos_dispo.append(datos[0])
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer archivo de vehículos: {str(e)}")
        return vehiculos_dispo

"""trabajadores_disponibles = trabajadores_disponibles()
vehiculos_disponibles = vehiculos_disponibles()"""

"""if __name__ == "__main__":
    Formar_Grupo_GUI()"""