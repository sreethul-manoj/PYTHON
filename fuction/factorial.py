def factorial(a):
    fact=1
    for i in range(1,a+1):
        fact*=i
    print(fact)
b=int(input("enter the no : "))
factorial(b)