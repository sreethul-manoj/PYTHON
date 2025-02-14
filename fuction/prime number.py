def prime(a):
    flag=True
    if a>1:
        for i in range(2,a):
            if a%i==0:
                flag=False
                break
    if flag==True:
        print("prime")
    else:
        print("not")
n=int(input("enter a number :"))
prime(n)
