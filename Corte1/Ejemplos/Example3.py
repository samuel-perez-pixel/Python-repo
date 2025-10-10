class Student:
    def __init__(self):
        self.name=''
        self.lastname=''
        self.age=0
    def showData(self):
        print('')
        print('student data:')
        print('Name: ',self.name)
        print('Lastname: ',self.lastname)
        print('\nAge: ',str(self.age))
def main():
    print("Welcome to the registry of a student")
    print('')
    objStudent=Student()
    answer='yes'
    while answer=='yes':
        objStudent.name=input('\nPlease enter the name of the student: ')
        objStudent.lastname=input('\nPlease enter the lastname of the student: ')
        objStudent.age=int(input("\nPlease enter the age: "))
        print('')
        objStudent.showData()
        answer=input("Another one? yes or not: ")
        print('End of the program')
        pass

if __name__=="__main__":
    main()
