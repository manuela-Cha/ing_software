class Ruta:
    def __init__(self, ruta):
        self.ruta = ruta
        self.estado_ruta = "Sin cubrir"

    @staticmethod
    def crear_ruta():
        print("Ingrese la ruta: ")

        ruta_str = input("ruta: ")
        ruta = Ruta(ruta_str)
        return ruta

    def __str__(self):
        return f"{self.ruta} {self.estado_ruta} \n"

    