from funcionalidades.Carga import Carga

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
                    print("1) Registrar Nuevo empleado")
                    print("2) Formar grupo")
                    print("3) Eliminar empleado")
                    print("4) Registrar Nuevo vehiculo") 
                    print("5) Asignar ruta")
                    print("6) Registrar estado del vehiculo")
                    print("7) Salir")
                    
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
                            Carga.asignar_ruta()
                        elif respuesta == "6":
                            Carga.Registrar_estado_del_vehiculo()
                        elif respuesta == "7":
                            print("Saliendo del menú...")
                            break  
                        else:
                            print("Opción no válida.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número.")
            

    





    