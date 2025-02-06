class Empleado:
    def __init__(self, nombre, apellido, cedula):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.estado = "Disponible"

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.cedula} {self.estado}\n"
    
    def __repr__(self):
        return str(self)

    