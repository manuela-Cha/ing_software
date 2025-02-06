class Vehiculo:
    def __init__(self, id_vehiculo):
        self.id_vehiculo = id_vehiculo
        self.estado = "Disponible"

    def __str__(self):
        return f"{self.id_vehiculo} {self.estado}\n"

    