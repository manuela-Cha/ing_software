from Objetos.Empleado import Empleado
from Objetos.Vehiculo import Vehiculo
from Objetos.Ruta import Ruta

class Gestion:
    def cargar_empleado(nombre, apellido, cedula):
        return Empleado(nombre,apellido, cedula)
    
    def cargar_vehiculo(id_vehiculo):
        return Vehiculo(id_vehiculo)
    
    def cargar_ruta(ruta):
        return Ruta(ruta)

    def crear_nueva_ruta():
        Ruta.crear_ruta()

    
    