from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class GestorGruposRutas:
    def __init__(self):
        self.archivo_grupos = "Nomina_ing_software/archivos_de_texto/Grupos.txt"
        self.archivo_rutas = "Nomina_ing_software/archivos_de_texto/Rutas.txt"

    def verificar_grupos(self):
        try:
            with open(self.archivo_grupos, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read().strip()
                if not contenido:
                    return False
                return True
        except FileNotFoundError:
            return False

    def verificar_rutas_disponibles(self):
        try:
            with open(self.archivo_rutas, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    if "Por_cubrir" in linea:
                        return True
                return False
        except FileNotFoundError:
            return False

    def verificar_estado_sistema(self):
        hay_grupos = self.verificar_grupos()
        if not hay_grupos:
            return "No hay grupos creados."

        grupos_disponibles = self.obtener_grupos()
        if not grupos_disponibles:
            return "No hay grupos disponibles."

        hay_rutas_disponibles = self.verificar_rutas_disponibles()
        if not hay_rutas_disponibles:
            return "Todas las rutas están cubiertas."
        
        return "Hay grupos y rutas disponibles."

    def obtener_grupos(self):
        grupos = []
        try:
            with open(self.archivo_grupos, 'r', encoding='utf-8') as archivo:
                grupo_actual = []
                es_disponible = False
                
                for linea in archivo:
                    linea_strip = linea.strip()
                    if linea_strip == "-" * 50:
                        if grupo_actual and es_disponible:
                            grupos.append('\n'.join(grupo_actual))
                        grupo_actual = []
                        es_disponible = False
                    else:
                        grupo_actual.append(linea_strip)
                        if linea_strip == "Estado: Disponible":
                            es_disponible = True
                
                if grupo_actual and es_disponible:
                    grupos.append('\n'.join(grupo_actual))
        except FileNotFoundError:
            return []
        return grupos

    def obtener_rutas(self):
        rutas = []
        try:
            with open(self.archivo_rutas, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    partes = linea.strip().split()
                    nombre_ruta = partes[0]
                    estado = partes[1]
                    equipo = ' '.join(partes[2:]) if len(partes) > 2 else '_'
                    rutas.append((nombre_ruta, estado, equipo))
        except FileNotFoundError:
            return []
        return rutas

    def obtener_integrantes_grupo(self, grupo_texto):
        integrantes = []
        for linea in grupo_texto.split('\n'):
            if '(CC:' in linea and ')' in linea:
                integrantes.append(linea.strip())
        return integrantes

    def grupo_ya_asignado(self, grupo_texto):
        integrantes = self.obtener_integrantes_grupo(grupo_texto)
        if not integrantes:
            return False
        
        try:
            with open(self.archivo_rutas, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    if "Cubierta" in linea:
                        partes = linea.strip().split()
                        equipo = ' '.join(partes[2:]) if len(partes) > 2 else ''
                        for integrante in integrantes:
                            if integrante in equipo:
                                return True
        except FileNotFoundError:
            return False
        return False

    def asignar_grupo_a_ruta(self, nombre_ruta, grupo_texto):
        try:
            if self.grupo_ya_asignado(grupo_texto):
                raise ValueError("Este grupo ya está asignado a otra ruta.")

            integrantes = self.obtener_integrantes_grupo(grupo_texto)
            if not integrantes:
                raise ValueError("No se encontraron integrantes en el grupo seleccionado")

            integrantes_str = "-".join(integrantes)
            with open(self.archivo_rutas, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()

            with open(self.archivo_rutas, 'w', encoding='utf-8') as archivo:
                for linea in lineas:
                    if linea.startswith(nombre_ruta):
                        nueva_linea = f"{nombre_ruta} Cubierta {integrantes_str}\n"
                        archivo.write(nueva_linea)
                    else:
                        archivo.write(linea)

            return True
        except Exception as e:
            raise Exception(f"Error al asignar grupo a ruta: {str(e)}")

class GestorGruposRutasGUI:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Gestión de Grupos y Rutas")
        self.ventana.geometry("1000x600")
        self.gestor = GestorGruposRutas()
        
        frame_superior = Frame(self.ventana, pady=20)
        frame_superior.pack(fill='x')
        
        Label(frame_superior, text="Estado del Sistema", font=('Arial', 14, 'bold')).pack()
        self.label_estado = Label(frame_superior, text="", font=('Arial', 12))
        self.label_estado.pack(pady=10)
        
        frame_principal = Frame(self.ventana)
        frame_principal.pack(expand=True, fill='both', padx=20)
        
        frame_grupos = LabelFrame(frame_principal, text="Grupos Disponibles", padx=10, pady=10)
        frame_grupos.pack(side=LEFT, expand=True, fill='both', padx=(0,10))
        
        self.lista_grupos = Listbox(frame_grupos, width=50, height=15, exportselection=0)
        self.lista_grupos.pack(expand=True, fill='both')
        
        frame_asignacion = Frame(frame_principal)
        frame_asignacion.pack(side=LEFT, padx=10)
        
        # Guardamos el botón como atributo para poder modificarlo
        self.boton_asignar = Button(frame_asignacion, text="Asignar >>", 
                                   command=self.asignar_grupo_ruta, width=15)
        self.boton_asignar.pack(pady=10)
        
        frame_rutas = LabelFrame(frame_principal, text="Rutas", padx=10, pady=10)
        frame_rutas.pack(side=LEFT, expand=True, fill='both')
        
        self.lista_rutas = Listbox(frame_rutas, width=50, height=15, exportselection=0)
        self.lista_rutas.pack(expand=True, fill='both')
        
        frame_botones = Frame(self.ventana, pady=20)
        frame_botones.pack()
        
        Button(frame_botones, text="Actualizar Todo", 
               command=self.actualizar_todo, width=15).pack(side=LEFT, padx=5)
        
        Button(frame_botones, text="Salir", 
               command=self.ventana.quit, width=15).pack(side=LEFT, padx=5)
        
        self.grupos_dict = {}
        self.rutas_dict = {}
        
        self.actualizar_todo()
        
        self.ventana.mainloop()
    
    def actualizar_todo(self):
        self.actualizar_estado()
        self.mostrar_grupos()
        self.mostrar_rutas()
    
    def actualizar_estado(self):
        estado = self.gestor.verificar_estado_sistema()
        self.label_estado.config(text=estado)
        
        if "No hay grupos creados" in estado:
            self.label_estado.config(fg='red')
            self.boton_asignar.config(state='disabled')  # Deshabilitar botón
        elif "No hay grupos disponibles" in estado:
            self.label_estado.config(fg='red')
            self.boton_asignar.config(state='disabled')  # Deshabilitar botón
        elif "Todas las rutas están cubiertas" in estado:
            self.label_estado.config(fg='orange')
            self.boton_asignar.config(state='disabled')  # Deshabilitar botón
        else:
            self.label_estado.config(fg='green')
            self.boton_asignar.config(state='normal')  # Habilitar botón
    
    def mostrar_grupos(self):
        self.lista_grupos.delete(0, END)
        self.grupos_dict.clear()
        grupos = self.gestor.obtener_grupos()
        
        if not grupos:
            self.lista_grupos.insert(END, "No hay grupos disponibles")
            return
            
        for i, grupo in enumerate(grupos):
            fecha = "Sin fecha"
            for linea in grupo.split('\n'):
                if "GRUPO CREADO EN FECHA:" in linea:
                    fecha = linea.split(": ")[1]
                    break
            
            display_text = f"Grupo {i+1} (Creado: {fecha})"
            self.lista_grupos.insert(END, display_text)
            self.grupos_dict[display_text] = grupo
    
    def mostrar_rutas(self):
        self.lista_rutas.delete(0, END)
        self.rutas_dict.clear()
        rutas = self.gestor.obtener_rutas()
        
        if not rutas:
            self.lista_rutas.insert(END, "No hay rutas registradas")
            return
            
        for nombre, estado, equipo in rutas:
            if estado == "Por_cubrir":
                display_text = f"{nombre} ({estado})"
                self.lista_rutas.insert(END, display_text)
                self.rutas_dict[display_text] = nombre
    
    def asignar_grupo_ruta(self):
        grupo_sel = self.lista_grupos.curselection()
        ruta_sel = self.lista_rutas.curselection()
        
        if not grupo_sel or not ruta_sel:
            messagebox.showwarning("Selección requerida", "Por favor, seleccione un grupo y una ruta")
            return
        
        grupo_texto = self.grupos_dict[self.lista_grupos.get(grupo_sel[0])]
        ruta_nombre = self.rutas_dict[self.lista_rutas.get(ruta_sel[0])]
        
        try:
            self.gestor.asignar_grupo_a_ruta(ruta_nombre, grupo_texto)
            messagebox.showinfo("Éxito", "Grupo asignado correctamente a la ruta")
            self.actualizar_todo()
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = GestorGruposRutasGUI()