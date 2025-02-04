from mysql.connector import Error
from BD.conexion import Conectar

class Eliminar_empleado:
    @staticmethod
    def verificar_existencia(nombre, apellido, cedula):
        """Verifica si el empleado existe en la base de datos antes de eliminarlo."""
        conexion = Conectar.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                consulta = """
                SELECT COUNT(*) FROM usuarios_registrados 
                WHERE nombre = %s AND apellido = %s AND cedula = %s
                """
                cursor.execute(consulta, (nombre.strip(), apellido.strip(), cedula.strip()))
                resultado = cursor.fetchone()
                cursor.close()
                return resultado[0] > 0  # Retorna True si el empleado existe
            except Error as e:
                print(f"Error en la verificación de existencia: {e}")
                return False
            finally:
                if conexion.is_connected():
                    conexion.close()

    @staticmethod
    def eliminar_empleado(nombre, apellido, cedula):
        """Elimina un empleado en la tabla 'usuarios_registrados'."""
        conexion = Conectar.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                consulta = """
                DELETE FROM usuarios_registrados 
                WHERE nombre = %s AND apellido = %s AND cedula = %s
                """
                valores = (nombre.strip(), apellido.strip(), cedula.strip())

                if not Eliminar_empleado.verificar_existencia(nombre, apellido, cedula):
                    print("Error: El empleado no existe en la base de datos.")
                    return False  # No se eliminó porque no existe

                cursor.execute(consulta, valores)
                conexion.commit()
                print("Empleado eliminado exitosamente.")
                return True  # Se eliminó correctamente
            except Error as e:
                print(f"Error al eliminar el empleado: {e}")
                return False
            finally:
                if conexion.is_connected():
                    cursor.close()
                    conexion.close()
                    print("Conexión cerrada.")
