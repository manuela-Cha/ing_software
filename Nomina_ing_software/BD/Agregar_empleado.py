from BD.conexion import Conectar
from mysql.connector import Error

class Agregar_empleado:
    def registrar_empleado(nombre, apellido, cedula, turno, ruta_asignada):
        "Inserta un empleado en la tabla 'empleados'."
        conexion = Conectar.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                consulta = """
                INSERT INTO usuarios_registrados (nombre, apellido, cedula, turno, ruta_asignada)
                VALUES (%s, %s, %s, %s, %s)
                """
                valores = (nombre, apellido, cedula, turno, ruta_asignada)
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