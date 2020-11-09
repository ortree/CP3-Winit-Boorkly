from setuptools.command.test import test

print("Login to the Happy-Shop")
username = input("Please fill username :")
password = input("Please fill password :")
if username == "warle" and password == "000":
    print("Welcome to the Happy-Shop.....")
    print("-----Category List----- ")
    print("1. Cat :  9900 baht ")
    print("2. Dos :  12200 baht ")
    print("3. Rabbit :  3300 baht ")
    print("-----------------------")
    selectedItem = int(input("Select ur item number : "))
    amount = int(input("Fill Amount : "))
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

        totalprice = (amount * price)
        netprice  =  ((totalprice * 7 ) / 100) + totalprice

        print("-----Bill------------------ ")
        print("1.",itemName, ": ",amount," netprice: ",netprice," baht")
        print("-----****************------ ")
else:
    print("Username or Password  is incorrect")