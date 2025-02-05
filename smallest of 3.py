num1=float(input("enter the first number : "))
num2=float(input("enter the second number : "))
num3=float(input("enter the third number : "))
if num1<num2 and num1<num3:
    smallest=num1
elif num2<num1 and num2<num3:
    smallest=num2
else:smallest =num3
print(smallest,"is the smallest")