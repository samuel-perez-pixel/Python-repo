class Tareas:
    __id_tarea : str
    __titulo : str
    __descripcion: str
    __fecha_creacion : str
    __fecha_finalizacion : str
    __status : str
    __id_desarrollador : str
    __cod_estado : str
    __cod_prioridad : str
    def __init__(self):
        self.__id_tarea = ''
        self.__titulo = ''
        self.__descripcion = ''
        self.__fecha_creacion = ''
        self.__fecha_finalizacion = ''
        self.__status = 'A'
        self.__id_desarrollador = ''
        self.__cod_estado = ''
        self.__cod_prioridad = ''
    
    def setIdTarea(self,varX):
        self.__id_tarea = varX
    
    def setTitulo(self,varX):
        self.__titulo = varX

    def setDescripcion(self,varX):
        self.__descripcion = varX

    def setFechaCreacion(self,varX):
        self.__fecha_creacion = varX

    def setFechaFinalizacion(self,varX):
        self.__fecha_finalizacion = varX

    def setStatus(self,varX):
        self.__status = varX

    def setIdDesarrollador(self,varX):
        self.__id_desarrollador = varX

    def setCodEstado(self,varX):
        self.__cod_estado = varX
    def setCodPrioridad(self,varX):
        self.__cod_prioridad = varX
        
    def getIdTarea(self):
        return self.__id_tarea
    def getTitulo(self):
        return self.__titulo
    def getDescripcion(self):
        return self.__descripcion
    def getFechaCreacion(self):
        return self.__fecha_creacion
    def getFechaFinalizacion(self):
        return self.__fecha_finalizacion
    def getStatus(self):
        return self.__status
    def getIdDesarrollador(self):
        return self.__id_desarrollador
    def getCodEstado(self):
        return self.__cod_estado
    def getCodPrioridad(self):
        return self.__cod_prioridad 