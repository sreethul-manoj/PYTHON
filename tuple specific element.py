x=int(input("enter the range : "))
y=[]
for i in range(x):
    a=int(input("enter the values : "))
    y.append(a)
q=int(input("element :"))
w=tuple(y)
z=w.count(q)
print(f"the occurance of {q} is {z}")
