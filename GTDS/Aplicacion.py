import tkinter as tk
from tkinter import ttk, messagebox
from ConexionDB import ConexionDB

class Aplicacion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GTDS - Tareas")
        
        # ========== CAMPOS REQUERIDOS ==========
        
        # ID Tarea
        self.labelIdTarea = tk.Label(self.window, text="ID Tarea:")
        self.labelIdTarea.place(x=10, y=10)
        self.entryIdTarea = tk.Entry(self.window, width=20)
        self.entryIdTarea.place(x=80, y=10)

        # Título
        self.labelTitulo = tk.Label(self.window, text="Título:")
        self.labelTitulo.place(x=10, y=40)
        self.entryTitulo = tk.Entry(self.window, width=20)
        self.entryTitulo.place(x=80, y=40)

        # Descripción
        self.labelDescripcion = tk.Label(self.window, text="Descripción:")
        self.labelDescripcion.place(x=10, y=70)
        self.entryDescripcion = tk.Entry(self.window, width=20)
        self.entryDescripcion.place(x=80, y=70)
        
        # Fecha Creación
        self.labelFechaCreacion = tk.Label(self.window, text="Fecha Creación:")
        self.labelFechaCreacion.place(x=10, y=100)
        self.entryFechaCreacion = tk.Entry(self.window, width=20)
        self.entryFechaCreacion.place(x=100, y=100)
        
        # Fecha Finalización
        self.labelFechaFinalizacion = tk.Label(self.window, text="Fecha Final:")
        self.labelFechaFinalizacion.place(x=10, y=130)
        self.entryFechaFinalizacion = tk.Entry(self.window, width=20)
        self.entryFechaFinalizacion.place(x=100, y=130)
        
        # ========== COMBOBOX PARA PRIORIDAD ==========
        self.labelPrioridad = tk.Label(self.window, text="Prioridad:")
        self.labelPrioridad.place(x=10, y=160)
        self.comboPrioridad = ttk.Combobox(self.window, state="readonly", width=20)
        self.comboPrioridad.place(x=80, y=160)
        
        # ========== COMBOBOX PARA ESTADO ==========
        self.labelEstado = tk.Label(self.window, text="Estado:")
        self.labelEstado.place(x=10, y=190)
        self.comboEstado = ttk.Combobox(self.window, state="readonly", width=20)
        self.comboEstado.place(x=80, y=190)
        
        # ========== COMBOBOX PARA DESARROLLADOR ==========
        self.labelDesarrollador = tk.Label(self.window, text="Desarrollador:")
        self.labelDesarrollador.place(x=10, y=220)
        self.comboDesarrollador = ttk.Combobox(self.window, state="readonly", width=20)
        self.comboDesarrollador.place(x=100, y=220)
        
        # ========== BOTONES ==========
        self.buttonSearch = tk.Button(self.window, text="Search", command=self.search, width=8)
        self.buttonSearch.place(x=250, y=10)
        
        self.buttonAdd = tk.Button(self.window, text="Add", command=self.Add, width=8)
        self.buttonAdd.place(x=250, y=40)
        
        self.buttonModify = tk.Button(self.window, text="Modify", command=self.Modify, width=8)
        self.buttonModify.place(x=250, y=70)
        
        self.buttonDelete = tk.Button(self.window, text="Delete", command=self.searchDelete, width=8)
        self.buttonDelete.place(x=250, y=100)
        
        self.buttonClear = tk.Button(self.window, text="Clear", command=self.clear, width=8)
        self.buttonClear.place(x=250, y=130)
        
        self.buttonCargarCombos = tk.Button(self.window, text="Cargar Combos", command=self.cargarCombos, width=10)
        self.buttonCargarCombos.place(x=240, y=160)

        self.window.geometry("350x300")
        
        # Cargar combos al iniciar
        self.cargarCombos()
        
        self.window.mainloop()
    
    def cargarCombos(self):
        """Carga los combos desde BD MOSTRANDO ID y NOMBRE"""
        try:
            db = ConexionDB()
            db.cursor = db.conn.cursor()
            
            # PRIORIDADES: "CÓDIGO - Nombre"
            db.cursor.execute("SELECT cod_prioridad, nombre_prioridad FROM Prioridades ORDER BY nombre_prioridad")
            prioridades = [f"{fila[0]} - {fila[1]}" for fila in db.cursor.fetchall()]
            self.comboPrioridad['values'] = prioridades
            if prioridades:
                self.comboPrioridad.current(0)
            
            # ESTADOS: "CÓDIGO - Nombre"
            db.cursor.execute("SELECT cod_estado, nombre_estado FROM Estados ORDER BY nombre_estado")
            estados = [f"{fila[0]} - {fila[1]}" for fila in db.cursor.fetchall()]
            self.comboEstado['values'] = estados
            if estados:
                self.comboEstado.current(0)
            
            # DESARROLLADORES: "ID - Nombre Apellido"
            db.cursor.execute("SELECT id_desarrollador, nombre, apellido FROM Desarrolladores WHERE status='A' ORDER BY apellido")
            desarrolladores = [f"{fila[0]} - {fila[1]} {fila[2]}" for fila in db.cursor.fetchall()]
            self.comboDesarrollador['values'] = desarrolladores
            if desarrolladores:
                self.comboDesarrollador.current(0)
            
            db.cursor.close()
            db.desconectarDB()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error cargando combos: {str(e)}")
    
    def loadinWindow(self):
        """Crea objeto Tarea EXTRACTING IDs from combos"""
        from Tareas import Tareas
        
        objTarea = Tareas()
        objTarea.setIdTarea(self.entryIdTarea.get().strip())
        objTarea.setTitulo(self.entryTitulo.get().strip())
        objTarea.setDescripcion(self.entryDescripcion.get().strip())
        objTarea.setFechaCreacion(self.entryFechaCreacion.get().strip())
        objTarea.setFechaFinalizacion(self.entryFechaFinalizacion.get().strip())
        objTarea.setStatus("A")  # Siempre Activo al crear
        
        # EXTRAER ID DESARROLLADOR (formato: "DEV001 - Juan Pérez")
        if self.comboDesarrollador.get():
            id_desarrollador = self.comboDesarrollador.get().split(" - ")[0].strip()
            objTarea.setIdDesarrollador(id_desarrollador)
        else:
            return None
        
        # EXTRAER CÓDIGO ESTADO (formato: "TODO - To Do")
        if self.comboEstado.get():
            cod_estado = self.comboEstado.get().split(" - ")[0].strip()
            objTarea.setCodEstado(cod_estado)
        else:
            return None
        
        # EXTRAER CÓDIGO PRIORIDAD (formato: "ALTA - Alta")
        if self.comboPrioridad.get():
            cod_prioridad = self.comboPrioridad.get().split(" - ")[0].strip()
            objTarea.setCodPrioridad(cod_prioridad)
        else:
            return None
        
        return objTarea
    
    def searchinDB(self):
        code = self.entryIdTarea.get().strip()
        db = ConexionDB()
        row = db.BuscarenDB(code)
        return row
    
    def Add(self):
        """Agrega nueva tarea CON VALIDACIÓN"""
        # Validar
        if not self.entryIdTarea.get().strip():
            messagebox.showwarning("Validación", "ID Tarea requerido")
            return
        
        if not self.entryTitulo.get().strip():
            messagebox.showwarning("Validación", "Título requerido")
            return
        
        if not self.comboDesarrollador.get():
            messagebox.showwarning("Validación", "Seleccione desarrollador")
            return
        
        if not self.comboEstado.get():
            messagebox.showwarning("Validación", "Seleccione estado")
            return
        
        if not self.comboPrioridad.get():
            messagebox.showwarning("Validación", "Seleccione prioridad")
            return
        
        # Verificar si existe
        row = self.searchinDB()
        if row:
            messagebox.showwarning("Error", "Ya existe ese ID")
            return
        
        # Crear y agregar
        objTarea = self.loadinWindow()
        if objTarea:
            try:
                objConn = ConexionDB()
                objConn.AgregarTarea(objTarea)
                messagebox.showinfo('Éxito!', 'Tarea agregada!')
                self.clear()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
    
    def search(self):
        """Busca tarea"""
        code = self.entryIdTarea.get().strip()
        if not code:
            messagebox.showwarning("Validación", "Ingrese ID")
            return
        
        objConn = ConexionDB()
        row = objConn.BuscarenDB(code)
        
        if row:
            self.clear()
            self.entryIdTarea.insert(0, row[0])
            self.entryTitulo.insert(0, row[1])
            self.entryDescripcion.insert(0, row[2])
            self.entryFechaCreacion.insert(0, row[3])
            self.entryFechaFinalizacion.insert(0, row[4])
            
            # Aquí deberías cargar los combos también
            if row[5] == 'I':
                response = messagebox.askyesno("Inactivo", "¿Reactivar?")
                if response:
                    objConn.ActivarTarea(code)
                    messagebox.showinfo("Info", "¡Reactivado!")
                self.clear()
        else:
            messagebox.showerror("Error", "No encontrado")
            self.clear()
    
    def clear(self):
        """Limpia campos"""
        self.entryIdTarea.delete(0, tk.END)
        self.entryTitulo.delete(0, tk.END)
        self.entryDescripcion.delete(0, tk.END)
        self.entryFechaCreacion.delete(0, tk.END)
        self.entryFechaFinalizacion.delete(0, tk.END)
        
        if self.comboPrioridad['values']:
            self.comboPrioridad.current(0)
        if self.comboEstado['values']:
            self.comboEstado.current(0)
        if self.comboDesarrollador['values']:
            self.comboDesarrollador.current(0)
    
    def Modify(self):
        """Modifica tarea"""
        if not self.entryIdTarea.get().strip():
            messagebox.showwarning("Validación", "Busque primero")
            return
        
        objTarea = self.loadinWindow()
        if objTarea:
            objConn = ConexionDB()
            objConn.ActualizarTareas(objTarea)
            messagebox.showinfo("Info", "¡Modificado!")
            self.clear()
    
    def searchDelete(self):
        """Desactiva tarea"""
        code = self.entryIdTarea.get().strip()
        if not code:
            messagebox.showwarning("Validación", "Ingrese ID")
            return
        
        objConn = ConexionDB()
        row = objConn.BuscarenDB(code)
        
        if row:
            self.clear()
            self.entryIdTarea.insert(0, row[0])
            self.entryTitulo.insert(0, row[1])
            self.entryDescripcion.insert(0, row[2])
            self.entryFechaCreacion.insert(0, row[3])
            self.entryFechaFinalizacion.insert(0, row[4])
            
            if row[5] == 'A':
                response = messagebox.askyesno("Confirmar", "¿Desactivar?")
                if response:
                    objConn.DesactivarTarea(code)
                    messagebox.showinfo("Info", "¡Desactivado!")
                self.clear()
            else:
                messagebox.showinfo("Info", "Ya inactiva")
        else:
            messagebox.showwarning("Error", "No encontrado")

if __name__ == "__main__":
    app = Aplicacion()