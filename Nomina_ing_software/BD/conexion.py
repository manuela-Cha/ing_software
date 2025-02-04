import mysql.connector
from mysql.connector import Error

class Conectar:
    def conectar():
        """Establece la conexión con la base de datos MySQL."""
        try:
            conexion = mysql.connector.connect(
                host='localhost',          
                user='root',         
                password='',  
                database='bd_registros'         
            )
            if conexion.is_connected():
                print("Conexión exitosa a la base de datos")
            return conexion

        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

"""def eliminar_empleado_registrado(nombre, apellido, edad):
    "Elimina un empleado en la tabla 'usuarios_registrados'."
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "
            DELETE FROM usuarios_registrados 
            WHERE nombre = %s AND apellido = %s AND edad = %s
            "
            valores = (nombre.strip(), apellido.strip(), edad)
            
            # Construir y mostrar la consulta completa para depuración
            consulta_completa = consulta % tuple(map(repr, valores))
            print("Consulta SQL ejecutada:", consulta_completa)

            cursor.execute(consulta, valores)
            conexion.commit()  # Confirma la eliminación
            print("Empleado eliminado exitosamente.")

        except Error as e:
            print(f"Error al eliminar el empleado: {e}")

        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
                print("Conexión cerrada.")

    def registrar_vehiculo():"""




