from Contacs import Contacs
contacs=[]

def menu():
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Modify Contact")
    print("5. Delete Contact")
    print("6. Exit")
    option = int(input("Please select a choice: "))
    return option

def search():
    finded=False
    parameterTosearch=input("Please enter the contact name or phone: ")
    for i in contacs:
        if i.name==parameterTosearch or i.phone==parameterTosearch:
            if i.status=='A':
                i.showContacs()
            else :
                print('Contact Inactive')
                answer=input('Do you wanna reactive the contact? Yes or No:  ')
                if answer=="Yes":
                    obj=i
                    obj.status='A'
                    contacs.remove(i)
                    contacs.append(obj)
                    print('')
                    print('The contact has been reactivated')
            finded=True
            break
    if not finded:
        print("")
        print("Error!!! The Contact not Exist!!!")
        print("")

def searchinList(fi):
    finded=False
    parameterTosearch=fi
    for i in contacs:
        if i.name==parameterTosearch or i.phone==parameterTosearch:
            i.showContact()
            finded=True
            break
    return finded

def readContacData():
    print('contact data: ')
    print('')
    idC=input('Enter the Id: ')
    name=input('Enter the name: ')
    phone=input('Enter the phone: ')
    mail=input('Enter the mail: ')
    if not searchinList(idC):
        obj=Contacs(idC,name,phone,mail)
        contacs.append(obj)
        print('')
        print('The contact has been added')
        print('')
    else:
        print('')
        print('The contact already exists')
        print('')

def modify():
    print('Modifying contact')
    print('')
    parameterTosearch=input('Please enter the contact name or phone to modify: ')
    for i in contacs:
        if i.name==parameterTosearch or i.phone==parameterTosearch:
            i.showContacs()
            contacs.remove(i)
            phone=input('Enter the new phone: ')
            mail=input('Enter the new mail: ')
            obj=Contacs(i.id,i.name,phone,mail)
            contacs.append(obj)
            print('')
            print('The contact has been modified')
            finded=True
            break
        else:
            print('')
            print('Error!!! The Contact not Exist!!!')
            print('')

def logicalDelete():
    print('Deleting contact')
    print('')
    parameterTosearch=input('Please enter the contact name or phone to delete: ')
    for i in contacs:
        if i.name==parameterTosearch or i.phone==parameterTosearch:
            i.showContacs()
            print('')
            obj=i
            i.status='I'
            contacs.remove(obj)
            contacs.append(obj)
            print('')
            print('The contact has been deleted')
            finded=True
            break
    if not finded:
        print("")
        print("Error!!! The Contact not Exist!!!")
        print("")

def showAllContacts():
    number=1
    for i in contacs:
        print('Contact number #'+str(number))
        i.showContacs()
        number+=1

def main():
    answer='Yes'
    while answer=='Yes' or answer=='yes':
        op=menu()
        if op==1:
            readContacData()
        elif op==2:
            showAllContacts()
        elif op==3:
            search()
        elif op==4:
            modify()
        elif op==5:
            logicalDelete()
        elif op==6:
            print('Thank you for using our system')
            answer='No'
        else:
            print('Error!!! Please select a correct option')
        if answer!='No':
            answer=input('Do you want to continue? Yes or No: ')

if __name__=="__main__":
    main()
#