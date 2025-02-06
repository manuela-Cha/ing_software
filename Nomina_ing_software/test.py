
import re
ruta = "AAA-2533" #Array de rutas

class Empleado:
    empleados_actuales = []
    def __init__(self, nombre, apellido, cedula):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.turno = ""
        self.rutas_asignadas = []
        Empleado.empleados_actuales.append(self.cedula)

    @staticmethod
    def crear_empleado():
        print("Ingrese los datos del empleado: ")

        cedula = input("Cedula: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        empleado = Empleado( nombre, apellido, cedula)
        return empleado

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.cedula}\n"

def evaluarValidezRuta(ruta):
    if re.search("([A-Z]){3}-([0-9]){4}", ruta) == None:
        return False
    else: 
        return True

def evaluarValidezVehiculo(placa):
    if re.search("([A-Z]){3}-([0-9]){3}", placa) == None:
        return False
    else: 
        return True

class Grupo:
    numero_de_grupos = 1

    def __init__(self, empleados = [], rutas = [], vehiculo = None):
        self.id = Grupo.numero_de_grupos
        Grupo.numero_de_grupos+=1
        self.empleados = empleados
        self.rutas = rutas
        self.vehiculo = vehiculo
#Hola
    def AsignarRuta(self, ruta):
        if evaluarValidezRuta(ruta):
            self.rutas.append(ruta)
            print(f"Se ha añadido la ruta al grupo {self.id}")
        else:
            print("La ruta ingresada es inválida, por tanto no puede ser asignada")
    
    def AddEmpleado(self, cedula):
        if len(self.empleados) == 3:
            return f"El grupo {self.id} esta completo, no es posible añadir mas integrantes"

        if cedula in self.empleados:
            return f"El empleado {cedula} ya se encuentra en el grupo, revise los datos ingresados"

        if cedula in Empleado.empleados_actuales:
            self.empleados.append(cedula)
            return f"El empleado {cedula} ha sido asignado correctamente al grupo {self.id}"
        else:
            return "La cedula ingresada no es válida o no se encuentra registrada como empleado, verifique sus datos"

    def removeEmpleado(self, cedula):
        if cedula in self.empleados:
            self.empleados.remove(cedula)
            return f"El empleado con C.C {cedula} ha sido removido del grupo correctamente"
        else:
            return f"El empleado con C.C {cedula} no se encuentra en el grupo {self.id}, verifique los datos"
    
    def addVehiculo(self, placa):
        if self.vehiculo != None:
            return f"El grupo {self.id} ya tiene un vehiculo asignado, revise los datos ingresados"

        if evaluarValidezVehiculo(placa):
            self.vehiculo = placa
            return f"El vehiculo de placa {placa} ha sido asignado al grupo {self.id} correctamente"
        else:
            return f"La placa ingresada es invalida, verifique los datos ingresados"
    
    def toString(self):
        return f"{self.id}, {self.empleados}, {self.vehiculo}, {self.rutas}"

            

grupo1 = Grupo()
grupo2 = Grupo()
grupo3 = Grupo()
grupo4 = Grupo()
grupo5 = Grupo()

e1 = Empleado("Juan", "Lopez", 12345)
e2 = Empleado("Juan", "Lopez", 11)
e3 = Empleado("Juan", "Lopez", 1546)
e4 = Empleado("Juan", "Lopez", 14)
e5 = Empleado("Juan", "Lopez", 16)

grupo6 = Grupo([e1.cedula,e2.cedula,e3.cedula])

print(grupo1.toString())

print(grupo1.AddEmpleado(12345))
print(grupo1.toString())
print(grupo1.AddEmpleado(11))
print(grupo1.AddEmpleado(16))
print(grupo1.AddEmpleado(11))

print(grupo1.toString())
print(grupo6.toString())
