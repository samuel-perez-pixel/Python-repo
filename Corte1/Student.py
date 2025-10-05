class  Student:
    def __init__(self, notaQuimica,notaCalculo,notaFisica):
        self.notaQuimica=notaQuimica
        self.notaCalculo=notaCalculo
        self.notaFisica=notaFisica

        def showNotes(self):
            print('')
            print('--------------student qulifications-------------------')
            print('')
            print(f"Chemistry: {str(self.notaQuimica)} \n Calculus: {str(self.notaCalculo)}\n Physic: {str(self.notaFisica)}")
            print('')
