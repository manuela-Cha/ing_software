from Objetos.Empleado import Empleado
from Objetos.Vehiculo import Vehiculo
from Objetos.Ruta import Ruta
class Gestion:
    def crear_empleado(nombre, apellido, cedula):
        return Empleado(nombre,apellido, cedula)
    
    def crear_vehiculo(id_vehiculo):
        return Vehiculo(id_vehiculo)
    
    def crear_ruta(ruta):
        return Ruta(ruta)
    
    def crear_nuevo_empleado():
        Empleado.crear_empleado()

    def crear_nueva_ruta():
        Ruta.crear_ruta()

    def crear_nuevo_vehiculo():
        Vehiculo.crear_vehiculo()