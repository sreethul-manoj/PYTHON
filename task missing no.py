x=int(input("enter the range : "))
l=[]
for i in range(x):
    a=int(input("enter the list : "))
    l.append(a)
z=max(l)
y=[]
for i in range(1,z):
    y.append(i)
new=[]
for i in y:
    if i not in l:
        new.append(i)
print(new)


