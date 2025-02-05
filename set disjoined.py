x=int(input("enter the range : "))
z=set()
flag=0
for i in range(x):
    a=int(input("enter the set : "))
    z.add(a)

y=int(input("enter the second range : "))
w=set()
for j in range(y):
    b=int(input("enter the subset : "))
    w.add(b)
    
for i in z:
    for j in w:
        if i==j:
            flag=1
if flag!=0:
    print("joined")
else:
    print("not joined")
