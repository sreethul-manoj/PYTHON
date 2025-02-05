x=int(input("enter the range : "))
l=[]
for i in range (x):
    a=input("enter the values : ")
    l.append(a)
l.sort()
print(l[-2])

