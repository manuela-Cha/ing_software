from tkinter import *
from tkinter import messagebox


trabajadores_disponibles = ["A", "B", "C", "D", "E"]
vehiculos_disponibles = ["AAA", "ABB", "ACC"]


class Formar_Grupo_GUI(Tk):
    def __init__(self, *args,**kwargs):
        #Creacion ventana
        super().__init__(*args, **kwargs)
        self.title("Formación de grupos")
        self.geometry("500x500")

        #Boton de confirmacion
        self.confirm = Button(self, bg = "#AAA000", text="Confirmar selecciones", command=self.verificacion)

        #Valores para retornar las selecciones
        self.valores = [StringVar(self) for i in range(3)]
        self.valorVehiculo = StringVar(self)

        #Creacion frames de trabajadores
        for i in range(3):
            self.frameTrabajador(i)

        self.frameVehiculo = Frame(self, pady=10)
        self.vehiculoLabel = Label(self.frameVehiculo, text="Seleccione el vehículo a asignar")
        self.vehiculoOpciones = OptionMenu(self.frameVehiculo, self.valorVehiculo, *vehiculos_disponibles)

        self.vehiculoLabel.pack()
        self.vehiculoOpciones.pack()
        self.frameVehiculo.pack()

        self.confirm.pack()

        self.mainloop()

    #Funcion para crear la seleccion de trabajador
    def frameTrabajador(self, number):
        aux = Frame(self)
        auxLabel = Label(aux,text = "Trabajador "+str(number+1))
        auxOpciones = OptionMenu(aux, self.valores[number], *trabajadores_disponibles)
        auxLabel.grid(row=number,column = 0)
        auxOpciones.grid(row=number,column=1)
        aux.pack()
        return


    #Verificacion de criterios de aceptacion
    def verificacion(self):
        trabajadores_seleccionados = [self.valores[0].get(), self.valores[1].get(), self.valores[2].get()]
        vehiculo_seleccionado = self.valorVehiculo.get()
        print(trabajadores_seleccionados)

        #Verificacion de que se escogió vehículo
        if vehiculo_seleccionado == "":
            messagebox.showwarning("Error", "Por favor seleccione un vehículo")
            return

        #Verificacion de que todos los campos tengan trabajador
        if "" in trabajadores_seleccionados:
            messagebox.showwarning("Error", "Todos los trabajadores deben ser seleccionados, por favor verifique")
            return

        #Verificacion de que todos los trabajadores sean distintos
        if len(trabajadores_seleccionados) != len(set(trabajadores_seleccionados)):
            messagebox.showwarning("Error","Los trabajadores seleccionados deben ser distintos y todos deben estar asignados, por favor verifique")
            return
        
        
        

