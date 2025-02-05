def fibonacci(s):
    a=0
    b=1
    for i in range(s):
        print(a)
        a,b=b,a+b
s=int(input("enter the range : "))
fibonacci(s)


        