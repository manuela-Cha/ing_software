class Admin:
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena

    def get_usuario(self):
        return self.usuario
    
    def get_contrasena(self):
        return self.contrasena

    def __str__(self):
        return f"{self.usuario} {self.contrasena} \n"
    
    def __repr__(self):
        return str(self)
