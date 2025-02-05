class Empleado:
    def __init__(self, nombre, apellido, cedula):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.turno = ""
        self.ruta_asignada = ""

    @staticmethod
    def crear_empleado():
        print("Ingrese los datos del empleado: ")

        cedula = input("Cedula: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        empleado = Empleado( nombre, apellido, cedula)
        return empleado

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.cedula}\n"

    