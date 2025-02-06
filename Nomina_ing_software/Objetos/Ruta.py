class Ruta:
    def __init__(self, ruta):
        self.ruta = ruta
        self.estado_ruta = "Sin cubrir"

    def __str__(self):
        return f"{self.ruta} {self.estado_ruta} \n"
    
    def __repr__(self):
        return str(self)

    