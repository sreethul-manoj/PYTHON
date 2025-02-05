def max(a,b,c):
    if a>b and a>c:
        print(a,"is grater")
    elif b>a and b>c:
        print(b,"is grater")
    else:
        print(c,"is grater")
a=int(input("enter the number : "))
b=int(input("enter the number : "))
c=int(input("enter the number : "))
max(a,b,c)