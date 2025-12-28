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
        self.cursor.execute(sql,(id_tarea),)
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

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    def desconectarDB(self):
        self.conn.close()   
        self.cursor.close()

    
    