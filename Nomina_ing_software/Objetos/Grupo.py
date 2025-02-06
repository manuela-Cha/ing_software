class Grupo:
    def __init__(self, dia, mes, anio, integrantes ):
        self.integrantes = integrantes
        self.dia = dia
        self.mes = mes
        self.anio  = anio

    def __str__(self):
        return f" {self.dia} {self.mes} {self.anio} {self.integrantes}\n"
    
    def __repr__(self):
        return str(self)