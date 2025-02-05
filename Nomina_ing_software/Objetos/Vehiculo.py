class Vehiculo:
    def __init__(self, id_vehiculo):
        self.id_vehiculo = id_vehiculo
        self.estado = "Disponible"

    @staticmethod
    def crear_vehiculo():
        print("Ingrese los datos del vehiculo: ")

        id_vehiculo = input("Id del vehiculo: ")
        vehiculo = Vehiculo(id_vehiculo)
        return vehiculo

    def __str__(self):
        return f"{self.id_vehiculo} {self.estado}\n"

    