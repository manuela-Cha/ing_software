from funcionalidades.Gestion import Gestion
class Carga:
    lista_empleados = list()
    lista_vehiculos = list()
    lista_rutas = list()
    lista_admins = list()
    lista_grupos = list()

    @classmethod
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
            print(f"Error: {e}")

    @classmethod
    def carga_admins_existentes(cls):
        try:
            with open("Nomina_ing_software/archivos_de_texto/Usuarios_y_contras.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split() 
                    obj = Gestion.cargar_admin(datos[0], datos[1])
                    Carga.lista_admins.append(obj)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    @classmethod
    def carga_grupos_existentes(cls):
        try:
            with open("Nomina_ing_software/archivos_de_texto/Grupos.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split()
                    obj = Gestion.cargar_grupo(datos[0], datos[1], datos[2], datos[3:])
                    Carga.lista_grupos.append(obj)
        except FileNotFoundError as e:
            print(f"Error: {e}")
        
    @staticmethod
    def crear_nuevo_empleado():
        print("Ingrese los datos del empleado: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = input("Cedula: ")
        empleado = Gestion.cargar_empleado(nombre, apellido, cedula)

        try:
            with open("Nomina_ing_software/archivos_de_texto/Empleados.txt", "a") as file:
                file.write("{} {} {}\n".format(nombre, apellido, cedula)) 
                Carga.carga_empleados_existentes
        except:
            print("No se pudo escribir en Empleados")
        return empleado
    
    @staticmethod
    def crear_nuevo_vehiculo():
        print("Ingrese los datos del vehiculo: ")

        id_vehiculo = input("Id del vehiculo: ")
        vehiculo = Gestion.cargar_vehiculo(id_vehiculo)

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
        return ruta
    
    @staticmethod
    def crear_grupo():
        print("Lista de empleados:", Carga.lista_empleados)
        dia = input("Ingrese el día actual: ")
        mes = input("Ingrese el mes actual: ")
        anio = input("Ingrese el año actual: ")

        integrantes = []
        for i in range(4):
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

        if len(empleados_validos) == 4 and vehiculo:
            try:
                with open("Nomina_ing_software/archivos_de_texto/Grupos.txt", "a") as file:
                    file.write(f"{dia} {mes} {anio} {' '.join(integrantes)} {vehiculo_id}\n")

                for empleado in empleados_validos:
                    empleado.estado = "Ocupado"
                vehiculo.estado = "Ocupado"

                print("Grupo registrado exitosamente.")
            except Exception as e:
                print("No se pudo escribir en Grupos:", e)
        else:
            print("Error: Algún integrante o el vehículo no está disponible o no existe.")
    
    @staticmethod
    def validacion_admin(usuario_ingresado, contrasena_ingresada):
        flag = False
        for i in Carga.lista_admins:
            if i.get_usuario() == usuario_ingresado and i.get_contrasena() == contrasena_ingresada:
                flag = True
                break
        return flag
    
    @staticmethod
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
            print(f"Ocurrió un error: {e}")





