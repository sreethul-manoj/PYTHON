inventory={}
while True:
    print("\n1.Add a product")
    print("2.Update product quantity")
    print("3.Remove a product from the inventory")
    print("4.View all products in the inventory.")
    print("5.Exit the program")
    choice=int(input("enter the choice : "))
    if choice==1:
        product=input("enter the product name : ")
        if product in inventory:
            print("!! The product already included !!")
        else:
            
            price=input("enter the price of product : ")
            quantity=int(input("enter the product quantity : "))
            inventory[product]={'name': product,'price':price,'quantity':quantity}
            print("!! Product successfully added !!")
    elif choice==2:
        product=input("enter the product name : ")
        if product in inventory:
            quantity=int(input("enter the new quantity :  "))
            inventory[product]={'name': product,'price':price,'quantity':quantity}
            print(inventory)

        else:
            print("!! The product is not exist in inventory !!")
    
    elif choice==3:
        product=input("enter the Remove a product : ")
        if product in inventory:
            del inventory[product]
            print("!! The product is removed !!")
        else:
             print("!! The product is not exist in inventory !!")
    elif choice==4:
        print(inventory)
    elif choice==5:
        print("!! Exiting the program !!")
        break
    else:
        print("invalid choice")


        




            


