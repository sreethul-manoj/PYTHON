x=int(input("enter the range : "))
l=[]
for i in range (x):
    a=input("enter the values : ")
    l.append(a)
b=[l[-1]]+l[:-1]
print(b)

