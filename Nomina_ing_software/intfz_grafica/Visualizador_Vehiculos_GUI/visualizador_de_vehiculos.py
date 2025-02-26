import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, font
import os
from datetime import datetime

class VisualizadorVehiculos:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Visualización de Vehiculos")
        self.root.geometry("800x600")
        self.root.minsize(700, 500)  # Tamaño mínimo para mejor experiencia
        
        # Definir colores
        self.color_primary = "#2ECC71"      # Verde principal
        self.color_secondary = "#27AE60"    # Verde secundario
        self.color_accent = "#1E8449"       # Verde oscuro para acentos
        self.color_bg = "#F5F5F5"           # Fondo gris muy claro
        self.color_text = "#2C3E50"         # Texto oscuro
        self.color_white = "#FFFFFF"        # Blanco puro
        
        # Configurar el color de fondo de la ventana principal
        self.root.configure(bg=self.color_bg)
        
        # Crear fuentes personalizadas
        self.font_title = font.Font(family="Helvetica", size=16, weight="bold")
        self.font_subtitle = font.Font(family="Helvetica", size=12, weight="bold")
        self.font_button = font.Font(family="Helvetica", size=10, weight="bold")
        self.font_normal = font.Font(family="Helvetica", size=10)
        
        # Crear marco principal con efecto de sombra
        self.main_container = tk.Frame(root, bg=self.color_bg)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header con logo y título
        self.create_header()
        
        # Panel principal con pestañas
        self.create_main_panel()
        
        # Footer con información
        self.create_footer()
        
        # Cargar datos inicialmente
        self.cargar_empleados()
    
    def create_header(self):
        """Crea el encabezado con logo y título."""
        header_frame = tk.Frame(self.main_container, bg=self.color_primary, height=80)
        header_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Crear efecto de gradiente en el header
        canvas = tk.Canvas(header_frame, height=80, bg=self.color_primary, 
                          highlightthickness=0)
        canvas.pack(fill=tk.X)
        
        # Logo ficticio
        canvas.create_oval(30, 15, 70, 55, fill=self.color_white, outline="")
        canvas.create_text(50, 35, text="SGR", fill=self.color_primary, 
                          font=self.font_subtitle)
        
        # Título
        canvas.create_text(400, 30, text="Visualizador de vehiculos", 
                          fill=self.color_white, font=self.font_title)
        
        # Fecha actual
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        canvas.create_text(700, 55, text=f"Fecha: {date_str}", 
                          fill=self.color_white, font=self.font_normal)
    
    def create_main_panel(self):
        """Crea el panel principal con pestañas."""
        # Marco para el contenido
        content_frame = tk.Frame(self.main_container, bg=self.color_white)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Crear pestañas
        tab_control = ttk.Notebook(content_frame)
        
        # Estilos para las pestañas
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background=self.color_bg, 
                       font=self.font_normal, padding=[10, 5])
        style.map('TNotebook.Tab', background=[('selected', self.color_primary)], 
                 foreground=[('selected', self.color_white)])
        
        # Pestaña de listado
        self.tab_listado = tk.Frame(tab_control, bg=self.color_white)
        tab_control.add(self.tab_listado, text="Listado de Vehiculos")
    
        
        # Mostrar las pestañas
        tab_control.pack(expand=1, fill="both")
        
        # Crear el contenido de la pestaña de listado
        self.create_listado_tab()
    
    def create_listado_tab(self):
        """Crea el contenido de la pestaña de listado."""
        # Panel de búsqueda
        search_frame = tk.Frame(self.tab_listado, bg=self.color_white)
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Etiqueta de búsqueda
        search_label = tk.Label(search_frame, text="Buscar: ", 
                               font=self.font_normal, bg=self.color_white)
        search_label.pack(side=tk.LEFT, padx=(0, 5))
        
        # Campo de búsqueda
        self.search_entry = tk.Entry(search_frame, width=30, 
                                   font=self.font_normal)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        
        # Botón de búsqueda
        search_button = tk.Button(search_frame, text="Buscar", 
                                 bg=self.color_secondary, fg=self.color_white,
                                 font=self.font_normal, bd=0, padx=10,
                                 activebackground=self.color_accent,
                                 activeforeground=self.color_white,
                                 command=self.buscar_empleado)
        search_button.pack(side=tk.LEFT, padx=5)
        
        # Panel para la tabla
        table_frame = tk.Frame(self.tab_listado, bg=self.color_white)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Configurar estilo del Treeview
        style = ttk.Style()
        style.configure("Treeview", 
                       background=self.color_white,
                       foreground=self.color_text,
                       rowheight=30,
                       fieldbackground=self.color_white,
                       font=self.font_normal)
        
        style.configure("Treeview.Heading", 
                       background=self.color_accent,
                       foreground=self.color_white,
                       font=self.font_button)
        
        style.map('Treeview', 
                 background=[('selected', self.color_primary)],
                 foreground=[('selected', self.color_white)])
        
        # Scrollbar
        table_scroll = ttk.Scrollbar(table_frame)
        table_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Tabla de vehiculos
        self.tree = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set)
        self.tree["columns"] = ("ID", "Estado")
        
        # Configurar columnas
        self.tree.column("#0", width=120, stretch=tk.NO)
        self.tree.column("ID", width=180, anchor=tk.W)
        self.tree.column("Estado", width=180, anchor=tk.W)
        
        # Configurar encabezados
        self.tree.heading("#0", text="Vehiculo número")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Estado", text="Estado")
        
        # Empacar la tabla
        self.tree.pack(fill=tk.BOTH, expand=True)
        table_scroll.config(command=self.tree.yview)
        
        # Panel de botones
        button_frame = tk.Frame(self.tab_listado, bg=self.color_white)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Botones con estilo moderno
        refresh_button = tk.Button(button_frame, text="Actualizar Lista", 
                                  bg=self.color_secondary, fg=self.color_white,
                                  font=self.font_button, bd=0, padx=15, pady=8,
                                  activebackground=self.color_accent,
                                  activeforeground=self.color_white,
                                  command=self.cargar_empleados)
        refresh_button.pack(side=tk.LEFT, padx=5)
        
        export_button = tk.Button(button_frame, text="Exportar", 
                                 bg=self.color_secondary, fg=self.color_white,
                                 font=self.font_button, bd=0, padx=15, pady=8,
                                 activebackground=self.color_accent,
                                 activeforeground=self.color_white)
        export_button.pack(side=tk.LEFT, padx=5)
    
    def create_footer(self):
        """Crea el pie de página."""
        footer_frame = tk.Frame(self.main_container, bg=self.color_accent, height=30)
        footer_frame.pack(fill=tk.X, pady=(15, 0))
        
        # Texto de copyright
        copyright_label = tk.Label(footer_frame, text="© 2025 Sistema de Gestión de Rutas - v1.0", 
                                  bg=self.color_accent, fg=self.color_white,
                                  font=("Helvetica", 8))
        copyright_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Botón de ayuda
        help_button = tk.Button(footer_frame, text="?", bg=self.color_accent, 
                               fg=self.color_white, bd=0, font=("Helvetica", 10, "bold"),
                               activebackground=self.color_secondary,
                               command=self.mostrar_ayuda)
        help_button.pack(side=tk.RIGHT, padx=10, pady=5)
    
    def cargar_empleados(self):
        """Carga los empleados desde el archivo y los muestra en la tabla."""
        # Limpiar la tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            # Rutas posibles del archivo
            rutas = [
                'Nomina_ing_software/archivos_de_texto/Vehiculos.txt',
                'Vehiculos.txt'
            ]
            
            # Verificar las rutas
            ruta_encontrada = None
            for ruta in rutas:
                if os.path.exists(ruta):
                    ruta_encontrada = ruta
                    break
                    
            if not ruta_encontrada:
                messagebox.showerror("Error", "No se encontró el archivo Vehiculos.txt")
                return
            
            # Leer el archivo
            with open(ruta_encontrada, 'r') as archivo:
                lineas = archivo.readlines()
            
            # Contador para el ID
            contador = 1
            
            # Insertar cada línea en la tabla
            for linea in lineas:
                # Ignorar líneas vacías
                if linea.strip() == "":
                    continue
                    
                # Dividir la línea
                datos = linea.strip().split(" ")
                
                # Asegurarse de que hay al menos 3 elementos
                if len(datos) >= 2:
                    Id = datos[0]
                    estado = datos[1]
                    
                    # Insertar con tags alternados para efectos visuales
                    tag = "even" if contador % 2 == 0 else "odd"
                    self.tree.insert("", tk.END, text=f"{contador}", 
                                    values=(Id, estado), tags=(tag,))
                else:
                    # Si el formato es incorrecto
                    tag = "even" if contador % 2 == 0 else "odd"
                    self.tree.insert("", tk.END, text=f"{contador}", 
                                    values=(linea.strip(), "", ""), tags=(tag,))
                    
                contador += 1
            
            # Configurar colores de filas alternadas
            self.tree.tag_configure("odd", background=self.color_white)
            self.tree.tag_configure("even", background="#F0F9F2")  # Verde muy claro
            
            # Mostrar mensaje si no hay empleados
            if contador == 1:
                self.tree.insert("", tk.END, text="", 
                               values=("No hay vehiculos registrados", "", ""))
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar vehiculos: {str(e)}")
    
    def buscar_empleado(self):
        """Filtra los empleados según el texto de búsqueda."""
        busqueda = self.search_entry.get().strip().lower()
        
        # Si no hay texto de búsqueda, mostrar todos
        if not busqueda:
            self.cargar_empleados()
            return
        
        # Limpiar la tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        try:
            # Rutas posibles del archivo
            rutas = [
                'Nomina_ing_software/archivos_de_texto/Vehiculos.txt',
                'Vehiculos.txt'
            ]
            
            # Verificar las rutas
            ruta_encontrada = None
            for ruta in rutas:
                if os.path.exists(ruta):
                    ruta_encontrada = ruta
                    break
                    
            if not ruta_encontrada:
                messagebox.showerror("Error", "No se encontró el archivo Vehiculos.txt")
                return
            
            # Leer el archivo
            with open(ruta_encontrada, 'r') as archivo:
                lineas = archivo.readlines()
            
            # Contador para el ID y para resultados encontrados
            contador = 1
            encontrados = 0
            
            # Buscar e insertar coincidencias
            for linea in lineas:
                # Ignorar líneas vacías
                if linea.strip() == "":
                    continue
                    
                # Si la línea contiene el texto de búsqueda
                if busqueda in linea.lower():
                    # Dividir la línea
                    datos = linea.strip().split(" ")
                    
                    # Asegurarse de que hay al menos 3 elementos
                    if len(datos) >= 2:
                        nombre = datos[0]
                        apellido = datos[1]
                        cedula = datos[2]
                        
                        # Insertar con tags alternados para efectos visuales
                        tag = "even" if contador % 2 == 0 else "odd"
                        self.tree.insert("", tk.END, text=f"{contador}", 
                                        values=(nombre, apellido, cedula), tags=(tag,))
                    else:
                        # Si el formato es incorrecto
                        tag = "even" if contador % 2 == 0 else "odd"
                        self.tree.insert("", tk.END, text=f"{contador}", 
                                        values=(linea.strip(), "", ""), tags=(tag,))
                        
                    contador += 1
                    encontrados += 1
            
            # Configurar colores de filas alternadas
            self.tree.tag_configure("odd", background=self.color_white)
            self.tree.tag_configure("even", background="#F0F9F2")  # Verde muy claro
            
            # Mostrar mensaje si no hay resultados
            if encontrados == 0:
                self.tree.insert("", tk.END, text="", 
                               values=("No se encontraron coincidencias", "", ""))
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar el vehiculo: {str(e)}")
    
    def mostrar_ayuda(self):
        """Muestra una ventana de ayuda."""
        help_window = tk.Toplevel(self.root)
        help_window.title("Ayuda")
        help_window.geometry("400x300")
        help_window.configure(bg=self.color_white)
        
        # Título
        titulo = tk.Label(help_window, text="Ayuda del Sistema", 
                         font=self.font_title, bg=self.color_white)
        titulo.pack(pady=10)
        
        # Contenido
        contenido = tk.Label(help_window, text=
                           "Este sistema permite visualizar el listado de vehiculos.\n\n"
                           "- Para actualizar la lista: haga clic en 'Actualizar Lista'\n"
                           "- Para buscar: escriba texto en el campo y presione 'Buscar'\n"
                           "- Las filas se muestran con colores alternados para mejor lectura\n\n"
                           "El archivo debe tener el formato:\n"
                           "id estado",
                           justify=tk.LEFT, bg=self.color_white, fg=self.color_text)
        contenido.pack(padx=20, pady=10, fill=tk.X)
        
        # Botón de cerrar
        cerrar = tk.Button(help_window, text="Cerrar", 
                          bg=self.color_secondary, fg=self.color_white,
                          font=self.font_button, bd=0, padx=15, pady=5,
                          activebackground=self.color_accent,
                          activeforeground=self.color_white,
                          command=help_window.destroy)
        cerrar.pack(pady=20)

    # Función para iniciar la aplicación
    def iniciar_aplicacion():
        root = tk.Tk()
        app = VisualizadorVehiculos(root)
        root.mainloop()

# Si este archivo se ejecuta directamente
if __name__ == "__main__":
    VisualizadorVehiculos.iniciar_aplicacion()