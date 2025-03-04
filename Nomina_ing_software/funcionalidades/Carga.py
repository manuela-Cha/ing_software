from funcionalidades.Gestion import Gestion
class Carga:
    lista_admins = list()

    def limpiar_txt_grupos():
        with open("Nomina_ing_software/archivos_de_texto/Grupos.txt", "w") as file:
                pass
        
    @classmethod
    def carga_usuarios_existentes(cls):
        try:
            with open("Nomina_ing_software/archivos_de_texto/Usuarios_y_contras.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split() 
                    obj = Gestion.cargar_admin(datos[0], datos[1])
                    Carga.lista_admins.append(obj)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            
    @staticmethod
    def validacion_Usuario(usuario_ingresado, contrasena_ingresada):
        flag = False
        for i in Carga.lista_admins:
            if i.get_usuario() == usuario_ingresado and i.get_contrasena() == contrasena_ingresada:
                flag = True
                break
        return flag
    