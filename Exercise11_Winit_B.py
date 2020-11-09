number = int(input("number :"))

for i in range(number):
    print(" "*(number-i) + ("*" * (2*(i+1)-1)))