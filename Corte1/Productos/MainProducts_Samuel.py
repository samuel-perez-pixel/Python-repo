#Ejemplo de CRUD de Productos
#Clase principal
from Products import Products

productList = [] #Empty List

def menu():
    print("Menu")
    print("")
    print("1 - Add Product")
    print("2 - Search Product")
    print("3 - Modify Product")
    print("4 - Delete Product")
    print("5 - Show List")
    print("6 - Exit")
    print("")
    option = int(input("Please select a choice: "))
    print("")
    return option

def search():
    finded = False
    idtoSearch = input("Please enter the product id: ")
    for item in productList:
        if item.id==idtoSearch:
            if item.status=='A':
                item.showData()
            else:
                print('Inactive Product')
                answer=input('Do you want to reactive the product? Yes or No:  ')
                if answer=='Yes':
                    obj=item
                    obj.status='A'
                    productList.remove(item)
                    productList.append(obj)
                    print('')
                    print('The product has been reactivated')
            finded=True
            break
    if not finded:
        print("")
        print("Error!!! The Id not Exist!!!")
        print("")

def searchinList(fi):
    finded = False
    idtoSearch = fi
    for item in productList:
        if item.id==idtoSearch:
            item.showData()
            finded=True
            break
    return finded

def readProductData():
    print("Product Data:")
    print("")
    idP = input("Enter the Id: ")
    name = input("Enter the name: ")
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    if not searchinList(idP):
        objProduct = Products(idP, name, price,quantity)
        productList.append(objProduct)
        objProduct.showData()
        print("")
        print("Data Loaded!!!!")
    else:
        print("")
        print("Data already exist!!!")
        print("")
    print("")
def modify():
    print('Modify product data')
    print('')
    idp=input('Enter the id: ')
    for item in productList:
        if  item.id==idp:
            item.showData()
            productList.remove(item)
            print('')
            name = input("Enter the name: ")
            price = float(input("Enter the price: "))
            quantity = int(input("Enter the quantity: "))
            objProduct = Products(idp, name, price,quantity)
            productList.append(objProduct)
            print('')
            objProduct.showData()
            print('')
            print('Data Modified')
            finded=True
            break
    if not finded:
        print("")
        print("Error!!! The Id not Exist!!!")
        print("")

def delete():
    print('Delete  product data')
    print('')
    idp=input('Enter the id: ')
    for item in productList:
        if  item.id==idp:
            item.showData()
            print('')
            productList.remove(item)
            print('')
            finded=True
            print('Data removed')
            break
    if not finded:
        print("")
        print("Error!!! The Id not Exist!!!")
        print("")

def showList():
    number=1
    for item in productList:
        print('Product number #'+str(number))
        item.showData()
        number+=1

def logicalElimination():
    print('Delete product data')
    print('')
    idP = input("Enter the Id : ")
    for item in productList:
        if item.id==idP:
            item.showData()
            print('')
            obj=item
            obj.status='I'
            productList.remove(item)
            productList.append(obj)
            print('')
            print("Data Deleted!!!!")
            finded=True
            break
    if not finded:
        print("")
        print("Error!!! The Id not Exist!!!")
        print("")

def main():
    answer = "Yes"
    while answer=="Yes":
        op = menu()
        if op==1: #Add Product
            readProductData()
        elif op==2: #Search Product
            search()                
        elif op==3: #Modify Product
            modify()
        elif op==4: #Delete Product
            logicalElimination()
        elif op==5: #ShowList
            showList()
        elif op==6: #Exit
            print("End of the Program!!!")
            break
        else:
            print("Error! Option not valid!")
            print("")
        answer = input("Do you wish continue? Yes or no: ")

if __name__=="__main__":
    main()


