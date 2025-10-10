from Cl_Ticket import Ticket
ticket=[]

def menu():
    print("**********Menu**********")
    print("1. Add Ticket")
    print("2. Search Ticket")
    print("3. Modify Ticket")
    print("4. Delete Ticket")
    print("5. Exit")
    print("************************")
    option=int(input("Select an option: "))
    return option

def searchinList(fi):
    finded=False
    numberToSearch=fi
    for i in ticket:
        if i.numberTicket==numberToSearch:
            i.showTicket()
            finded=True
            break
    return finded

def modify():
    finded=False
    numberToSearch=input("Enter the ticket number to modify: ")
    for i in ticket:
        if i.numberTicket==numberToSearch:
            print("Enter new data")
            nameClient=input("Enter the client name: ")
            idClient=input("Enter the client ID: ")
            price=float(input("Enter the price: "))
            quantity=int(input("Enter the quantity: "))
            movieName=input("Enter the movie name: ")
            weekDay=input("Enter the week day: ")
            obj=Ticket(numberToSearch,nameClient,idClient,price,quantity,movieName,weekDay)
            ticket.remove(i)
            ticket.append(obj)
            print("")
            print("Ticket Modified")
            print("")
            finded=True
            break
    if not finded:
        print("")
        print("Ticket Not Found")
        print("")

def search():
    finded=False
    numberToSearch=input("Enter the ticket number to search: ")
    for i in ticket:
        if i.numberTicket==numberToSearch:
            i.showTicket()
            finded=True
            break
    if not finded:
        print("")
        print("Ticket Not Found")
        print("")

def readTicketData():
    print("Ticket Data:")
    print('Note: On Mondays there is a 50% discount on the ticket price and On Thursdays there is a 30% discount on the ticket price')
    print('')
    print('When search the ticket you will see the discounted price if the day is Monday or Thursday')
    print("")
    numberTicket=input("Enter the ticket number: ")
    nameClient=input("Enter the client name: ")
    idClient=input("Enter the client ID: ")
    price=float(input("Enter the price: "))
    quantity=int(input("Enter the quantity: "))
    movieName=input("Enter the movie name: ")
    weekDay=input("Enter the week day: ")
    if weekDay=="Monday" or weekDay=="monday":
        price=price-(price*(50/100))
    elif weekDay=="Thursday" or weekDay=="thursday":
        price=price-(price*(30/100))
    if not searchinList(numberTicket):
        obj=Ticket(numberTicket,nameClient,idClient,price,quantity,movieName,weekDay)
        ticket.append(obj)
        print("")
        print("Ticket Added")
        print("")
    else:
        print("")
        print("The ticket number already exists")
        print("")

def delete():
    finded=False
    numberToSearch=input("Enter the ticket number to delete: ")
    for i in ticket:
        if i.numberTicket==numberToSearch:
            ticket.remove(i)
            print("")
            print("Ticket Deleted")
            print("")
            finded=True
            break
    if not finded:
        print("")
        print("Ticket Not Found")
        print("")

def main():
    answer='yes'
    while answer=='yes' or answer=='Yes':
        Op=menu()
        if Op==1:
            readTicketData()
        elif Op==2:
            search()
        elif Op==3:
            modify()
        elif Op==4:
            delete()
        elif Op==5:
            print("Exiting the program...")
        else:
            print("Invalid option. Please try again.")
        print("")
        answer=input("Do you want to continue? Yes or No: ")
if __name__=="__main__":
    main()