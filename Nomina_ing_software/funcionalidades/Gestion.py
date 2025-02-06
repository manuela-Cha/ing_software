from Objetos.Empleado import Empleado
from Objetos.Vehiculo import Vehiculo
from Objetos.Admin import Admin
from Objetos.Ruta import Ruta
from Objetos.Grupo import Grupo

class Gestion:
    def cargar_empleado(nombre, apellido, cedula):
        return Empleado(nombre,apellido, cedula)
    
    def cargar_vehiculo(id_vehiculo):
        return Vehiculo(id_vehiculo)
    
    def cargar_ruta(ruta):
        return Ruta(ruta)
    
    def cargar_admin(usuario, contrasena):
        return Admin(usuario, contrasena)

    def cargar_grupo(dia, mes, anio, integrantes):
        return Grupo(dia, mes, anio, integrantes)
    
    