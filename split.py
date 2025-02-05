x=int(input("enter the range : "))
l=[]
for i in range(x):
    a=input("enter the values :")
    l.append(a)
z=x//2
print(l[:z])
print(l[z:])