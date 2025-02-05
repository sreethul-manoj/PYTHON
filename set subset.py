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

if len(z)>=len(w):
    for i in z:
        for j in w:
            if i==j:
                flag+=1
print(z)
print(w)
if flag==y:
    print("its subset")
else:
    print("its not subset")


