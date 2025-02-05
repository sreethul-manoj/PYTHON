x=int(input("enter the range : "))
l=[]
l1=[]
l2=[]
for i in range(x):
    a=input("enter the first list : ")
    l.append(a)
for i in range(x):
    
    b=input("enter the second list  : ")
    l1.append(b)
for i in l:
    for j in l1:
        if i==j:
            l2.append(i)
print(l2)

    