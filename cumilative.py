x=int(input("enter the range : "))
l=[]
sum=[]
temp=0
for i in range (x):
    a=int(input("enter the list : "))
    l.append(a)
for i in l:
    temp=temp+i
    sum.append(temp)
print(sum)