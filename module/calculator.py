import calculator2
def menu():
    print("\nCalculator Menu")
    print("1.Add")
    print("2.Sub")
    print("3.Muti")
    print("4.Div")
    print("5.Exit")
while True:
    menu()
    choice=int(input("enter the choice : "))
    if choice==5:
        print("Program Exitinggg...!!")
        break
    x=int(input("enter first number :"))
    y=int(input("enter second number :"))
    if choice==1:
        print("sum of the numbers =",calculator2.add(x,y))
    elif choice==2:
        print("result of the numbers =",calculator2.sub(x,y))
    elif choice==3:
        print("mul of the numbers =",calculator2.mul(x,y))
    elif choice==4:
        print("div of the numbers =",calculator2.div(x,y))
    
    
