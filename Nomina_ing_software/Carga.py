from funcionalidades.Gestion import Gestion
class Carga:
    lista_empleados = list()
    lista_vehiculos = list()
    lista_rutas = list()

    @classmethod
    def carga_empleados_existentes(cls):
        try:
            with open("Nomina_ing_software/Empleados.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split()
                    datos_empleado = [
                        datos[0],
                        datos[1],
                        datos[2]
                    ] 
                    obj = Gestion.crear_empleado(datos_empleado)
                    Carga.lista_empleados.append(obj)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    @staticmethod
    def carga_vehiculos_existentes(cls):
        try:
            with open("Nomina_ing_software/Vehiculos.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split()
                    obj = Gestion.crear_vehiculo(datos[0])
                    obj.estado = datos[1]
                    Carga.lista_vehiculos.append(obj)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    @staticmethod
    def carga_rutas_existentes(cls):
        try:
            with open("Nomina_ing_software/Rutas.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split() 
                    obj = Gestion.crear_ruta(datos[0])
                    obj.estado = datos[1]
                    Carga.lista_rutas.append(obj)
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
            with open("Nomina_ing_software/Empleados.txt", "a") as file:
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
        return vehiculo
    
    @staticmethod
    def crear_nueva_ruta():
        print("Ingrese la ruta: ")

        ruta_str = input("ruta: ")
        ruta = Gestion.cargar_ruta(ruta_str)
        return ruta