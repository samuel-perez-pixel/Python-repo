from Subjects import Subjects

subjects=[] # List to store student objects
def menu():
    print("Menu")
    print("")
    print("1 - Add Subject ")
    print("2 - Search Subject")
    print("3 - Modify Subject")
    print("4 - Delete Subject")
    print("5 - Show List")
    print("6 - Show Aproved Subjects")
    print("7 - Exit")
    print("")
    option = int(input("Please select a choice: "))
    print("")
    return option

def search():
    finded= False
    nameToSearch = input("Please enter the subject name: ")
    for item in subjects:
        if item.name==nameToSearch:
            if item.status=='A':
                item.showSubject()
            else:
                print('Inactive Subject')
                answer=input('Do you want to reactive the subject? Yes or No:  ')
                if answer=='Yes':
                    obj=item
                    obj.status='A'
                    subjects.remove(item)
                    subjects.append(obj)
                    print('')
                    print('The subject has been reactivated')
            finded=True
            break
def searchinList(fi):
    finded = False
    nameToSearch = fi
    for item in subjects:
        if item.name==nameToSearch:
            item.showSubject()
            finded=True
            break
    return finded

def readSubjectData():
    print("Subject Data:")
    print("")
    name = input("Enter the name: ")
    note = float(input("Enter the note: "))
    if not searchinList(name):
        obj=Subjects(name,note)
        subjects.append(obj)
        print("")
        print("Subject Added")
        print("")
    else:
        print("")
        print("Error!!! The Subject already exist!!!")
        print("")

def modify():
    print ("Modify Subject")
    print("")
    name = input("Please enter the subject name to modify: ")
    for item in subjects:
        if item.name==name:
            item.showSubject()
            subjects.remove(item)
            note = float(input("Enter the new note: "))
            objSubject=Subjects(name,note)
            subjects.append(objSubject)
            print("")
            print("Subject Modified")
            finded=True
            break
    if not finded:
        print("")
        print("Error!!! The Subject not Exist!!!")
        print("")

def logicalDelete():
    print('Delete Subject')
    print('')
    name=input('Enter the subject name to delete: ')
    for item in subjects:
        if  item.name==name:
            item.showSubject()
            item.status='I'
            print('')
            print('The subject has been deleted')
            finded=True
            break
    if not finded:
        print("")
        print("Error!!! The Subject not Exist!!!")
        print("")

def showList():
    print("Subject List")
    print("")
    for item in subjects:
        if item.status=='A':
            item.showSubject()
    print("End of List")
    print("")

def  showAproved():
    number=1
    for item in subjects:
        if item.note>=48 and item.status=='A':
            print('Aproved Subject number #'+str(number))
            item.showSubject()
            number+=1
def main():
    answer='yes'
    while answer =='yes':
        op=menu()
        if op==1:
            readSubjectData()
        elif op==2:
            search()
        elif op==3:
            modify()
        elif op==4:
            logicalDelete()
        elif op==5:
            showList()
        elif op==6:
            showAproved()    
        elif op==7:
            print("Exit")
        else:
            print("Error!!! Invalid Option")
        print("")
        answer=input('Wanna keep going? yes or no ')
if __name__=='__main__':
    main()


