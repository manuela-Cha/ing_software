from funcionalidades.Carga import Carga
from intfz_grafica.Consola_provisional import Consola
from intfz_grafica.login.login import Login

Carga.carga_empleados_existentes()
Carga.carga_vehiculos_existentes()
Carga.carga_rutas_existentes()
Carga.carga_admins_existentes()
Carga.limpiar_txt_grupos()

Login()
