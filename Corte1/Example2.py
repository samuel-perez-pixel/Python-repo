def menu():
    print('1=sum')
    print('2=substract')
    print('3=multiply')
    print('4=division')
    answer=int(input("Please select an option: "))
    return answer
def main():
    print('Welcome to the new version of calculator')
    print('')
    name=input('Enter your name,please: ')
    flag="Yes"
    while flag=="Yes":

        option=menu()
        number1=float(input("Enter the first number: "))
        number2=float(input('Enter de second number: '))
        if option==1:
            result=number1+number2
        elif option==2:
            result=number1-number2
        elif option==3:
            result=number1*number2
        elif option==4:
            result=number1/number2
        else:
            result="Incorrect option"
        print("The result is: "+str(result))
        flag=input('Do you continue? Yes or not: ')
        print('')
    print('')
    print('')
    print('Thanks for using')
if __name__=="__main__":
    main()
