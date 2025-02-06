#from intfz_grafica.registrar_empleado_gui import Registrar_empleado_gui
#from intfz_grafica.registrar_empleado_gui import Registrar_empleado_GUI
"from intfz_grafica.eliminar_empleado_gui import Eliminar_empleado_GUI"

from Carga import Carga
from intfz_grafica.Consola_provisional import Consola

Carga.carga_empleados_existentes()
Carga.carga_vehiculos_existentes()
Carga.carga_rutas_existentes()
Carga.carga_admins_existentes()
Carga.carga_grupos_existentes()

Carga.crear_grupo()

#print(Carga.lista_grupos)

"""consola = Consola()
consola.validacion()"""