x=int(input("enter the ranage : "))
l=[]
flag=0
for i in range(x):
    a=input("enter the list : ")
    l.append(a)
a=tuple(l)
spe=input("enter the values : ")
for i in range(x):
    if a[i]==spe:
        flag=1
        print(i)
        break
if flag==0:
    print("-1")
