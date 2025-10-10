from Cl_Task  import Task

task=[]
def menu():
    print('--------Task Menu---------')
    print('')
    print('1= Add Task')
    print('2= View Tasks')
    print('3= Search Task')
    print('4= Modify Task')
    print('5= Delete Task')
    print('6= Exit')
    Option=int(input('Selec an Option: '))
    return Option

def searchInlist(fi):
    finded=True
    parameterTosearch=fi
    for i in task:
        if i.id==parameterTosearch or i.description==parameterTosearch:
            i.showTask()
            finded=True
    return finded

def search():
    finded=False
    parameterTosearch=input('Please enter the task id or description:')
    for i in task:
        if i.id==parameterTosearch or i.description==parameterTosearch:
            if i.internalSate=='A':
                i.showTask()
            else:
                print('Task inactive ')
                print('')
                react=input('Wanna reactivate this task? Yes or No:')
                if react=='Yes' or react=='yes':
                    obj=i
                    obj.internalState='A'
                    task.remove(obj)
                    task.append(obj)
                    print('')
                    print('Sucessfully reactivation')
                    finded=True
                break
            if not finded:
                print('')
                print('Error!!! The Task not Exist!!!')
                print('')

def readTaskData():
    print('Task Data: ')
    print('')
    idT=input('Enter the Id: ')
    descrip=input('Enter the description: ')
    prio=input('Enter the priority: ')
    stat=input('Enter the status(finished,started,pending): ')
    if not searchInlist(idT):
        obj =Task(idT,descrip,prio,stat)
        task.append(obj)
        print('')
        print('/////Task loaded sucesfully/////')
    else:
        print('')
        print('The Task already exist')
        print('')

def modify():
    print('Now gonna modify your task data')
    print('')
    parameterTosearch=input('Please enter the task id or description: ')
    for i in task:
        if i.id==parameterTosearch or i.description==parameterTosearch:
            i.showTask()
            print('')
            task.remove(i)
            name=input('Enter the new name: ')
            prio=input('Enter the new priority: ')
            stat=input('Enter the new status: ')
            obj=Task(i.id,name,prio,stat)
            task.append(obj)
            print('')
            obj.showTask()
            print('')
            print('Task modified sucesfully')

def delete():
    print('Now gonna delete your task')
    print('')
    idD=input('Enter Id to delete the task: ')
    for i in task:
        if i.id==idD:
            i.showTask()
            obj=i
            obj.internalState='I'
            task.remove(obj)
            task.append(obj)
            print('')
            print('Task deleted sucesfully')
            finded=True
            break
        if not finded:
            print('')
            print('Task no exist ')
            print('')

def viewTasks():
    print('Your Tasks: ')
    print('')
    for i in task:
        number=1
        if i.internalState=='A':
            i.showTask()
            print('Task number# '+str(number))
            number+=1
        else:
            print('No tasks to show')
            print('')

def main():
    answer='Yes'
    while answer=='Yes' or answer=='yes':
        option=menu()
        if option==1:
            readTaskData()
        elif option==2:
            viewTasks()
        elif option==3:
            search()
        elif option==4:
            modify()
        elif option==5:
            delete()
        elif option==6:
            print('Thank you for using our system')
            answer='No'
        else:
            print('Error!!! Please select a correct option')
        if answer!='No':
            answer=input('Do you want to continue? Yes or No: ')

if __name__=='__main__':
    main()

            