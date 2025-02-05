accounts={}
while True:
    print("\n1.Create Acc")
    print("2.Display Acc details")
    print("3.Deposite money")
    print("4.Withdraw money")
    print("5.Delete Acc")
    print("6.Exit")
    choice=int(input("\nenter the choice : "))
    if choice==1:
        acc_no=int(input("enter the Acc number : "))
        if acc_no in accounts:
            print("Account Already Exists!!")
            
        else:
            name=input("enter the name :")
            balance=int(input("deposite amound : "))
            accounts[acc_no]=balance
            print("Account Created!!")
            
    elif choice==2:
        acc_no=int(input("enter the acc no: "))
        if acc_no in accounts:
            print("\nAccount Details")
            print("account number:",acc_no)
            print("account balance:",balance)
            print("account holder:",name)
        else:
            print("\ninvalid Acc number!!")
            
    elif choice==3:
        acc_no=int(input("enter the acc no: "))
        if acc_no in accounts:
            amount=int(input("enter the amount: "))
            if amount>0:
                balance+=amount
                print("Balance: ",balance)
    elif choice==4:
        acc_no=int(input("enter the acc no: "))
        if acc_no in accounts:
            amount=int(input("enter the amount: "))
            if amount>0:
                balance-=amount
                print("Balance: ",balance)
    elif choice==5:
        acc_no=int(input("enter the acc no: "))
        if acc_no in accounts:
            del accounts[acc_no]
            print("Deleted the acc!!")
    elif choice==6:
        break
        



        
        
        

        

        