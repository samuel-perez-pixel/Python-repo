class Contacs:
    def __init__(self,id,name,phone,mail):
        self.id=id
        self.name=name
        self.phone=phone
        self.mail=mail
        self.status='A'
    def showContacs(self):
        print("")
        print("*********Contact Data*********")
        print("")
        print(f"Id: {self.id} \n Name: {self.name}\n Phone: {str(self.phone)}\n Mail: {self.mail}")
        print("")
        print("*******************************")
        print("")