class Empleado:
    def __init__(self, nombre, apellido, cedula):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.turno = ""
        self.ruta_asignada = ""

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.cedula}\n"

    