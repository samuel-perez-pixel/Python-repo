class Prioridades:
    __cod_prioridad: str
    __nombre_prioridad: str
    def __init__(self):
        self.__cod_prioridad=''
        self.__nombre_prioridad=''
    def setCodPrioridad(self,varX):
        self.__cod_prioridad=varX
    def setNombrePrioridad(self,varX):
        self.__nombre_prioridad=varX
    def getCodPrioridad(self):
        return self.__cod_prioridad
    def getNombrePrioridad(self):
        return self.__nombre_prioridad