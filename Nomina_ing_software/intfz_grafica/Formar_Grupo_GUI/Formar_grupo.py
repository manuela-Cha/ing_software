from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import tkinter.font as font

class Formar_Grupo_GUI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Formación de grupos")
        self.geometry("500x500")
        self.resizable(False, False)

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
        self.configure(bg=self.color_bg)

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
        self.main_frame = Frame(self, bg=self.color_bg)
        self.main_frame.pack(padx=20, pady=20, expand=True, fill='both')
        
        # Título
        Label(self.main_frame, 
              text="Formación de Grupo de Trabajo", 
              font=self.font_title,
              bg=self.color_bg,
              fg=self.color_text).pack(pady=10)
        
        # Creación frames de trabajadores
        for i in range(3):
            self.frameTrabajador(i)
        
        # Frame para vehículo
        self.frameVehiculo = Frame(self.main_frame, pady=10, bg=self.color_bg)
        self.vehiculoLabel = Label(self.frameVehiculo, 
                                 text="Seleccione el vehículo a asignar",
                                 bg=self.color_bg,
                                 fg=self.color_text,
                                 font=self.font_subtitle)
        self.vehiculoOpciones = OptionMenu(self.frameVehiculo, 
                                         self.valorVehiculo, 
                                         *self.vehiculos_disponibles)
        self.vehiculoOpciones.config(bg=self.color_white,
                                   fg=self.color_text,
                                   font=self.font_normal,
                                   activebackground=self.color_secondary,
                                   activeforeground=self.color_white)
        self.vehiculoLabel.pack()
        self.vehiculoOpciones.pack()
        self.frameVehiculo.pack()
        
        # Frame para fecha
        self.frameFecha = Frame(self.main_frame, pady=10, bg=self.color_bg)
        Label(self.frameFecha, 
              text="Fecha de creación del grupo",
              bg=self.color_bg,
              fg=self.color_text,
              font=self.font_subtitle).pack()
        
        # Frame para los campos de fecha
        fecha_campos = Frame(self.frameFecha, bg=self.color_bg)
        
        # Día
        Label(fecha_campos, 
              text="Día:", 
              bg=self.color_bg,
              fg=self.color_text,
              font=self.font_normal).grid(row=0, column=0, padx=5)
        dias = [str(i).zfill(2) for i in range(1, 32)]
        self.dia.set(datetime.now().strftime("%d"))
        dia_combo = ttk.Combobox(fecha_campos, 
                               textvariable=self.dia, 
                               values=dias, 
                               width=3)
        dia_combo.grid(row=0, column=1)
        
        # Mes
        Label(fecha_campos, 
              text="Mes:", 
              bg=self.color_bg,
              fg=self.color_text,
              font=self.font_normal).grid(row=0, column=2, padx=5)
        meses = [str(i).zfill(2) for i in range(1, 13)]
        self.mes.set(datetime.now().strftime("%m"))
        mes_combo = ttk.Combobox(fecha_campos, 
                               textvariable=self.mes, 
                               values=meses, 
                               width=3)
        mes_combo.grid(row=0, column=3)
        
        # Año
        Label(fecha_campos, 
              text="Año:", 
              bg=self.color_bg,
              fg=self.color_text,
              font=self.font_normal).grid(row=0, column=4, padx=5)
        anios = [str(i) for i in range(2024, 2035)]
        self.anio.set(datetime.now().strftime("%Y"))
        anio_combo = ttk.Combobox(fecha_campos, 
                                textvariable=self.anio, 
                                values=anios, 
                                width=5)
        anio_combo.grid(row=0, column=5)
        
        # Estilizar Combobox
        style = ttk.Style()
        style.configure("TCombobox", 
                       fieldbackground=self.color_white,
                       background=self.color_white,
                       foreground=self.color_text)
        
        fecha_campos.pack(pady=5)
        self.frameFecha.pack()
        
        # Botón de confirmación
        self.confirm = Button(self.main_frame, 
                            bg=self.color_primary, 
                            fg=self.color_white,
                            text="Confirmar selecciones",
                            command=self.verificacion,
                            font=self.font_button,
                            activebackground=self.color_secondary,
                            activeforeground=self.color_white,
                            relief="flat",
                            padx=10,
                            pady=5)
        self.confirm.pack(pady=20)
        
        # Footer con copyright y botón de ayuda
        self.create_footer()

        self.mainloop()

    def create_footer(self):
        """Crea el pie de página con copyright y botón de ayuda."""
        footer_frame = Frame(self.main_frame, bg=self.color_accent, height=30)
        footer_frame.pack(fill='x', pady=(15, 0))

        # Texto de copyright
        copyright_label = Label(footer_frame,
                                text="© 2025 Sistema de Gestión de Rutas - v1.0",
                                bg=self.color_accent,
                                fg=self.color_white,
                                font=("Helvetica", 8))
        copyright_label.pack(side='left', padx=10, pady=5)

        # Botón de ayuda
        help_button = Button(footer_frame,
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

    def mostrar_ayuda(self):
        """Muestra una ventana de ayuda."""
        help_window = Toplevel(self)
        help_window.title("Ayuda")
        help_window.geometry("400x350")
        help_window.configure(bg=self.color_white)
        help_window.transient(self)
        help_window.grab_set()

        # Contenido de ayuda
        content_frame = Frame(help_window, bg=self.color_white)
        content_frame.pack(expand=True, fill='both', padx=10, pady=10)

        Label(content_frame,
              text="Ayuda - Formación de Grupos",
              font=self.font_subtitle,
              bg=self.color_white,
              fg=self.color_text).pack(pady=(0, 10))

        help_text = """Instrucciones:
- Trabajadores: Seleccione 3 trabajadores distintos de las listas desplegables.
- Vehículo: Elija un vehículo disponible del menú.
- Fecha: Ajuste la fecha de creación del grupo (día, mes, año).
- Confirmar: Haga clic para formar el grupo y registrarlo.

Nota:
- Todos los campos son obligatorios.
- Los trabajadores deben ser únicos.
- La fecha debe ser válida."""
        
        Label(content_frame,
              text=help_text,
              font=self.font_normal,
              bg=self.color_white,
              fg=self.color_text,
              justify="left",
              wraplength=380).pack(pady=10)

        # Botón de cerrar
        Button(content_frame,
               text="Cerrar",
               font=self.font_normal,
               bg=self.color_accent,
               fg=self.color_white,
               command=help_window.destroy,
               activebackground=self.color_secondary,
               relief="flat",
               padx=10,
               pady=5).pack(pady=(10, 0))

    def frameTrabajador(self, number):
        aux = Frame(self.main_frame, bg=self.color_bg)
        auxLabel = Label(aux, 
                        text=f"Trabajador {number + 1}",
                        bg=self.color_bg,
                        fg=self.color_text,
                        font=self.font_subtitle)
        
        opciones_disponibles = self.trabajadores_disponibles if number == 0 else ['']
        menu = OptionMenu(aux, self.valores[number], *opciones_disponibles)
        menu.config(bg=self.color_white,
                   fg=self.color_text,
                   font=self.font_normal,
                   activebackground=self.color_secondary,
                   activeforeground=self.color_white)
        self.trabajador_menus.append(menu)
        
        auxLabel.grid(row=number, column=0, padx=5)
        menu.grid(row=number, column=1, padx=5)
        aux.pack(pady=5)

    def obtener_fecha_seleccionada(self):
        return f"{self.anio.get()}-{self.mes.get()}-{self.dia.get()}"

    def registrar_grupo(self, trabajadores_seleccionados, vehiculo_seleccionado, fecha):
        cedulas = {}
        with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(" ")
                nombre_completo = datos[0] + " " + datos[1]
                if nombre_completo in trabajadores_seleccionados:
                    cedulas[nombre_completo] = datos[2]

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
        
        self.registrar_grupo(trabajadores_seleccionados, vehiculo_seleccionado, fecha_seleccionada)
        
        with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
            lineas = archivo.readlines()
        with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'w') as archivo:
            for linea in lineas:
                datos = linea.strip().split(" ")
                if datos[0] + " " + datos[1] in trabajadores_seleccionados:
                    archivo.write(f"{datos[0]} {datos[1]} {datos[2]} Ocupado\n")
                else:
                    archivo.write(linea)
        
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
        
        try:
            fecha = self.obtener_fecha_seleccionada()
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Error", "La fecha seleccionada no es válida")
            return
        
        if vehiculo_seleccionado == "":
            messagebox.showwarning("Error", "Por favor seleccione un vehículo")
            return
            
        if "" in trabajadores_seleccionados:
            messagebox.showwarning("Error", "Todos los trabajadores deben ser seleccionados, por favor verifique")
            return
            
        if len(trabajadores_seleccionados) != len(set(trabajadores_seleccionados)):
            messagebox.showwarning("Error", "Los trabajadores seleccionados deben ser distintos y todos deben estar asignados, por favor verifique")
            return
        
        self.actualizacion_archivo(trabajadores_seleccionados, vehiculo_seleccionado)
    
    def actualizar_opciones(self, menu_index):
        seleccionados = [var.get() for var in self.valores[:menu_index]]
        opciones_disponibles = [t for t in self.trabajadores_disponibles if t not in seleccionados]
        
        menu = self.trabajador_menus[menu_index]
        menu['menu'].delete(0, 'end')
        
        for opcion in opciones_disponibles:
            menu['menu'].add_command(
                label=opcion,
                command=lambda o=opcion: self.valores[menu_index].set(o)
            )

    def obtener_trabajadores_disponibles(self):
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

if __name__ == "__main__":
    Formar_Grupo_GUI()