class Ticket:
    def __init__(self,numberTicket,nameClient,idClient,price,quantity,movieName,weekDay):
        self.numberTicket=numberTicket
        self.nameClient=nameClient
        self.idClient=idClient
        self.price=price
        self.quantity=quantity
        self.movieName=movieName
        self.weekDay=weekDay

    def showTicket(self):
        print("")
        print("*********Ticket Data*********")
        print("")
        print(f"Number Ticket: {self.numberTicket}\n Name Client: {self.nameClient}\n Id Client: {self.idClient}\n Price: {str(self.price)}\n Quantity: {str(self.quantity)}\n Movie Name: {self.movieName} \n Week Day: {self.weekDay}")
        print("")
        print("*******************************")
        print("")