from funcionalidades.Gestion import Gestion
class Carga:
    """lista_empleados = list()
    lista_vehiculos = list()
    lista_rutas = list()"""
    lista_admins = list()
    #lista_grupos = list()

    def limpiar_txt_grupos():
        with open("Nomina_ing_software/archivos_de_texto/Grupos.txt", "w") as file:
                pass
        
    @classmethod
    def carga_usuarios_existentes(cls):
        try:
            with open("Nomina_ing_software/archivos_de_texto/Usuarios_y_contras.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split() 
                    obj = Gestion.cargar_admin(datos[0], datos[1])
                    Carga.lista_admins.append(obj)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            
    @staticmethod
    def validacion_Usuario(usuario_ingresado, contrasena_ingresada):
        flag = False
        for i in Carga.lista_admins:
            if i.get_usuario() == usuario_ingresado and i.get_contrasena() == contrasena_ingresada:
                flag = True
                break
        return flag
    """@classmethod
    def carga_empleados_existentes(cls):
        try:
            with open("Nomina_ing_software/archivos_de_texto/Empleados.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split()
                    obj = Gestion.cargar_empleado(datos[0], datos[1], datos[2])
                    Carga.lista_empleados.append(obj)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    @classmethod
    def carga_vehiculos_existentes(cls):
        try:
            with open("Nomina_ing_software/archivos_de_texto/Vehiculos.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split()
                    obj = Gestion.cargar_vehiculo(datos[0])
                    obj.estado = datos[1]
                    Carga.lista_vehiculos.append(obj)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    @classmethod
    def carga_rutas_existentes(cls):
        try:
            with open("Nomina_ing_software/archivos_de_texto/Rutas.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split() 
                    obj = Gestion.cargar_ruta(datos[0])
                    obj.estado = datos[1]
                    Carga.lista_rutas.append(obj)
        except FileNotFoundError as e:
            print(f"Error: {e}")"""

    

    """@classmethod
    def carga_grupos_existentes(cls):
        try:
            with open("Nomina_ing_software/archivos_de_texto/Grupos.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split()
                    obj = Gestion.cargar_grupo(datos[0], datos[1], datos[2], datos[3:])
                    Carga.lista_grupos.append(obj)
        except FileNotFoundError as e:
            print(f"Error: {e}")"""
        
    """@staticmethod
    def crear_nuevo_empleado():
        print("Ingrese los datos del empleado: ")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        cedula = input("Cédula: ").strip()

        if not nombre or not apellido or not cedula:
            print("Error: Todos los campos deben estar llenos.")
            return None

        ruta_archivo = "Nomina_ing_software/archivos_de_texto/Empleados.txt"
        
        try:
            with open(ruta_archivo, "r") as file:
                for linea in file:
                    if linea.strip().endswith(cedula):
                        print(f"Ya existe un empleado con la cédula {cedula}.")
                        return None
        except FileNotFoundError:
            print("No se encontró el archivo. Se creará uno nuevo al agregar el empleado.")

        empleado = Gestion.cargar_empleado(nombre, apellido, cedula)

        try:
            with open(ruta_archivo, "a") as file:
                file.write(f"{nombre} {apellido} {cedula}\n")
            Carga.carga_empleados_existentes()
            print("Empleado agregado exitosamente.")
        except Exception as e:
            print("No se pudo escribir en Empleados:", e)
        
        return empleado"""

    """@staticmethod
    def crear_nuevo_vehiculo():
        print("Ingrese los datos del vehiculo: ")

        id_vehiculo = input("Id del vehiculo: ")
        vehiculo = Gestion.cargar_vehiculo(id_vehiculo)
        if id_vehiculo == "":
            return
        try:
            with open("Nomina_ing_software/archivos_de_texto/Empleados.txt", "a") as file:
                file.write("{} {}\n".format(id_vehiculo, vehiculo.estado)) 
                Carga.carga_empleados_existentes
        except:
            print("No se pudo escribir en Vehiculos")

        return vehiculo
    
    @staticmethod
    def crear_nueva_ruta():
        print("Ingrese la ruta: ")

        ruta_str = input("ruta: ")
        ruta = Gestion.cargar_ruta(ruta_str)
        return ruta"""
    
    """@staticmethod
    def crear_grupo():
        for empleado in Carga.lista_empleados:
            if empleado.estado == "Disponible":
                print(empleado)
        dia = input("Ingrese el día actual: ")
        mes = input("Ingrese el mes actual: ")
        anio = input("Ingrese el año actual: ")

        integrantes = []
        for i in range(3):
            cedula = input(f"Ingrese cédula del integrante {i+1}: ")
            integrantes.append(cedula)

        print("Lista de vehículos:", Carga.lista_vehiculos)
        vehiculo_id = input("Ingrese el ID del vehículo: ")

        empleados_validos = []
        for cedula in integrantes:
            empleado = next((e for e in Carga.lista_empleados if e.cedula == cedula and e.estado == "Disponible"), None)
            if empleado:
                empleados_validos.append(empleado)

        vehiculo = next((v for v in Carga.lista_vehiculos if v.id_vehiculo == vehiculo_id and v.estado == "Disponible"), None)

        if len(empleados_validos) == 3 and vehiculo:
            try:
                with open("Nomina_ing_software/archivos_de_texto/Grupos.txt", "a") as file:
                    file.write(f"{dia} {mes} {anio} {' '.join(integrantes)} {vehiculo_id} {vehiculo.estado}\n")

                for empleado in empleados_validos:
                    empleado.estado = "Ocupado"
                vehiculo.estado = "Ocupado"

                print("Grupo registrado exitosamente.")
            except Exception as e:
                print("No se pudo escribir en Grupos:", e)
        else:
            print("Error: Algún integrante o el vehículo no está disponible o no existe.")"""
    
    
    
    """@staticmethod
    def eliminar_empleado():
        cedula = input("Ingrese la Cedula del empleado que eliminara: ")
        try:
            with open("Nomina_ing_software/archivos_de_texto/Empleados.txt", "r") as file:
                lineas = file.readlines()

            nuevas_lineas = [linea for linea in lineas if not linea.strip().endswith(cedula)]

            if len(nuevas_lineas) == len(lineas):
                print(f"No se encontró la cédula {cedula} en el archivo.")
                return
            
            with open("Nomina_ing_software/archivos_de_texto/Empleados.txt", "w") as file:
                file.writelines(nuevas_lineas)

            print(f"Empleado con cédula {cedula} eliminado correctamente.")
            Carga.carga_empleados_existentes()

        except FileNotFoundError:
            print("Error: No se encontró el archivo.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")"""

    """def asignar_ruta():
        print(Carga.lista_rutas)
        ruta_grupos = "Nomina_ing_software/archivos_de_texto/Grupos.txt"
        ruta_rutas = "Nomina_ing_software/archivos_de_texto/Rutas.txt"
        ruta_asignacion = "Nomina_ing_software/archivos_de_texto/Asignacion_de_rutas.txt"

        grupo_disponible = None
        ruta_valida = None

        
        try:
            with open(ruta_grupos, "r") as file:
                lineas_grupos = file.readlines()

            for i, linea in enumerate(lineas_grupos):
                if linea.strip().endswith("Disponible"):
                    grupo_disponible = linea.strip()
                    indice_grupo = i 
                    break
        except FileNotFoundError:
            print("Error: No se encontró el archivo de grupos.")
            return
        except Exception as e:
            print(f"Ocurrió un error al leer Grupos.txt: {e}")
            return

        if not grupo_disponible:
            print("No hay grupos disponibles.")
            return

        
        ruta_ingresada = input("Ingrese la ruta: ").strip()

    
        try:
            with open(ruta_rutas, "r") as file:
                lineas_rutas = file.readlines()

            for i, linea in enumerate(lineas_rutas):
                palabras = linea.strip().split()
                if palabras and palabras[0] == ruta_ingresada and palabras[-1] == "Por_cubrir":
                    ruta_valida = linea.strip()
                    indice_ruta = i  
                    break
        except FileNotFoundError:
            print("Error: No se encontró el archivo de rutas.")
            return
        except Exception as e:
            print(f"Ocurrió un error al leer Rutas.txt: {e}")
            return

        if not ruta_valida:
            print("La ruta ingresada no existe o ya está cubierta en el archivo de rutas.")
            return

        
        try:
            with open(ruta_asignacion, "a") as file:
                file.write(f"{grupo_disponible} - {ruta_valida}\n")

            print(f"Grupo asignado correctamente: {grupo_disponible} -> {ruta_valida}")
        except Exception as e:
            print(f"Ocurrió un error al escribir en Asignacion_de_rutas.txt: {e}")
            return

        
        try:
            lineas_grupos[indice_grupo] = lineas_grupos[indice_grupo].replace("Disponible", "Ocupado") + "\n"
            with open(ruta_grupos, "w") as file:
                file.writelines(lineas_grupos)
        except Exception as e:
            print(f"Ocurrió un error al actualizar Grupos.txt: {e}")

        try:
            lineas_rutas[indice_ruta] = lineas_rutas[indice_ruta].replace("Por_cubrir", "Cubierta") + "\n"
            with open(ruta_rutas, "w") as file:
                file.writelines(lineas_rutas)
        except Exception as e:
            print(f"Ocurrió un error al actualizar Rutas.txt: {e}")"""

      
       
    """def Registrar_estado_del_vehiculo():
        print(Carga.lista_vehiculos)
        ruta_vehiculos = "Nomina_ing_software/archivos_de_texto/Vehiculos.txt"

        id_vehiculo = input("Ingrese el ID del vehículo al que le desea cambiar el estado: ").strip()
        vehiculo_encontrado = False

        try:
            with open(ruta_vehiculos, "r") as file:
                lineas = file.readlines()

            for i, linea in enumerate(lineas):
                palabras = linea.strip().split()
                if palabras and palabras[0] == id_vehiculo:  
                    palabras[-1] = "En_revision"  
                    lineas[i] = " ".join(palabras) + "\n"
                    vehiculo_encontrado = True
                    break

            
            if vehiculo_encontrado:
                with open(ruta_vehiculos, "w") as file:
                    file.writelines(lineas)
                print(f"El estado del vehículo {id_vehiculo} ha sido cambiado a 'En revisión'.")
            else:
                print("No se encontró un vehículo con el ID ingresado.")

        except FileNotFoundError:
            print("Error: No se encontró el archivo de vehículos.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar el estado del vehículo: {e}")"""

 



