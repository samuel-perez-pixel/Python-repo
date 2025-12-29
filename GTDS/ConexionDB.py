import psycopg2
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

class ConexionDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host =  'localhost',
            database = 'GTDS',
            user = 'postgres',
            password = 'post56',
            port = '5432'
        )
    def BuscarenDB(self,id_tarea):
        self.cursor=self.conn.cursor()
        sql='Select * from Tareas where id_tarea=%s'
        self.cursor.execute(sql,(id_tarea,))
        columna=self.cursor.fetchone()
        self.desconectarDB()
        return columna
        
    def AgregarTarea(self,tarea):
        try:
            self.cursor=self.conn.cursor()
            sql='Insert into Tareas VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            self.cursor.execute(sql,(
            tarea.getIdTarea(),
            tarea.getTitulo(),
            tarea.getDescripcion(),
            tarea.getFechaCreacion(),
            tarea.getFechaFinalizacion(),
            tarea.getStatus(),
            tarea.getIdDesarrollador(),
            tarea.getCodEstado(),
            tarea.getCodPrioridad()))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error","No se pudo agregar la tarea. Error: "+str(e))
        finally:
            self.desconectarDB()

   
    def LeerTareas(self,tree):
        self.cursor=self.conn.cursor()
        sql='Select * from Tareas order by id_tarea;'
        self.cursor.execute(sql)
        filas=self.cursor.fetchall()
        tree.delete(*tree.get_children())
        for fila in filas:
            tree.insert('',END,values=fila)
        self.desconectarDB()
   
    def ActualizarTareas(self,tarea):
        try:
            self.cursor=self.conn.cursor()
            sql='Update Tareas set titulo=%s,descripcion=%s,fecha_creacion=%s,fecha_finalizacion=%s,status=%s,id_desarrollador=%s,cod_estado=%s,cod_prioridad=%s where id_tarea=%s;'
            self.cursor.execute(sql,(
            tarea.getTitulo(),
            tarea.getDescripcion(),
            tarea.getFechaCreacion(),
            tarea.getFechaFinalizacion(),
            tarea.getStatus(),
            tarea.getIdDesarrollador(),
            tarea.getCodEstado(),
            tarea.getCodPrioridad(),
            tarea.getIdTarea()))
            self.conn.commit()
        except Exception as e:
            messagebox.showerror("Error","No se pudo actualizar la tarea. Error: "+str(e))
        finally:
            self.desconectarDB()
   
    def DesactivarTarea(self,id_tarea):
        try:
            self.cursor=self.conn.cursor()
            sql='Update Tareas set status=%s where id_tarea=%s;'
            self.cursor.execute(sql,('I',id_tarea))
            self.conn.commit()
        except Exception as e:
            messagebox.showerror("Error","No se pudo desactivar la tarea. Error: "+str(e))
        finally:
            self.desconectarDB()
    def ActivarTarea(self,id_tarea):
        try:
            self.cursor=self.conn.cursor()
            sql='Update Tareas set status=%s where id_tarea=%s;'
            self.cursor.execute(sql,('A',id_tarea))
            self.conn.commit()
        except Exception as e:
            messagebox.showerror("Error","No se pudo activar la tarea. Error: "+str(e))
        finally:
            self.desconectarDB()
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    def desconectarDB(self):
        self.conn.close()   
        self.cursor.close()

    
    