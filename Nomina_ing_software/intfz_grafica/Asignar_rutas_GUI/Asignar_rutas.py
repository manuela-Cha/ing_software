from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class GestorGruposRutas:
    def __init__(self):
        self.archivo_grupos = "Nomina_ing_software/archivos_de_texto/Grupos.txt"
        self.archivo_rutas = "Nomina_ing_software/archivos_de_texto/Rutas.txt"

    def verificar_grupos(self):
        try:
            with open(self.archivo_grupos, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read().strip()
                if not contenido:
                    return False
                return True
        except FileNotFoundError:
            return False

    def verificar_rutas_disponibles(self):
        try:
            with open(self.archivo_rutas, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    if "Por_cubrir" in linea:
                        return True
                return False
        except FileNotFoundError:
            return False

    def verificar_estado_sistema(self):
        hay_grupos = self.verificar_grupos()
        if not hay_grupos:
            return "No hay grupos creados."

        grupos_disponibles = self.obtener_grupos()
        if not grupos_disponibles:
            return "No hay grupos disponibles."

        hay_rutas_disponibles = self.verificar_rutas_disponibles()
        if not hay_rutas_disponibles:
            return "Todas las rutas están cubiertas."
        
        return "Hay grupos y rutas disponibles."

    def obtener_grupos(self):
        grupos = []
        try:
            with open(self.archivo_grupos, 'r', encoding='utf-8') as archivo:
                grupo_actual = []
                es_disponible = False
                
                for linea in archivo:
                    linea_strip = linea.strip()
                    if linea_strip == "-" * 50:
                        if grupo_actual and es_disponible:
                            grupos.append('\n'.join(grupo_actual))
                        grupo_actual = []
                        es_disponible = False
                    else:
                        grupo_actual.append(linea_strip)
                        if linea_strip == "Estado: Disponible":
                            es_disponible = True
                
                if grupo_actual and es_disponible:
                    grupos.append('\n'.join(grupo_actual))
        except FileNotFoundError:
            return []
        return grupos

    def obtener_rutas(self):
        rutas = []
        try:
            with open(self.archivo_rutas, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    partes = linea.strip().split()
                    nombre_ruta = partes[0]
                    estado = partes[1]
                    equipo = ' '.join(partes[2:]) if len(partes) > 2 else '_'
                    rutas.append((nombre_ruta, estado, equipo))
        except FileNotFoundError:
            return []
        return rutas

    def obtener_integrantes_grupo(self, grupo_texto):
        integrantes = []
        for linea in grupo_texto.split('\n'):
            if '(CC:' in linea and ')' in linea:
                integrantes.append(linea.strip())
        return integrantes

    def grupo_ya_asignado(self, grupo_texto):
        integrantes = self.obtener_integrantes_grupo(grupo_texto)
        if not integrantes:
            return False
        
        try:
            with open(self.archivo_rutas, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    if "Cubierta" in linea:
                        partes = linea.strip().split()
                        equipo = ' '.join(partes[2:]) if len(partes) > 2 else ''
                        for integrante in integrantes:
                            if integrante in equipo:
                                return True
        except FileNotFoundError:
            return False
        return False
    
    def actualizar_estado_grupo(self, grupo_texto, nuevo_estado):
        """Actualiza el estado de un grupo en el archivo de grupos."""
        try:
            # Identificar al grupo por algún atributo único
            grupo_lineas = grupo_texto.split('\n')
            grupo_identificadores = []
            
            # Recopilar los identificadores del grupo (nombres e IDs de miembros)
            for linea in grupo_lineas:
                if '(CC:' in linea and ')' in linea:
                    grupo_identificadores.append(linea.strip())
            
            if not grupo_identificadores:
                raise ValueError("No se pudieron encontrar identificadores para el grupo")
            
            # Leer el archivo completo
            with open(self.archivo_grupos, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()
            
            # Escribir el archivo con el estado actualizado
            with open(self.archivo_grupos, 'w', encoding='utf-8') as archivo:
                grupo_encontrado = False
                dentro_de_grupo = False
                
                for linea in lineas:
                    linea_strip = linea.strip()
                    
                    # Si encontramos un separador, podemos resetear las banderas
                    if linea_strip == "-" * 50:
                        dentro_de_grupo = False
                        grupo_encontrado = False
                        archivo.write(linea)
                        continue
                    
                    # Si estamos en el grupo correcto y es la línea de estado, actualizarla
                    if grupo_encontrado and linea_strip.startswith("Estado:"):
                        archivo.write(f"Estado: {nuevo_estado}\n")
                        continue
                    
                    # Verificar si esta línea contiene un identificador del grupo
                    if not grupo_encontrado:
                        for identificador in grupo_identificadores:
                            if identificador in linea_strip:
                                dentro_de_grupo = True
                                break
                    
                    # Si estamos dentro del grupo y encontramos "Vehiculo asignado:", 
                    # entonces el estado vendrá después
                    if dentro_de_grupo and "Vehiculo asignado:" in linea_strip:
                        grupo_encontrado = True
                    
                    # En cualquier otro caso, escribir la línea original
                    archivo.write(linea)
            
            return True
        except Exception as e:
            raise Exception(f"Error al actualizar el estado del grupo: {str(e)}")

    def asignar_grupo_a_ruta(self, nombre_ruta, grupo_texto):
        try:
            if self.grupo_ya_asignado(grupo_texto):
                raise ValueError("Este grupo ya está asignado a otra ruta.")

            integrantes = self.obtener_integrantes_grupo(grupo_texto)
            if not integrantes:
                raise ValueError("No se encontraron integrantes en el grupo seleccionado")

            integrantes_str = "-".join(integrantes)
            with open(self.archivo_rutas, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()

            with open(self.archivo_rutas, 'w', encoding='utf-8') as archivo:
                for linea in lineas:
                    if linea.startswith(nombre_ruta):
                        nueva_linea = f"{nombre_ruta} Cubierta {integrantes_str}\n"
                        archivo.write(nueva_linea)
                    else:
                        archivo.write(linea)
            
            # Actualizar el estado del grupo a Ocupado
            self.actualizar_estado_grupo(grupo_texto, "Ocupado")

            return True
        except Exception as e:
            raise Exception(f"Error al asignar grupo a ruta: {str(e)}")

from tkinter import Tk, Frame, Label, Button, LabelFrame, Listbox, END, messagebox, font

class GestorGruposRutasGUI:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Gestión de Grupos y Rutas")
        self.ventana.geometry("1000x600")
        self.gestor = GestorGruposRutas()
        
        # Definir colores
        self.color_primary = "#2ECC71"      # Verde principal
        self.color_secondary = "#27AE60"    # Verde secundario
        self.color_accent = "#1E8449"       # Verde oscuro para acentos
        self.color_bg = "#F5F5F5"           # Fondo gris muy claro
        self.color_text = "#2C3E50"         # Texto oscuro
        self.color_white = "#FFFFFF"        # Blanco puro
        
        # Configurar el color de fondo de la ventana principal
        self.ventana.configure(bg=self.color_bg)
        
        # Crear fuentes personalizadas
        self.font_title = font.Font(family="Helvetica", size=16, weight="bold")
        self.font_subtitle = font.Font(family="Helvetica", size=12, weight="bold")
        self.font_button = font.Font(family="Helvetica", size=10, weight="bold")
        self.font_normal = font.Font(family="Helvetica", size=10)
        
        # Frame superior con título y estado
        frame_superior = Frame(self.ventana, pady=20, bg=self.color_bg)
        frame_superior.pack(fill='x')
        
        Label(frame_superior, text="Estado del Sistema", font=self.font_title, 
              bg=self.color_bg, fg=self.color_text).pack()
        
        self.label_estado = Label(frame_superior, text="", font=self.font_subtitle,
                                  bg=self.color_bg)
        self.label_estado.pack(pady=10)
        
        # Frame principal que contiene las listas
        frame_principal = Frame(self.ventana, bg=self.color_bg)
        frame_principal.pack(expand=True, fill='both', padx=20)
        
        # Frame para grupos
        frame_grupos = LabelFrame(frame_principal, text="Grupos Disponibles", 
                                 padx=10, pady=10, font=self.font_subtitle,
                                 bg=self.color_bg, fg=self.color_text)
        frame_grupos.pack(side="left", expand=True, fill='both', padx=(0,10))
        
        self.lista_grupos = Listbox(frame_grupos, width=50, height=15, exportselection=0,
                                   font=self.font_normal, bg=self.color_white, 
                                   fg=self.color_text, selectbackground=self.color_primary)
        self.lista_grupos.pack(expand=True, fill='both')
        
        # Frame para botón de asignación
        frame_asignacion = Frame(frame_principal, bg=self.color_bg)
        frame_asignacion.pack(side="left", padx=10)
        
        # Botón de asignar con el nuevo estilo
        self.boton_asignar = Button(frame_asignacion, text="Asignar >>", 
                                  command=self.asignar_grupo_ruta, width=15,
                                  font=self.font_button, bg=self.color_primary, 
                                  fg=self.color_white, activebackground=self.color_secondary)
        self.boton_asignar.pack(pady=10)
        
        # Frame para rutas
        frame_rutas = LabelFrame(frame_principal, text="Rutas", padx=10, pady=10,
                               font=self.font_subtitle, bg=self.color_bg, 
                               fg=self.color_text)
        frame_rutas.pack(side="left", expand=True, fill='both')
        
        self.lista_rutas = Listbox(frame_rutas, width=50, height=15, exportselection=0,
                                 font=self.font_normal, bg=self.color_white, 
                                 fg=self.color_text, selectbackground=self.color_primary)
        self.lista_rutas.pack(expand=True, fill='both')
        
        # Frame para botones inferiores
        frame_botones = Frame(self.ventana, pady=20, bg=self.color_bg)
        frame_botones.pack()
        
        # Botones con el nuevo estilo
        Button(frame_botones, text="Actualizar Todo", command=self.actualizar_todo, 
              width=15, font=self.font_button, bg=self.color_primary, 
              fg=self.color_white, activebackground=self.color_secondary).pack(side="left", padx=5)
        
        Button(frame_botones, text="Salir", command=self.salir, width=15,
              font=self.font_button, bg=self.color_accent, 
              fg=self.color_white, activebackground=self.color_secondary).pack(side="left", padx=5)
        
        self.grupos_dict = {}
        self.rutas_dict = {}
        
        self.actualizar_todo()
        
        self.ventana.mainloop()

    def salir(self):
        self.ventana.destroy()
        from intfz_grafica.Ventana_Principal_GUI.ventana_principal import Ventana_principal
        Ventana_principal()
    
    def actualizar_todo(self):
        self.actualizar_estado()
        self.mostrar_grupos()
        self.mostrar_rutas()
    
    def actualizar_estado(self):
        estado = self.gestor.verificar_estado_sistema()
        self.label_estado.config(text=estado)
        
        if "No hay grupos creados" in estado:
            self.label_estado.config(fg='red')
            self.boton_asignar.config(state='disabled')
        elif "No hay grupos disponibles" in estado:
            self.label_estado.config(fg='red')
            self.boton_asignar.config(state='disabled')
        elif "Todas las rutas están cubiertas" in estado:
            self.label_estado.config(fg='orange')
            self.boton_asignar.config(state='disabled')
        else:
            self.label_estado.config(fg=self.color_accent)
            self.boton_asignar.config(state='normal')
    
    def mostrar_grupos(self):
        self.lista_grupos.delete(0, END)
        self.grupos_dict.clear()
        grupos = self.gestor.obtener_grupos()
        
        if not grupos:
            self.lista_grupos.insert(END, "No hay grupos disponibles")
            return
            
        for i, grupo in enumerate(grupos):
            fecha = "Sin fecha"
            for linea in grupo.split('\n'):
                if "GRUPO CREADO EN FECHA:" in linea:
                    fecha = linea.split(": ")[1]
                    break
            
            display_text = f"Grupo {i+1} (Creado: {fecha})"
            self.lista_grupos.insert(END, display_text)
            self.grupos_dict[display_text] = grupo
    
    def mostrar_rutas(self):
        self.lista_rutas.delete(0, END)
        self.rutas_dict.clear()
        rutas = self.gestor.obtener_rutas()
        
        if not rutas:
            self.lista_rutas.insert(END, "No hay rutas registradas")
            return
            
        for nombre, estado, equipo in rutas:
            if estado == "Por_cubrir":
                display_text = f"{nombre} ({estado})"
                self.lista_rutas.insert(END, display_text)
                self.rutas_dict[display_text] = nombre
    
    def asignar_grupo_ruta(self):
        grupo_sel = self.lista_grupos.curselection()
        ruta_sel = self.lista_rutas.curselection()
        
        if not grupo_sel or not ruta_sel:
            messagebox.showwarning("Selección requerida", "Por favor, seleccione un grupo y una ruta")
            return
        
        grupo_texto = self.grupos_dict[self.lista_grupos.get(grupo_sel[0])]
        ruta_nombre = self.rutas_dict[self.lista_rutas.get(ruta_sel[0])]
        
        try:
            self.gestor.asignar_grupo_a_ruta(ruta_nombre, grupo_texto)
            messagebox.showinfo("Éxito", "Grupo asignado correctamente a la ruta")
            self.actualizar_todo()
        except Exception as e:
            messagebox.showerror("Error", str(e))