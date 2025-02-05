nums=int(input("enter the range : "))
x=[]
product=1
for i in range(nums):
    a=int(input("enter the values : "))
    x.append(a)
print(x)
for i in x:
    product*=i
print(product)


