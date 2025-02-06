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
                    print("1) Registrar empleado") #Lista
                    print("2) Formar grupos") #Lista - falta probar
                    print("3) Asignar rutas a un grupo")
                    print("4) Actualizar estado de un vehiculo")
                    print("5) consultar estado solicitudes")
                    print("6) solicitar eliminar equipo")
                    print("7) Salir")
                    
                    try:
                        respuesta = input("Ingrese el número de la acción deseada: ")
                        if respuesta == "1":
                            Carga.crear_nuevo_empleado()
                        elif respuesta == "2":
                            Carga.crear_grupo() 
                        elif respuesta == "3":
                            investigador.escribir_inventario_en_txt() 
                        elif respuesta == "4":
                            investigador.escribir_solicitudes_en_txt() 
                        elif respuesta == "5":
                            investigador.consultar_estado_solicitudes() 
                        elif respuesta == "6":
                            investigador.solicitar_eliminar_equipo()
                        elif respuesta == "7":
                            print("Saliendo del menú de investigador...")
                            break  
                        else:
                            print("Opción no válida.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número.")
            

    





    