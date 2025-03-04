import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, font
import os
from datetime import datetime

class VisualizadorEquipos:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Visualización de Equipos")
        self.root.geometry("900x650")
        self.root.minsize(800, 650)  # Tamaño mínimo para mejor experiencia
        
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
        self.cargar_equipos()
    
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
        canvas.create_text(400, 30, text="Visualización de Equipos", 
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
        tab_control.add(self.tab_listado, text="Listado de Equipos")
        
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
                                 command=self.buscar_equipo)
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
        
        # Tabla de equipos
        self.tree = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set)
        self.tree["columns"] = ("Fecha", "Integrantes", "Vehiculo", "Estado")
        
        # Configurar columnas
        self.tree.column("#0", width=60, stretch=tk.NO)
        self.tree.column("Fecha", width=100, anchor=tk.CENTER)
        self.tree.column("Integrantes", width=350, anchor=tk.W)
        self.tree.column("Vehiculo", width=100, anchor=tk.CENTER)
        self.tree.column("Estado", width=100, anchor=tk.CENTER)
        
        # Configurar encabezados
        self.tree.heading("#0", text="ID")
        self.tree.heading("Fecha", text="Fecha Creación")
        self.tree.heading("Integrantes", text="Integrantes")
        self.tree.heading("Vehiculo", text="Vehículo")
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
                                  command=self.cargar_equipos)
        refresh_button.pack(side=tk.LEFT, padx=5)

        # Botón para ver detalles
        details_button = tk.Button(button_frame, text="Ver Detalles", 
                                bg=self.color_secondary, fg=self.color_white,
                                font=self.font_button, bd=0, padx=15, pady=8,
                                activebackground=self.color_accent,
                                activeforeground=self.color_white,
                                command=self.ver_detalles)
        details_button.pack(side=tk.LEFT, padx=5)

        # Botón para salir
        out_button = tk.Button(button_frame, text="Salir", 
                              bg=self.color_secondary, fg=self.color_white,
                              font=self.font_button, bd=0, padx=10, pady=8,
                              activebackground=self.color_accent,
                              activeforeground=self.color_white,
                              command=self.salir)
        out_button.pack(side=tk.LEFT, padx=20)

    def salir(self):
        self.root.destroy()
        from intfz_grafica.Ventana_Principal_GUI.ventana_principal import Ventana_principal
        Ventana_principal()
    
    def ver_detalles(self):
        """Muestra detalles del equipo seleccionado."""
        # Obtener el ítem seleccionado
        selected_item = self.tree.selection()
        
        if not selected_item:
            messagebox.showinfo("Información", "Por favor seleccione un equipo para ver sus detalles.")
            return
            
        # Obtener valores del ítem seleccionado
        item_id = self.tree.item(selected_item[0], "text")
        values = self.tree.item(selected_item[0], "values")
        
        # Crear ventana de detalles
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Detalles del Equipo #{item_id}")
        details_window.geometry("600x400")
        details_window.configure(bg=self.color_white)
        
        # Contenedor principal
        main_frame = tk.Frame(details_window, bg=self.color_white, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = tk.Label(main_frame, text=f"Información del Equipo #{item_id}", 
                              font=self.font_title, bg=self.color_white, fg=self.color_primary)
        title_label.pack(pady=(0, 20))
        
        # Información del equipo
        info_frame = tk.Frame(main_frame, bg=self.color_white)
        info_frame.pack(fill=tk.X)
        
        # Fecha
        fecha_label = tk.Label(info_frame, text="Fecha de Creación:", 
                              font=self.font_subtitle, bg=self.color_white, fg=self.color_text)
        fecha_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        
        fecha_valor = tk.Label(info_frame, text=values[0], 
                              font=self.font_normal, bg=self.color_white, fg=self.color_text)
        fecha_valor.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        # Vehículo
        vehiculo_label = tk.Label(info_frame, text="Vehículo Asignado:", 
                                 font=self.font_subtitle, bg=self.color_white, fg=self.color_text)
        vehiculo_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        vehiculo_valor = tk.Label(info_frame, text=values[2], 
                                 font=self.font_normal, bg=self.color_white, fg=self.color_text)
        vehiculo_valor.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        
        # Estado
        estado_label = tk.Label(info_frame, text="Estado:", 
                               font=self.font_subtitle, bg=self.color_white, fg=self.color_text)
        estado_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        
        estado_valor = tk.Label(info_frame, text=values[3], 
                               font=self.font_normal, bg=self.color_white, 
                               fg="#27AE60" if values[3] == "Disponible" else "#E74C3C")
        estado_valor.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        
        # Integrantes
        integrantes_label = tk.Label(main_frame, text="Integrantes del Equipo:", 
                                    font=self.font_subtitle, bg=self.color_white, fg=self.color_text)
        integrantes_label.pack(anchor=tk.W, pady=(20, 10))
        
        # Frame para la lista de integrantes
        integrantes_frame = tk.Frame(main_frame, bg=self.color_white, bd=1, relief=tk.SOLID)
        integrantes_frame.pack(fill=tk.BOTH, expand=True)
        
        # Texto con los integrantes
        integrantes_text = tk.Text(integrantes_frame, font=self.font_normal, wrap=tk.WORD, 
                                  bg=self.color_white, bd=0)
        integrantes_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        integrantes_text.insert(tk.END, values[1].replace(", ", "\n"))
        integrantes_text.config(state=tk.DISABLED)
        
        # Botón de cerrar
        close_button = tk.Button(main_frame, text="Cerrar", 
                                bg=self.color_secondary, fg=self.color_white,
                                font=self.font_button, bd=0, padx=20, pady=8,
                                activebackground=self.color_accent,
                                activeforeground=self.color_white,
                                command=details_window.destroy)
        close_button.pack(pady=20)
    
    def create_footer(self):
        """Crea el pie de página."""
        footer_frame = tk.Frame(self.main_container, bg=self.color_accent, height=30)
        footer_frame.pack(fill=tk.X, pady=(15, 0))
        
        # Texto de copyright
        copyright_label = tk.Label(footer_frame, text="© 2025 Sistema de Gestión de rutas - v1.0", 
                                  bg=self.color_accent, fg=self.color_white,
                                  font=("Helvetica", 8))
        copyright_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Botón de ayuda
        help_button = tk.Button(footer_frame, text="?", bg=self.color_accent, 
                               fg=self.color_white, bd=0, font=("Helvetica", 10, "bold"),
                               activebackground=self.color_secondary,
                               command=self.mostrar_ayuda)
        help_button.pack(side=tk.RIGHT, padx=10, pady=5)
    
    def cargar_equipos(self):
        """Carga los equipos desde el archivo y los muestra en la tabla."""
        # Limpiar la tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            # Rutas posibles del archivo
            rutas = [
                'Nomina_ing_software/archivos_de_texto/Grupos.txt',
                'Grupos.txt'
            ]
            
            # Verificar las rutas
            ruta_encontrada = None
            for ruta in rutas:
                if os.path.exists(ruta):
                    ruta_encontrada = ruta
                    break
                    
            if not ruta_encontrada:
                messagebox.showerror("Error", "No se encontró el archivo Grupos.txt")
                return
            
            # Leer el archivo
            with open(ruta_encontrada, 'r') as archivo:
                contenido = archivo.read()
            
            # Dividir por la línea de separación
            grupos = contenido.split('--------------------------------------------------')
            
            # Contador para el ID
            contador = 1
            
            # Insertar cada grupo en la tabla
            for grupo in grupos:
                # Ignorar contenido vacío
                if grupo.strip() == "":
                    continue
                
                # Parsear información del grupo
                fecha = ""
                integrantes = []
                vehiculo = ""
                estado = ""
                
                lineas = grupo.strip().split('\n')
                for i, linea in enumerate(lineas):
                    if "GRUPO CREADO EN FECHA:" in linea:
                        fecha = linea.replace("GRUPO CREADO EN FECHA:", "").strip()
                    elif "Vehiculo asignado:" in linea:
                        vehiculo = linea.replace("Vehiculo asignado:", "").strip()
                    elif "Estado:" in linea:
                        estado = linea.replace("Estado:", "").strip()
                    elif linea.strip() == "Integrantes:":
                        # Recopilar integrantes hasta encontrar otra sección
                        j = i + 1
                        while j < len(lineas) and (lineas[j].startswith("- ") or lineas[j].strip() == ""):
                            if lineas[j].startswith("- "):
                                integrantes.append(lineas[j][2:])
                            j += 1
                
                # Formatear integrantes para mostrar
                integrantes_str = ", ".join(integrantes)
                
                # Insertar con tags alternados para efectos visuales
                tag = "even" if contador % 2 == 0 else "odd"
                self.tree.insert("", tk.END, text=f"{contador}", 
                                values=(fecha, integrantes_str, vehiculo, estado), tags=(tag,))
                
                contador += 1
            
            # Configurar colores de filas alternadas
            self.tree.tag_configure("odd", background=self.color_white)
            self.tree.tag_configure("even", background="#E8F8F5")  # Verde muy claro
            
            # Mostrar mensaje si no hay equipos
            if contador == 1:
                self.tree.insert("", tk.END, text="", 
                               values=("No hay equipos registrados", "", "", ""))
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar equipos: {str(e)}")
    
    def buscar_equipo(self):
        """Filtra los equipos según el texto de búsqueda."""
        busqueda = self.search_entry.get().strip().lower()
        
        # Si no hay texto de búsqueda, mostrar todos
        if not busqueda:
            self.cargar_equipos()
            return
        
        # Limpiar la tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        try:
            # Rutas posibles del archivo
            rutas = [
                'Nomina_ing_software/archivos_de_texto/Grupos.txt',
                'Grupos.txt'
            ]
            
            # Verificar las rutas
            ruta_encontrada = None
            for ruta in rutas:
                if os.path.exists(ruta):
                    ruta_encontrada = ruta
                    break
                    
            if not ruta_encontrada:
                messagebox.showerror("Error", "No se encontró el archivo Grupos.txt")
                return
            
            # Leer el archivo
            with open(ruta_encontrada, 'r') as archivo:
                contenido = archivo.read()
            
            # Dividir por la línea de separación
            grupos = contenido.split('--------------------------------------------------')
            
            # Contador para el ID y para resultados encontrados
            contador = 1
            encontrados = 0
            
            # Buscar e insertar coincidencias
            for grupo in grupos:
                # Ignorar contenido vacío
                if grupo.strip() == "":
                    continue
                
                # Si el grupo contiene el texto de búsqueda
                if busqueda in grupo.lower():
                    # Parsear información del grupo
                    fecha = ""
                    integrantes = []
                    vehiculo = ""
                    estado = ""
                    
                    lineas = grupo.strip().split('\n')
                    for i, linea in enumerate(lineas):
                        if "GRUPO CREADO EN FECHA:" in linea:
                            fecha = linea.replace("GRUPO CREADO EN FECHA:", "").strip()
                        elif "Vehiculo asignado:" in linea:
                            vehiculo = linea.replace("Vehiculo asignado:", "").strip()
                        elif "Estado:" in linea:
                            estado = linea.replace("Estado:", "").strip()
                        elif linea.strip() == "Integrantes:":
                            # Recopilar integrantes hasta encontrar otra sección
                            j = i + 1
                            while j < len(lineas) and (lineas[j].startswith("- ") or lineas[j].strip() == ""):
                                if lineas[j].startswith("- "):
                                    integrantes.append(lineas[j][2:])
                                j += 1
                    
                    # Formatear integrantes para mostrar
                    integrantes_str = ", ".join(integrantes)
                    
                    # Insertar con tags alternados para efectos visuales
                    tag = "even" if contador % 2 == 0 else "odd"
                    self.tree.insert("", tk.END, text=f"{contador}", 
                                    values=(fecha, integrantes_str, vehiculo, estado), tags=(tag,))
                    
                    contador += 1
                    encontrados += 1
            
            # Configurar colores de filas alternadas
            self.tree.tag_configure("odd", background=self.color_white)
            self.tree.tag_configure("even", background="#E8F8F5")  # Verde muy claro
            
            # Mostrar mensaje si no hay resultados
            if encontrados == 0:
                self.tree.insert("", tk.END, text="", 
                               values=("No se encontraron coincidencias", "", "", ""))
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar equipos: {str(e)}")
    
    def mostrar_ayuda(self):
        """Muestra una ventana de ayuda."""
        help_window = tk.Toplevel(self.root)
        help_window.title("Ayuda")
        help_window.geometry("450x350")
        help_window.configure(bg=self.color_white)
        
        # Título
        titulo = tk.Label(help_window, text="Ayuda del Sistema", 
                         font=self.font_title, bg=self.color_white)
        titulo.pack(pady=10)
        
        # Contenido
        contenido = tk.Label(help_window, text=
                           "Este sistema permite visualizar el listado de equipos.\n\n"
                           "- Para actualizar la lista: haga clic en 'Actualizar Lista'\n"
                           "- Para buscar: escriba texto en el campo y presione 'Buscar'\n"
                           "- Para ver detalles: seleccione un equipo y haga clic en 'Ver Detalles'\n"
                           "- Las filas se muestran con colores alternados para mejor lectura\n\n"
                           "El archivo debe tener el formato:\n"
                           "GRUPO CREADO EN FECHA: YYYY-MM-DD\n"
                           "Integrantes:\n"
                           "- nombre apellido (CC: ####)\n"
                           "Vehiculo asignado: ####\n"
                           "Estado: [Disponible/Ocupado]",
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
        app = VisualizadorEquipos(root)
        root.mainloop()

# Si este archivo se ejecuta directamente
"""if __name__ == "__main__":
    VisualizadorEquipos.iniciar_aplicacion()"""