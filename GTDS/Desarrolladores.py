class Desarrolladores:
    __id_desarrollador : str
    __nombre : str
    __apellido : str
    __status : str

    def __init__(self):
        self.__id_desarrollador = ''
        self.__nombre = ''
        self.__apellido = ''
        self.__status = 'A'

    def setIdDesarrollador(self,varX):
        self.__id_desarrollador = varX  
    def setNombre(self,varX):
        self.__nombre = varX
    def setApellido(self,varX):
        self.__apellido = varX
    def setStatus(self,varX):
        self.__status = varX
    def getIdDesarrollador(self):
        return self.__id_desarrollador
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getStatus(self):
        return self.__status    