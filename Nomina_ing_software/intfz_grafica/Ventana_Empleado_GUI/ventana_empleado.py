from tkinter import *
from tkinter import messagebox
from intfz_grafica.login.login import Login
import tkinter.font as font

class Ventana_Empleado_GUI(Tk):
    def __init__(self, cedula_empleado):
        super().__init__()
        self.cedula_empleado = cedula_empleado
        self.title("Portal del Empleado")
        self.geometry("700x550")  # Slightly larger window for better layout
        

        # Definir colores
        self.color_primary = "#2ECC71"      # Verde principal
        self.color_secondary = "#27AE60"    # Verde secundario
        self.color_accent = "#1E8449"       # Verde oscuro para acentos
        self.color_bg = "#F5F5F5"           # Fondo gris muy claro
        self.color_text = "#2C3E50"         # Texto oscuro
        self.color_white = "#FFFFFF"        # Blanco puro
        self.color_border = "#D5D8DC"       # Gris claro para bordes

        # Crear fuentes personalizadas
        self.font_title = font.Font(family="Helvetica", size=18, weight="bold")
        self.font_subtitle = font.Font(family="Helvetica", size=14, weight="bold")
        self.font_button = font.Font(family="Helvetica", size=11, weight="bold")
        self.font_normal = font.Font(family="Helvetica", size=11)
        self.font_small = font.Font(family="Helvetica", size=9)

        # Configurar el color de fondo de la ventana principal
        self.configure(bg=self.color_bg)
        
        # Main container frame
        self.main_frame = Frame(self, bg=self.color_bg, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill='both')

        # Header section
        self.header_frame = Frame(self.main_frame, bg=self.color_primary, pady=15, padx=20)
        self.header_frame.pack(fill='x')
        
        Label(self.header_frame,
              text="Portal del Empleado",
              font=self.font_title,
              bg=self.color_primary,
              fg=self.color_white).pack(side=LEFT)
        
        Label(self.header_frame,
              text="Bienvenido",
              font=self.font_small,
              bg=self.color_primary,
              fg=self.color_white).pack(side=RIGHT)

        # Info empleado section
        self.info_empleado = self.obtener_info_empleado()
        
        self.info_container = Frame(self.main_frame, bg=self.color_white, 
                                  bd=1, relief="solid", pady=15, padx=20)
        self.info_container.pack(fill='x', pady=(20, 10))
        
        Label(self.info_container,
              text="Información Personal",
              font=self.font_subtitle,
              bg=self.color_white,
              fg=self.color_text).pack(anchor='w', pady=(0, 10))
        
        info_frame = Frame(self.info_container, bg=self.color_white)
        info_frame.pack(fill='x')
        
        Label(info_frame,
              text=f"Nombre: {self.info_empleado['nombre']} {self.info_empleado['apellido']}",
              font=self.font_normal,
              bg=self.color_white,
              fg=self.color_text).pack(anchor='w', pady=2)
        Label(info_frame,
              text=f"Cédula: {self.cedula_empleado}",
              font=self.font_normal,
              bg=self.color_white,
              fg=self.color_text).pack(anchor='w', pady=2)
        Label(info_frame,
              text=f"Estado: {self.info_empleado['estado']}",
              font=self.font_normal,
              bg=self.color_white,
              fg=self.color_text).pack(anchor='w', pady=2)

        # Estado del grupo section
        self.estado_container = Frame(self.main_frame, bg=self.color_white,
                                    bd=1, relief="solid", pady=15, padx=20)
        self.estado_container.pack(fill='x', pady=10)
        
        Label(self.estado_container,
              text="Estado del Grupo",
              font=self.font_subtitle,
              bg=self.color_white,
              fg=self.color_text).pack(anchor='w', pady=(0, 10))
        
        self.estado_frame = Frame(self.estado_container, bg=self.color_white)
        self.estado_frame.pack(fill='x')
        
        self.verificar_estado_grupo()

        # Buttons section
        self.button_frame = Frame(self.main_frame, bg=self.color_bg)
        self.button_frame.pack(fill='x', pady=20)
        
        Button(self.button_frame,
               text="Actualizar Estado",
               command=self.verificar_estado_grupo,
               font=self.font_button,
               bg=self.color_primary,
               fg=self.color_white,
               activebackground=self.color_secondary,
               activeforeground=self.color_white,
               relief="flat",
               padx=15,
               pady=8,
               bd=0,
               cursor="hand2").pack(side=LEFT, padx=5)
        
        Button(self.button_frame,
               text="Cerrar Sesión",
               command=self.cerrar_sesion,
               font=self.font_button,
               bg=self.color_accent,
               fg=self.color_white,
               activebackground=self.color_secondary,
               activeforeground=self.color_white,
               relief="flat",
               padx=15,
               pady=8,
               bd=0,
               cursor="hand2").pack(side=RIGHT, padx=5)
        
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
              text="Ayuda - Portal del Empleado",
              font=self.font_subtitle,
              bg=self.color_white,
              fg=self.color_text).pack(pady=(0, 10))

        help_text = """Instrucciones:
- Información Personal: Muestra su nombre, cédula y estado.
- Estado del Grupo: Indica si está asignado a un grupo.
  - Si está en un grupo, verá los detalles y podrá confirmar el trabajo.
  - Si no, aparecerá "No asignado a ningún grupo".
- Actualizar Estado: Refresca la información del grupo.
- Confirmar Trabajo: Finaliza el trabajo y libera el grupo (si aplica).
- Cerrar Sesión: Regresa a la pantalla de inicio de sesión."""
        
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
               padx=15,
               pady=5).pack(pady=(10, 0))
    
    def obtener_info_empleado(self):
        try:
            with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" ")
                    if datos[2] == self.cedula_empleado:
                        return {'nombre': datos[0], 'apellido': datos[1], 'estado': datos[3]}
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer archivo de empleados: {str(e)}")
        return {'nombre': 'Desconocido', 'apellido': '', 'estado': 'Desconocido'}
    
    def verificar_estado_grupo(self):
        for widget in self.estado_frame.winfo_children():
            widget.destroy()
        
        self.esta_en_grupo = False
        self.info_grupo = []
        self.vehiculo_asignado = None
        
        try:
            with open('Nomina_ing_software/archivos_de_texto/Grupos.txt', 'r') as archivo:
                lineas = archivo.readlines()
                i = 0
                while i < len(lineas):
                    linea = lineas[i].strip()
                    if linea.startswith("GRUPO CREADO EN FECHA:"):
                        fecha = linea.split(": ")[1]
                        grupo_actual = []
                        grupo_inicio = i
                        i += 1
                        
                        grupo_temp = []
                        while i < len(lineas) and not lineas[i].strip().startswith("-" * 50):
                            grupo_temp.append(lineas[i].strip())
                            i += 1
                        
                        for linea_grupo in grupo_temp:
                            if "(CC:" in linea_grupo:
                                cedula_en_grupo = linea_grupo.split("(CC: ")[1].split(")")[0]
                                if cedula_en_grupo == self.cedula_empleado:
                                    self.esta_en_grupo = True
                                    grupo_actual.append(f"Fecha de creación: {fecha}")
                                    grupo_actual.extend(grupo_temp)
                                    self.info_grupo = grupo_actual
                                    
                                    for linea_vehiculo in grupo_temp:
                                        if linea_vehiculo.startswith("Vehiculo asignado:"):
                                            self.vehiculo_asignado = linea_vehiculo.split(": ")[1].strip()
                                    break
                        
                        if self.esta_en_grupo:
                            break
                            
                        if i < len(lineas) and lineas[i].strip().startswith("-" * 50):
                            i += 1
                    else:
                        i += 1
                        
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer archivo de grupos: {str(e)}")
            return
    
        self.mostrar_estado_grupo()

    def mostrar_estado_grupo(self):
        if self.esta_en_grupo:
            status_frame = Frame(self.estado_frame, bg=self.color_primary, pady=5, padx=10)
            status_frame.pack(fill='x', pady=(0, 10))
            
            Label(status_frame,
                  text="Asignado a un grupo",
                  font=self.font_subtitle,
                  bg=self.color_primary,
                  fg=self.color_white).pack()
            
            grupo_frame = Frame(self.estado_frame, bg=self.color_white)
            grupo_frame.pack(fill='x', pady=5)
            
            for info in self.info_grupo:
                Label(grupo_frame,
                      text=info,
                      font=self.font_normal,
                      bg=self.color_white,
                      fg=self.color_text).pack(anchor='w', pady=2)
            
            Button(self.estado_frame,
                   text="Confirmar Trabajo Completado",
                   command=self.trabajo_confirmado,
                   font=self.font_button,
                   bg=self.color_accent,
                   fg=self.color_white,
                   activebackground=self.color_secondary,
                   activeforeground=self.color_white,
                   relief="flat",
                   padx=15,
                   pady=8,
                   bd=0,
                   cursor="hand2").pack(pady=10)
        else:
            status_frame = Frame(self.estado_frame, bg=self.color_secondary, pady=5, padx=10)
            status_frame.pack(fill='x', pady=(0, 10))
            
            Label(status_frame,
                  text="No asignado a ningún grupo",
                  font=self.font_subtitle,
                  bg=self.color_secondary,
                  fg=self.color_white).pack()

    def actualizar_interfaz(self):
        self.esta_en_grupo = False
        self.info_grupo = []
        self.vehiculo_asignado = None
        
        for widget in self.estado_frame.winfo_children():
            widget.destroy()
        
        status_frame = Frame(self.estado_frame, bg=self.color_secondary, pady=5, padx=10)
        status_frame.pack(fill='x', pady=(0, 10))
        
        Label(status_frame,
              text="No asignado a ningún grupo",
              font=self.font_subtitle,
              bg=self.color_secondary,
              fg=self.color_white).pack()
        
        messagebox.showinfo("Éxito", "El grupo ha sido eliminado correctamente.")
        self.update_idletasks()

    def actualizar_vehiculo(self):
        try:
            vehiculo_grupo = None
            for linea in self.info_grupo:
                if linea.startswith("Vehiculo asignado:"):
                    vehiculo_grupo = linea.split(": ")[1].strip()
                    break
                    
            if not vehiculo_grupo:
                messagebox.showerror("Error", "No se encontró el vehículo asignado al grupo")
                return
                
            with open('Nomina_ing_software/archivos_de_texto/Vehiculos.txt', 'r') as archivo:
                lineas = archivo.readlines()
                
            with open('Nomina_ing_software/archivos_de_texto/Vehiculos.txt', 'w') as archivo:
                for linea in lineas:
                    datos = linea.strip().split(" ")
                    if datos[0] == vehiculo_grupo:
                        archivo.write(f"{vehiculo_grupo} Disponible\n")
                    else:
                        archivo.write(linea)
                        
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el estado del vehículo: {str(e)}")

    def actualizar_empleados(self):
        try:
            empleados_grupo = [
                x.split("(")[1].split(")")[0].split(": ")[1] 
                for x in self.info_grupo 
                if "(CC:" in x
            ]
            
            if not empleados_grupo:
                messagebox.showerror("Error", "No se encontraron empleados en el grupo")
                return
                
            with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
                lineas = archivo.readlines()
                
            with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'w') as archivo:
                for linea in lineas:
                    datos = linea.strip().split(" ")
                    if len(datos) == 4 and datos[2] in empleados_grupo:
                        archivo.write(f"{datos[0]} {datos[1]} {datos[2]} Disponible\n")
                    else:
                        archivo.write(linea)
                        
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el estado de los empleados: {str(e)}")

    def actualizar_rutas(self):
        try:
            ruta_actualizada = False
            with open('Nomina_ing_software/archivos_de_texto/rutas.txt', 'r') as archivo:
                lineas = archivo.readlines()
                
            with open('Nomina_ing_software/archivos_de_texto/rutas.txt', 'w') as archivo:
                for linea in lineas:
                    partes = linea.strip().split(" ", 2)
                    if len(partes) == 3:
                        nombre_ruta, estado, equipo = partes
                        if estado == "Cubierta":
                            cedula_buscar = f"(CC: {self.cedula_empleado})"
                            if cedula_buscar in equipo:
                                archivo.write(f"{nombre_ruta} Por_cubrir _\n")
                                ruta_actualizada = True
                            else:
                                archivo.write(linea)
                        else:
                            archivo.write(linea)
                    else:
                        archivo.write(linea)
                        
            if not ruta_actualizada:
                messagebox.showwarning("Advertencia", "No se encontró ninguna ruta asignada al empleado.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el archivo de rutas: {str(e)}")

    def trabajo_confirmado(self):
        if messagebox.askyesno("Confirmación", "¿Está seguro de que desea confirmar el trabajo y eliminar el grupo?"):
            try:
                grupo_actual = self.info_grupo.copy()
                vehiculo_actual = self.vehiculo_asignado
                
                self.actualizar_vehiculo()
                self.actualizar_empleados()
                self.actualizar_rutas()
                self.eliminar_grupo()
                
                self.after(100, self.actualizar_interfaz)
                
            except Exception as e:
                messagebox.showerror("Error", f"Error al confirmar el trabajo: {str(e)}")
                
    def cerrar_sesion(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Está seguro que desea cerrar sesión?"):
            self.destroy()
            Login()

    def obtener_datos_empleado(self):
        try:
            with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" ")
                    if datos[2] == self.cedula_empleado:
                        return {
                            'nombre': datos[0],
                            'apellido': datos[1],
                            'cedula': datos[2],
                            'estado': datos[3]
                        }
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer datos del empleado: {str(e)}")
        return None

    def es_grupo_del_empleado(self, lineas, inicio, fin):
        for i in range(inicio, fin):
            linea = lineas[i].strip()
            if "(CC:" in linea:
                cedula_en_grupo = linea.split("(CC: ")[1].split(")")[0]
                if cedula_en_grupo == self.cedula_empleado:
                    return True
        return False

    def eliminar_grupo(self):
        try:
            with open('Nomina_ing_software/archivos_de_texto/Grupos.txt', 'r') as archivo:
                lineas = archivo.readlines()
            
            with open('Nomina_ing_software/archivos_de_texto/Grupos.txt', 'w') as archivo:
                i = 0
                while i < len(lineas):
                    if lineas[i].strip().startswith("GRUPO CREADO EN FECHA:"):
                        grupo_inicio = i
                        i += 1
                        
                        while i < len(lineas) and not lineas[i].strip().startswith("-" * 50):
                            i += 1
                        
                        if i < len(lineas) and lineas[i].strip().startswith("-" * 50):
                            grupo_fin = i + 1
                        else:
                            grupo_fin = i
                        
                        if not self.es_grupo_del_empleado(lineas, grupo_inicio, grupo_fin):
                            archivo.writelines(lineas[grupo_inicio:grupo_fin])
                        
                        i = grupo_fin
                    else:
                        archivo.write(lineas[i])
                        i += 1
                        
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el grupo: {str(e)}")

"""if __name__ == "__main__":
    Ventana_Empleado_GUI("123456") """