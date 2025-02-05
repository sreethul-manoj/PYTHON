x=int(input("enter the range : "))
l=[]
l2=[]
for i in range(x):
    a=input("enter the values : ")
    l.append(a)
b=input("enter the removing value : ")
for i in l:
    if i!=b:
        l2.append(i)
print(l2)
