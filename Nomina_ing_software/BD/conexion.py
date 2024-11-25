import mysql.connector
from mysql.connector import Error

def conectar():
    """Establece la conexión con la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            host='localhost',           # Cambia a la IP de tu servidor si no es local
            user='root',          # Reemplaza con tu usuario de MySQL
            password='',   # Reemplaza con tu contraseña de MySQL
            database='bd_registros'          # Nombre de la base de datos
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
        return conexion

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def registrar_empleado(nombre, apellido, edad):
    "Inserta un empleado en la tabla 'empleados'."
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
            INSERT INTO usuarios_registrados (nombre, apellido, edad)
            VALUES (%s, %s, %s)
            """
            valores = (nombre, apellido, edad)
            cursor.execute(consulta, valores)
            conexion.commit()  # Confirma la inserción
            print("Empleado agregado exitosamente.")

        except Error as e:
            print(f"Error al agregar el empleado: {e}")

        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
                print("Conexión cerrada.")

def eliminar_empleado_registrado(nombre, apellido, edad):
    """Elimina un empleado en la tabla 'usuarios_registrados'."""
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
            DELETE FROM usuarios_registrados 
            WHERE nombre = %s AND apellido = %s AND edad = %s
            """
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




