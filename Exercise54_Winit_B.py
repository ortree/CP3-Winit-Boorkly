def login():
    username = input("Please fill username :")
    password = input("Please fill password :")
    if username == "warle" and password == "000":
        return True
    else:
        return False

def showMenu():
    print("Welcome to the Happy-Shop.....")
    print("-----Category List----- ")
    print("1. Cat :  9900 baht ")
    print("2. Dos :  12200 baht ")
    print("3. Rabbit :  3300 baht ")
    print("-----------------------")

def menuSeleceted():
    selectedItem = int(input("Select ur item number : "))
    amount = int(input("Fill Amount : "))
    price = 0
    if selectedItem == 1 or selectedItem == 2 or selectedItem == 3:
        if selectedItem == 1:
            itemName = "Cat"
            price = 9900
        if selectedItem == 2:
            itemName = "Dog"
            price = 12200
        if selectedItem == 3:
            itemName = "Rabbit"
            price = 3300
    else:
        print("no item number selected !")
        menuSeleceted()
    return [selectedItem,amount,price,itemName]

def vatCalculate(menuSelectedList):
    totalprice = (menuSelectedList[1] * menuSelectedList[2])
    netprice = ((totalprice * 7) / 100) + totalprice

    print("-----Bill------------------ ")
    print("1.", menuSelectedList[3], ": ", menuSelectedList[1], " netprice: ", netprice, " baht")
    print("-----****************------ ")

'''--------------------------Code------------------------------'''

print("Login to the Happy-Shop")
if login():
    showMenu()
    listOfMenu = menuSeleceted()
    vatCalculate(listOfMenu)
else:
    print("Username or Password  is incorrect")

'''--------------------------------------------------------'''