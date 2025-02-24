from tkinter import *
from tkinter import messagebox
from intfz_grafica.login.login import Login

class Ventana_Empleado_GUI(Tk):
    def __init__(self, cedula_empleado):
        super().__init__()
        self.cedula_empleado = cedula_empleado
        self.title("Portal del Empleado")
        self.geometry("600x600")
        
        self.main_frame = Frame(self, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill='both')
        
        Label(self.main_frame, text="Portal del Empleado", font=('Arial', 18, 'bold')).pack(pady=20)
        
        self.info_empleado = self.obtener_info_empleado()
        
        info_frame = Frame(self.main_frame)
        info_frame.pack(pady=20)
        
        Label(info_frame, text=f"Empleado: {self.info_empleado['nombre']} {self.info_empleado['apellido']}", font=('Arial', 12)).pack()
        Label(info_frame, text=f"Cédula: {self.cedula_empleado}", font=('Arial', 12)).pack()
        
        self.estado_frame = Frame(self.main_frame)
        self.estado_frame.pack(pady=20)
        
        self.verificar_estado_grupo()
        
        #Button(self.main_frame, text="Actualizar Estado", command=self.verificar_estado_grupo, font=('Arial', 11)).pack(pady=10)
        Button(self.main_frame, text="Cerrar Sesión", command=self.cerrar_sesion, font=('Arial', 11)).pack(pady=10)
        
        self.mainloop()
    
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
        """
        Verifica y muestra el estado actual del grupo del empleado
        """
        # Limpiamos primero todos los widgets existentes
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
                        
                        # Guardar el grupo actual temporalmente
                        grupo_temp = []
                        while i < len(lineas) and not lineas[i].strip().startswith("-" * 50):
                            grupo_temp.append(lineas[i].strip())
                            i += 1
                        
                        # Verificar si el empleado está en este grupo usando la cédula exacta
                        for linea_grupo in grupo_temp:
                            if "(CC:" in linea_grupo:
                                cedula_en_grupo = linea_grupo.split("(CC: ")[1].split(")")[0]
                                if cedula_en_grupo == self.cedula_empleado:
                                    self.esta_en_grupo = True
                                    grupo_actual.append(f"Fecha de creación: {fecha}")
                                    grupo_actual.extend(grupo_temp)
                                    self.info_grupo = grupo_actual
                                    
                                    # Obtener el vehículo asignado
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
    
        # Mostramos la información en la interfaz
        self.mostrar_estado_grupo()

    def mostrar_estado_grupo(self):
        """Método separado para mostrar el estado del grupo en la interfaz"""
        if self.esta_en_grupo:
            Label(self.estado_frame, text="Estado: Asignado a un grupo", font=('Arial', 12, 'bold'), fg='green').pack(pady=10)
            grupo_frame = Frame(self.estado_frame)
            grupo_frame.pack(pady=10)
            for info in self.info_grupo:
                Label(grupo_frame, text=info, font=('Arial', 11)).pack()
            Button(self.estado_frame, text="Trabajo Confirmado", command=self.trabajo_confirmado, font=('Arial', 11), fg='white', bg='red').pack(pady=10)
        else:
            Label(self.estado_frame, text="Estado: No asignado a ningún grupo", font=('Arial', 12, 'bold'), fg='blue').pack(pady=10)

    
    def actualizar_interfaz(self):
        """
        Actualiza la interfaz después de confirmar el trabajo y eliminar el grupo
        """
        # Resetear las variables de estado
        self.esta_en_grupo = False
        self.info_grupo = []
        self.vehiculo_asignado = None
        
        # Limpiar el estado_frame actual
        for widget in self.estado_frame.winfo_children():
            widget.destroy()
        
        # Mostrar el nuevo estado (no asignado)
        Label(self.estado_frame, 
            text="Estado: No asignado a ningún grupo", 
            font=('Arial', 12, 'bold'), 
            fg='blue').pack(pady=10)
        
        messagebox.showinfo("Éxito", "El grupo ha sido eliminado correctamente.")
        self.update_idletasks()

    def actualizar_vehiculo(self):
        """
        Actualiza el estado del vehículo asignado al grupo actual a 'Disponible'
        """
        try:
            # Obtener el vehículo del grupo actual
            vehiculo_grupo = None
            for linea in self.info_grupo:
                if linea.startswith("Vehiculo asignado:"):
                    vehiculo_grupo = linea.split(": ")[1].strip()
                    break
                    
            if not vehiculo_grupo:
                messagebox.showerror("Error", "No se encontró el vehículo asignado al grupo")
                return
                
            # Actualizar el archivo de vehículos
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
        """
        Actualiza el estado de los empleados del grupo actual a 'Disponible'
        """
        try:
            # Obtener las cédulas de los empleados del grupo actual
            empleados_grupo = [
                x.split("(")[1].split(")")[0].split(": ")[1] 
                for x in self.info_grupo 
                if "(CC:" in x
            ]
            
            if not empleados_grupo:
                messagebox.showerror("Error", "No se encontraron empleados en el grupo")
                return
                
            # Actualizar el archivo de empleados
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
        """
        Actualiza el archivo de rutas.txt, cambiando el estado de la ruta del empleado actual
        de 'Cubierta' a 'Por_cubrir' y eliminando los integrantes del equipo.
        """
        try:
            ruta_actualizada = False
            with open('Nomina_ing_software/archivos_de_texto/rutas.txt', 'r') as archivo:
                lineas = archivo.readlines()
                
            with open('Nomina_ing_software/archivos_de_texto/rutas.txt', 'w') as archivo:
                for linea in lineas:
                    # Separar la línea en partes: nombre de ruta, estado y equipo
                    partes = linea.strip().split(" ", 2)  # Máximo 2 splits para mantener el equipo junto
                    
                    if len(partes) == 3:  # Si la línea tiene todas las partes esperadas
                        nombre_ruta, estado, equipo = partes
                        
                        # Si la ruta está cubierta, verificar si el empleado está en el equipo
                        if estado == "Cubierta":
                            # Buscar la cédula del empleado en el equipo
                            cedula_buscar = f"(CC: {self.cedula_empleado})"
                            if cedula_buscar in equipo:
                                # Actualizar el estado y limpiar el equipo
                                archivo.write(f"{nombre_ruta} Por_cubrir _\n")
                                ruta_actualizada = True
                            else:
                                # Mantener la línea sin cambios
                                archivo.write(linea)
                        else:
                            # Mantener la línea sin cambios
                            archivo.write(linea)
                    else:
                        # Si la línea no tiene el formato esperado, mantenerla sin cambios
                        archivo.write(linea)
                        
            if not ruta_actualizada:
                messagebox.showwarning("Advertencia", "No se encontró ninguna ruta asignada al empleado.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el archivo de rutas: {str(e)}")

    def trabajo_confirmado(self):
        if messagebox.askyesno("Confirmación", "¿Está seguro de que desea confirmar el trabajo y eliminar el grupo?"):
            try:
                # Guardar una copia de la información del grupo antes de eliminarlo
                grupo_actual = self.info_grupo.copy()
                vehiculo_actual = self.vehiculo_asignado
                
                # Realizar las actualizaciones
                self.actualizar_vehiculo()
                self.actualizar_empleados()
                self.actualizar_rutas()
                self.eliminar_grupo()
                
                # Actualizar la interfaz
                self.after(100, self.actualizar_interfaz)
                
            except Exception as e:
                messagebox.showerror("Error", f"Error al confirmar el trabajo: {str(e)}")
                
    def cerrar_sesion(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Está seguro que desea cerrar sesión?"):
            self.destroy()
            Login()

    def obtener_datos_empleado(self):
        """Obtiene los datos completos del empleado desde el archivo de empleados"""
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
        """
        Verifica si el grupo entre los índices dados corresponde al empleado actual
        """
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
                    # Si encontramos el inicio de un grupo
                    if lineas[i].strip().startswith("GRUPO CREADO EN FECHA:"):
                        grupo_inicio = i
                        i += 1
                        
                        # Encontrar el final del grupo
                        while i < len(lineas) and not lineas[i].strip().startswith("-" * 50):
                            i += 1
                        
                        # Si llegamos al separador, incluirlo en el rango
                        if i < len(lineas) and lineas[i].strip().startswith("-" * 50):
                            grupo_fin = i + 1
                        else:
                            grupo_fin = i
                        
                        # Verificar si este es el grupo del empleado usando múltiples criterios
                        if not self.es_grupo_del_empleado(lineas, grupo_inicio, grupo_fin):
                            # Si no es el grupo del empleado, escribirlo completo
                            archivo.writelines(lineas[grupo_inicio:grupo_fin])
                        
                        i = grupo_fin
                    else:
                        archivo.write(lineas[i])
                        i += 1
                        
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el grupo: {str(e)}")
