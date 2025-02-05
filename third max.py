x=int(input("enter the range : "))
l=[]
y=[]
for i in range(x):
    a=int(input("enter the list : "))
    l.append(a)
for i in l:
    if i not in y:
     y.append(i)

y.sort(reverse=True)
if len(y)>=3:
   print(y[2])
else:
   print(y[0])
