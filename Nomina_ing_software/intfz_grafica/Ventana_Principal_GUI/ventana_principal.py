import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from intfz_grafica.Estado_Vehiculo_GUI.Registrar_estado import EstadoVehiculo  
from intfz_grafica.Eliminar_Empleado_GUI.eliminar_empleado_gui import Eliminar_empleado_GUI
from intfz_grafica.Registrar_Empleado_GUI.registrar_empleado_gui import Registrar_empleado_GUI
from intfz_grafica.Registrar_Vehiculo_GUI.registrar_vehiculo_gui import RegistrarvehiculoGUI
from intfz_grafica.Formar_Grupo_GUI.Formar_grupo import Formar_Grupo_GUI
from intfz_grafica.Asignar_rutas_GUI.Asignar_rutas import GestorGruposRutasGUI
from intfz_grafica.Visualizador_Empleados_GUI.Visualizador_empleados import VisualizadorEmpleados
from intfz_grafica.Visualizador_Vehiculos_GUI.visualizador_de_vehiculos import VisualizadorVehiculos
from intfz_grafica.Añadir_Admin_GUI.añadir_admin import Añadir_admin
from intfz_grafica.Visualizador_Rutas_GUI.visualizador_de_rutas import VisualizadorRutas
from intfz_grafica.Visualizador_Grupos_GUI.visualizador_grupos import VisualizadorEquipos

class Ventana_principal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Panel de Administración")

        # Definir colores
        self.color_primary = "#2ECC71"      # Verde principal
        self.color_secondary = "#27AE60"    # Verde secundario
        self.color_accent = "#1E8449"       # Verde oscuro para acentos
        self.color_bg = "#F5F5F5"           # Fondo gris muy claro
        self.color_text = "#2C3E50"         # Texto oscuro
        self.color_white = "#FFFFFF"        # Blanco puro

        # Crear fuentes personalizadas
        self.font_title = font.Font(family="Helvetica", size=20, weight="bold")
        self.font_button = font.Font(family="Helvetica", size=12, weight="bold")
        self.font_normal = font.Font(family="Helvetica", size=11)

        # Configurar ventana a pantalla completa
        self.ventana.geometry("1000x600")
        self.ventana.configure(bg=self.color_bg)

        # Main container
        self.main_container = tk.Frame(self.ventana, bg=self.color_bg)
        self.main_container.pack(expand=True, fill='both', padx=50, pady=20)

        # Header
        header_frame = tk.Frame(self.main_container, bg=self.color_primary, pady=20)
        header_frame.pack(fill='x', pady=(0, 20))
        tk.Label(header_frame,
                 text="Panel de Administración",
                 font=self.font_title,
                 bg=self.color_primary,
                 fg=self.color_white).pack()

        # Buttons frame
        buttons_frame = tk.Frame(self.main_container, bg=self.color_white, 
                               bd=1, relief="solid", padx=30, pady=30)
        buttons_frame.pack(expand=True)

        botones = [
            ("Registrar empleado", self.registrar_empleado),
            ("Formar grupo", self.formar_grupo),
            ("Eliminar empleado", self.eliminar_empleado),
            ("Registrar nuevo vehículo", self.registrar_vehiculo),
            ("Asignar ruta", self.asignar_ruta),
            ("Registrar estado del vehículo", self.abrir_estado_vehiculo),
            ("Visualizar empleados", self.vizualizar_empleados),
            ("Visualizar vehículos", self.visualizador_vehiculos),
            ("Visualizar rutas", self.visualizador_rutas),
            ("Visualizar grupos", self.visualizador_grupos),
            ("Añadir administrador", self.añadir_admin),
            ("Cerrar", self.cerrar)
        ]

        # Create buttons in a grid layout (3 columns)
        for i, (texto, comando) in enumerate(botones):
            btn = tk.Button(buttons_frame,
                          text=texto,
                          font=self.font_button,
                          bg=self.color_primary if texto != "Cerrar" else self.color_accent,
                          fg=self.color_white,
                          width=25,
                          height=2,
                          command=comando,
                          activebackground=self.color_secondary,
                          activeforeground=self.color_white,
                          relief="flat",
                          bd=0,
                          cursor="hand2")
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="ew")

        # Configure grid weights for even spacing
        for col in range(3):
            buttons_frame.grid_columnconfigure(col, weight=1)

        # Footer with copyright and help button
        self.create_footer()

        self.ventana.mainloop()

    def create_footer(self):
        """Crea el pie de página con copyright y botón de ayuda."""
        footer_frame = tk.Frame(self.main_container, bg=self.color_accent, height=30)
        footer_frame.pack(fill='x', pady=(15, 0))

        # Texto de copyright
        copyright_label = tk.Label(footer_frame,
                                  text="© 2025 Sistema de Gestión de Rutas - v1.0",
                                  bg=self.color_accent,
                                  fg=self.color_white,
                                  font=("Helvetica", 8))
        copyright_label.pack(side='left', padx=10, pady=5)

        # Botón de ayuda
        help_button = tk.Button(footer_frame,
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
        help_window = tk.Toplevel(self.ventana)
        help_window.title("Ayuda")
        help_window.geometry("400x350")
        help_window.configure(bg=self.color_white)
        help_window.transient(self.ventana)
        help_window.grab_set()
        
        # Help content frame
        content_frame = tk.Frame(help_window, bg=self.color_white)
        content_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        tk.Label(content_frame,
                text="Guía Rápida",
                font=self.font_button,
                bg=self.color_white,
                fg=self.color_text).pack(pady=(0, 10))
        
        help_text = """Bienvenido al Panel de Administración:
- Registrar empleado: Añade nuevos empleados al sistema
- Formar grupo: Crea grupos de trabajo
- Eliminar empleado: Remueve empleados existentes
- Registrar vehículo: Añade nuevos vehículos
- Asignar ruta: Asocia grupos a rutas
- Estado del vehículo: Actualiza el estado de vehículos
- Visualizar empleados: Muestra todos los empleados
- Visualizar vehículos: Muestra todos los vehículos
- Cerrar: Sale del sistema"""
        
        tk.Label(content_frame,
                text=help_text,
                font=self.font_normal,
                bg=self.color_white,
                fg=self.color_text,
                justify="left",
                wraplength=380).pack(pady=10)
        
        # Close button
        tk.Button(content_frame,
                 text="Cerrar",
                 font=self.font_normal,
                 bg=self.color_accent,
                 fg=self.color_white,
                 command=help_window.destroy,
                 activebackground=self.color_secondary,
                 relief="flat",
                 padx=10,
                 pady=5).pack(pady=(10, 0))

    def registrar_empleado(self):
        self.ventana.withdraw()
        Registrar_empleado_GUI()

    def formar_grupo(self):
        self.ventana.withdraw()
        Formar_Grupo_GUI()

    def eliminar_empleado(self):
        self.ventana.withdraw()
        Eliminar_empleado_GUI()

    def registrar_vehiculo(self):
        self.ventana.withdraw()
        RegistrarvehiculoGUI()

    def asignar_ruta(self):
        self.ventana.withdraw()
        GestorGruposRutasGUI()

    def abrir_estado_vehiculo(self):
        self.ventana.withdraw()
        EstadoVehiculo()

    def vizualizar_empleados(self):
        self.ventana.withdraw()
        VisualizadorEmpleados.iniciar_aplicacion()

    def visualizador_vehiculos(self):
        self.ventana.withdraw()
        VisualizadorVehiculos.iniciar_aplicacion()

    def añadir_admin(self):
        self.ventana.withdraw()
        Añadir_admin()

    def visualizador_rutas(self):
        self.ventana.withdraw()
        VisualizadorRutas.iniciar_aplicacion()
    
    def visualizador_grupos(self):
        self.ventana.withdraw()
        VisualizadorEquipos.iniciar_aplicacion()

    def cerrar(self):
        respuesta = messagebox.askyesno(
            "Confirmar cierre",
            "¿Está seguro que desea salir del sistema?"
        )
        if respuesta:
            self.ventana.destroy()
"""
if __name__ == "__main__":
    Ventana_principal()"""