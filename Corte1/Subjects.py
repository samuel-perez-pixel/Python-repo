class  Subjects:
    def __init__(self, name, note):
        self.name=name
        self.note=note
        self.status='A'

    def showSubject(self):
        print("")
        print("*********Subject Data*********")
        print("")
        print(f"Name: {self.name}\n Note: {str(self.note)}")
        print("")
        print("*******************************")
        print("")