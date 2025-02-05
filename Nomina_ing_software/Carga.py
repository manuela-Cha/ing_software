from Nomina_ing_software.funcionalidades.Gestion import Gestion
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