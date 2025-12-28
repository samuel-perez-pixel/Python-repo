class Estados:
    __cod_estado: str
    __nombre_estado: str

    def __init__(self):
        self.__cod_estado=''
        self.__nombre_estado=''
    
    def setCodEstado(self,varX):
        self.__cod_estado=varX
    def setNombreEstado(self,varX):
        self.__nombre_estado=varX
    def getCodEstado(self):
        return self.__cod_estado
    def getNombreEstado(self):
        return self.__nombre_estado