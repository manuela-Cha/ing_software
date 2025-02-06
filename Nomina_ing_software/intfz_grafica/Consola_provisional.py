from Carga import Carga

class Consola():

    @staticmethod
    def inicio():
        while True:

            print("Bienvenido admin, identifiquese: ")

            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            if not Carga.validacion_admin(usuario, contrasena):
                print("Cédula o contraseña incorrectos. Intente nuevamente.")
                continue

            while True: 
                    print("\nSeleccione la acción que desee realizar:")
                    print("1) Registrar Nuevo empleado") #Lista
                    print("2) Formar grupo") #Lista
                    print("3) Eliminar empleado") #LISTA
                    print("4) Registrar Nuevo vehiculo") #
                    print("5) Salir")
                    
                    try:
                        respuesta = input("Ingrese el número de la acción deseada: ")
                        if respuesta == "1":
                            Carga.crear_nuevo_empleado()
                        elif respuesta == "2":
                            Carga.crear_grupo() 
                        elif respuesta == "3":
                            Carga.eliminar_empleado() 
                        elif respuesta == "4":
                            Carga.crear_nuevo_vehiculo()
                        elif respuesta == "5":
                            print("Saliendo del menú...")
                            break  
                        else:
                            print("Opción no válida.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número.")
            

    





    