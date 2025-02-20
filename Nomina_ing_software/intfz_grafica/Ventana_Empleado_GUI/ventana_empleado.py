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
                        
                        # Buscar en todo el grupo actual
                        encontrado = False
                        while i < len(lineas) and not lineas[i].strip().startswith("-" * 50):
                            if f"CC: {self.cedula_empleado}" in lineas[i]:
                                encontrado = True
                            i += 1
                        
                        # Si encontramos al empleado en este grupo, recolectar toda la información
                        if encontrado:
                            self.esta_en_grupo = True
                            grupo_actual.append(f"Fecha de creación: {fecha}")
                            j = grupo_inicio + 1
                            while j < i:
                                if lineas[j].startswith("Vehiculo asignado:"):
                                    self.vehiculo_asignado = lineas[j].split(": ")[1].strip()
                                grupo_actual.append(lineas[j].strip())
                                j += 1
                            self.info_grupo = grupo_actual
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

    
    def trabajo_confirmado(self):
        if messagebox.askyesno("Confirmación", "¿Está seguro de que desea confirmar el trabajo y eliminar el grupo?"):
            try:
                self.actualizar_vehiculo()
                self.actualizar_empleados()
                self.eliminar_grupo()
                
                # Usamos after para dar un pequeño retraso antes de actualizar la interfaz
                self.after(100, self.actualizar_interfaz)
                
            except Exception as e:
                messagebox.showerror("Error", f"Error al confirmar el trabajo: {str(e)}")
    
    def actualizar_interfaz(self):
        self.verificar_estado_grupo()
        messagebox.showinfo("Éxito", "El grupo ha sido eliminado correctamente.")
        self.update_idletasks()

    def actualizar_vehiculo(self):
        try:
            with open('Nomina_ing_software/archivos_de_texto/Vehiculos.txt', 'r') as archivo:
                lineas = archivo.readlines()
            with open('Nomina_ing_software/archivos_de_texto/Vehiculos.txt', 'w') as archivo:
                for linea in lineas:
                    if linea.startswith(self.vehiculo_asignado):
                        archivo.write(f"{self.vehiculo_asignado} Disponible\n")
                    else:
                        archivo.write(linea)
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el estado del vehículo: {str(e)}")
    
    def actualizar_empleados(self):
        try:
            with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'r') as archivo:
                lineas = archivo.readlines()
            with open('Nomina_ing_software/archivos_de_texto/Empleados.txt', 'w') as archivo:
                for linea in lineas:
                    datos = linea.strip().split(" ")
                    if len(datos) == 4 and datos[2] in [x.split("(")[1].split(")")[0].split(": ")[1] for x in self.info_grupo if "CC:" in x]:
                        archivo.write(f"{datos[0]} {datos[1]} {datos[2]} Disponible\n")
                    else:
                        archivo.write(linea)
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el estado de los empleados: {str(e)}")

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
        """Verifica si el grupo entre los índices dados corresponde al empleado actual"""
        datos_empleado = self.obtener_datos_empleado()
        if not datos_empleado:
            return False
        
        encontrado_cedula = False
        encontrado_nombre = False
        encontrado_apellido = False
        
        for i in range(inicio, fin):
            linea = lineas[i].strip()
            # Verificar coincidencia de cédula
            if f"CC: {datos_empleado['cedula']}" in linea:
                encontrado_cedula = True
            # Verificar coincidencia de nombre
            if datos_empleado['nombre'] in linea:
                encontrado_nombre = True
            # Verificar coincidencia de apellido
            if datos_empleado['apellido'] in linea:
                encontrado_apellido = True
                
        return encontrado_cedula and encontrado_nombre and encontrado_apellido

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
